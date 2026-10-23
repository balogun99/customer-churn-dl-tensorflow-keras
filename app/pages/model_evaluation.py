# import libraries
import pandas as pd
import streamlit as st
from pathlib import Path
from PIL import Image

from components.sidebar import build_sidebar

# configure page
st.set_page_config(
    page_title="Model Evaluation",
    page_icon="📊",
    layout="wide"
)

build_sidebar()

st.title("📊 Model Evaluation Dashboard")

# load evaluation metrics
metrics = pd.read_csv(
    "reports/evaluation_metrics.csv"
)

# display evaluation metrics
st.subheader("Evaluation Metrics")
cols = st.columns(5)

for column, (_, row) in zip(cols, metrics.iterrows()):
    with column:
        st.metric(
            row["Metric"],
            f"{row['Value']:.4f}"
        )

# load figures
accuracy_curve = Image.open(
    "reports/figures/accuracy_curve.png"
)

loss_curve = Image.open(
    "reports/figures/loss_curve.png"
)

cm = Image.open(
    "reports/figures/confusion_matrix.png"
)

roc = Image.open(
    "reports/figures/roc_curve.png"
)

pr = Image.open(
    "reports/figures/precision_recall_curve.png"
)

# training curves
st.header("Training History")

left, right = st.columns(2)

with left:

    st.image(
        accuracy_curve,
        use_container_width=True
    )

with right:

    st.image(
        loss_curve,
        use_container_width=True
    )

# Precision–Recall Curve
st.image(
    pr,
    use_container_width=True
)

# Classification Report
with open(
    "reports/classification_report.txt"
) as f:

    report = f.read()

st.subheader("Classification Report")

st.code(report)

# Download Metrics

csv = metrics.to_csv(index=False)

st.download_button(
    "⬇ Download Metrics",
    csv,
    "evaluation_metrics.csv",
    "text/csv"
)

# Download Classification Report
st.download_button(
    "⬇ Download Report",
    report,
    "classification_report.txt"
)

# About Page