# import libraries
import pandas as pd
import keras
from model import build_model
from keras.models import load_model

from keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau,
    CSVLogger
)

# load processed dataset
X_train = pd.read_csv("data/processed/X_train.csv")
X_val = pd.read_csv("data/processed/X_val.csv")

y_train = pd.read_csv("data/processed/y_train.csv").squeeze()
y_val = pd.read_csv("data/processed/y_val.csv").squeeze()

# build the model
model = build_model(input_dim=X_train.shape[1])

# compile the model
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=[
        "accuracy",
        "precision",
        "recall",
        "auc"
    ]
)

# configure callbacks
# Stops training when validation loss stops improving.
early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=10,
    restore_best_weights=True
)

# ModelCheckpoint
# Saves the best model.
checkpoint = ModelCheckpoint(
    filepath="models/best_model.keras",
    monitor="val_loss",
    save_best_only=True
)

# ReduceLROnPlateau
# Reduces the learning rate if validation loss plateaus.
reduce_lr = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=5,
    min_lr=1e-6
)

# CSVLogger
# Logs training metrics after every epoch.
csv_logger = CSVLogger(
    "reports/training_history.csv"
)

# train the model
history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=100,
    batch_size=32,
    callbacks=[
        early_stopping,
        checkpoint,
        reduce_lr,
        csv_logger
    ],
    verbose=1
)

# save the final model
# Even though ModelCheckpoint saves the best model, you can also save the final state
model.save("models/churn_model.keras")

# save the training history
# Convert the history to a DataFrame.
history_df = pd.DataFrame(history.history)

history_df.to_csv(
    "reports/training_history.csv",
    index=False
)

# inspect training history
print(history_df.head())

best_model = load_model("models/best_model.keras")

print("Model loaded successfully!")

# other metrices
# keras.metrics.Precision(name="precision"),
        # keras.metrics.Recall(name="recall"),
        # keras.metrics.AUC(name="auc")