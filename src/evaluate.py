# import libraries
import pandas as pd
import matplotlib.pyplot as plt

from keras.models import load_model

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report,
    roc_curve,
    precision_recall_curve
)

# load data
X_test = pd.read_csv("data/processed/X_test.csv")

y_test = pd.read_csv(
    "data/processed/y_test.csv"
).squeeze()

# load model
model = load_model(
    "models/best_model.keras"
)

# generate predictions
y_prob = model.predict(X_test) # Prediction probabilities

y_pred = (y_prob >= 0.5).astype(int) # Convert probabilities to labels

# calculate metrics
accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(y_test, y_pred)

recall = recall_score(y_test, y_pred)

f1 = f1_score(y_test, y_pred)

auc = roc_auc_score(y_test, y_prob)

# display them
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")
print(f"ROC-AUC  : {auc:.4f}")

# classification reports
report = classification_report(
    y_test,
    y_pred
)

print(report)

# save the classification report result
with open(
    "reports/classification_report.txt",
    "w"
) as f:
    f.write(report)

# save evaluation metrics results
metrics = pd.DataFrame({
    "Metric":[
        "Accuracy",
        "Precision",
        "Recall",
        "F1",
        "ROC-AUC"
    ],
    "Value":[
        accuracy,
        precision,
        recall,
        f1,
        auc
    ]
})

metrics.to_csv(
    "reports/evaluation_metrics.csv",
    index=False
)

# confusion matrix result
cm = confusion_matrix(
    y_test,
    y_pred
)

plt.figure(figsize=(5,5))

plt.imshow(cm)

plt.colorbar()

plt.xticks([0,1],["Stayed","Churn"])

plt.yticks([0,1],["Stayed","Churn"])

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.title("Confusion Matrix")

for i in range(2):
    for j in range(2):
        plt.text(
            j,
            i,
            cm[i,j],
            ha="center",
            va="center"
        )

plt.savefig(
    "reports/figures/confusion_matrix.png"
)

plt.show()

# ROC Curve - A curve closer to the top-left corner indicates better performance.
fpr, tpr, _ = roc_curve(
    y_test,
    y_prob
)

plt.figure(figsize=(6,5))

plt.plot(fpr, tpr)

plt.plot([0,1],[0,1],"--")

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.savefig(
    "reports/figures/roc_curve.png"
)

plt.show()

# Precision–Recall Curve - This curve is especially informative when dealing with imbalanced datasets.
precision_values, recall_values, _ = precision_recall_curve(
    y_test,
    y_prob
)

plt.figure(figsize=(6,5))

plt.plot(
    recall_values,
    precision_values
)

plt.xlabel("Recall")

plt.ylabel("Precision")

plt.title("Precision–Recall Curve")

plt.savefig(
    "reports/figures/precision_recall_curve.png"
)

plt.show()

# Training Accuracy Curve
# Load the training history
history = pd.read_csv(
    "reports/training_history.csv"
)

# plot
plt.figure(figsize=(7,5))

plt.plot(
    history["accuracy"],
    label="Training"
)

plt.plot(
    history["val_accuracy"],
    label="Validation"
)

plt.legend()

plt.xlabel("Epoch")

plt.ylabel("Accuracy")

plt.title("Accuracy vs Epoch")

plt.savefig(
    "reports/figures/accuracy_curve.png"
)

plt.show()

# Training Loss Curve
plt.figure(figsize=(7,5))

plt.plot(
    history["loss"],
    label="Training"
)

plt.plot(
    history["val_loss"],
    label="Validation"
)

plt.legend()

plt.xlabel("Epoch")

plt.ylabel("Loss")

plt.title("Loss vs Epoch")

plt.savefig(
    "reports/figures/loss_curve.png"
)

plt.show()

# Interpretation:
# Both curves decreasing together is a good sign.
# If validation loss increases while training loss decreases, the model may be overfitting.