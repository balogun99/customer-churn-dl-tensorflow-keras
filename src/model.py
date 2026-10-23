# import libraries
import keras
import numpy as np
from keras import layers
from keras.utils import plot_model

# define a model-building function (encapsulation)
def build_model(input_dim: int) -> keras.Model:

    model = keras.Sequential([
        layers.Input(shape=(input_dim,)), # Defines the number of input features.

        layers.Dense(128, activation="relu"), # This layer learns the first set of feature interactions.
        
        layers.BatchNormalization(),

        layers.Dropout(0.30),

        layers.Dense(64, activation="relu"),

        layers.BatchNormalization(),

        layers.Dropout(0.20),

        layers.Dense(32, activation="relu"),

        layers.Dense(1, activation="sigmoid")
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=[
            "accuracy",
            "precision",
            "recall",
            "auc"
            # keras.metrics.Precision(name="precision"),
            # keras.metrics.Recall(name="recall"),
            # keras.metrics.AUC(name="auc")
            ]
    )

    plot_model(
    model,
    show_shapes=True,
    show_layer_names=True,
    to_file="reports/model_architecture.png"
    )

    dummy_input = np.random.rand(5, input_dim)

    predictions = model.predict(dummy_input)

    print(predictions)

    return model

if __name__ == "__main__":

    model = build_model(input_dim=20)

    model.summary()

    model.save("models/untrained_model.keras")

    # plot_model(
    # model,
    # show_shapes=True,
    # show_layer_names=True,
    # to_file="reports/model_architecture.png"
    # )

    # import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers