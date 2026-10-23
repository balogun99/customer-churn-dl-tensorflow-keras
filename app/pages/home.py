# import libraries
from sklearn import metrics
import streamlit as st
import pandas as pd
from pathlib import Path

from components.sidebar import build_sidebar

# configure the page
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

build_sidebar()

# main header
st.title("🤖 Customer Churn Prediction System")

st.markdown("""
A production-ready **Deep Learning** application built using:

- TensorFlow 2.x
- Keras 3
- Streamlit
- FastAPI
- Scikit-learn

This system predicts whether a customer is likely to churn based on account and demographic information.
""")

# dataset overview
# Create four metric cards.
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Customers",
        "10,000"
    )

with col2:
    st.metric(
        "Features",
        "11"
    )

with col3:
    st.metric(
        "Classes",
        "2"
    )

with col4:
    st.metric(
        "Task",
        "Binary Classification"
    )

# model information
st.subheader("🧠 Neural Network")

st.markdown("""
Architecture

Input

↓

Dense(128)

↓

BatchNormalization

↓

Dropout

↓

Dense(64)

↓

BatchNormalization

↓

Dropout

↓

Dense(32)

↓

Sigmoid Output
""")

# load the evaluation metrics
metrics = pd.read_csv("reports/evaluation_metrics.csv")

# convert it into a dictionary
metric_dict = dict(zip(metrics["Metric"], metrics["Value"]))

# model performance
# Create another row of metrics.
st.subheader("📊 Model Performance")

# c1, c2, c3, c4 = st.columns(4)

import streamlit as st

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Accuracy",
    f"{metric_dict['Accuracy']:.2%}"
)

c2.metric(
    "Precision",
    f"{metric_dict['Precision']:.2%}"
)

c3.metric(
    "Recall",
    f"{metric_dict['Recall']:.2%}"
)

c4.metric(
    "F1 Score",
    f"{metric_dict['F1']:.2%}"
)

c5.metric(
    "ROC AUC",
    f"{metric_dict['ROC-AUC']:.2%}"
)

# display evaluation figures
from PIL import Image

st.subheader("📈 Training Accuracy")

accuracy_image = Image.open(
    "reports/figures/accuracy_curve.png"
)

st.image(
    accuracy_image,
    use_container_width=True
)

# loss curve
loss_image = Image.open(
    "reports/figures/loss_curve.png"
)

st.image(
    loss_image,
    use_container_width=True
)

# display the confusion matrix
st.subheader("📉 Confusion Matrix")

cm = Image.open(
    "reports/figures/confusion_matrix.png"
)

st.image(
    cm,
    use_container_width=True
)

# display ROC Curve
st.subheader("📈 ROC Curve")

roc = Image.open(
    "reports/figures/roc_curve.png"
)

st.image(
    roc,
    use_container_width=True
)

# project summary
st.subheader("📄 Project Summary")

st.info("""
This application demonstrates an end-to-end Deep Learning workflow:

✔ Data preprocessing

✔ TensorFlow 2.x + Keras 3 model

✔ Model evaluation

✔ Streamlit frontend

✔ FastAPI backend

✔ Docker deployment
""")

# navigation guide
st.subheader("🧭 Navigate")

st.success("""
Use the sidebar to access:

🏠 Home

🔍 Single Prediction

📂 Batch Prediction

📊 Model Evaluation

ℹ️ About
""")

# instead of hardcoding values like:
# st.metric("Accuracy", "86.4%")
# load them from your evaluation results:
# metrics = pd.read_csv("reports/evaluation_metrics.csv")
# Then display the values dynamically. 
# This ensures the dashboard always reflects the latest model evaluation after retraining.

