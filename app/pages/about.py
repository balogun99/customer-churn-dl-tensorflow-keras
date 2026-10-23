# import libraries
import streamlit as st
import tensorflow as tf
import keras
import streamlit as stlib
from components.sidebar import build_sidebar

# configure page
st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

build_sidebar()

st.title("ℹ️ About")

# project discription
st.markdown("""
# Customer Churn Prediction System

This project demonstrates an end-to-end Deep Learning workflow for predicting customer churn.

The application includes:

- Data preprocessing
- Deep Neural Network
- Model evaluation
- Streamlit frontend
- FastAPI backend
- Docker deployment

The model predicts whether a customer is likely to leave based on historical customer information.
""")

# technology stack
st.header("Technology Stack")

stack = {
    "TensorFlow": tf.__version__,
    "Keras": keras.__version__,
    "Streamlit": stlib.__version__,
    "Python": "3.12+"
}

st.table(stack)

# model information
st.header("Model Workflow")

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

Dense(1)

↓

Sigmoid
""")

# features
st.header("Application Features")

st.success("✔ Single Prediction")

st.success("✔ Batch Prediction")

st.success("✔ Model Evaluation")

st.success("✔ Download Results")

st.success("✔ FastAPI Integration")

st.success("✔ Docker Ready")

# future improvements
st.header("Future Work")

st.info("""
Possible improvements

• Explainable AI (SHAP)

• Authentication

• Database Integration

• Cloud Deployment

• CI/CD Pipeline

• Monitoring

• Retraining Pipeline

• MLflow Experiment Tracking

• Kubernetes Deployment
""")

# author details
st.header("Author")

st.write("Balogun Ishaq Murtala")

st.write("Machine Learning Engineer")

st.write("TensorFlow • Keras • Python • Streamlit")