# load libraries
import streamlit as st

from config import *

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state="expanded"
)

# load CSS
def load_css():

    with open("app/assets/style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# build sidebar
from components.sidebar import build_sidebar

build_sidebar()

# main page
st.title("🤖 Customer Churn Prediction")

st.markdown(
"""
Welcome to the Deep Learning Customer Churn Prediction System.

Use the navigation menu on the left to access:

- Home Dashboard
- Single Prediction
- Batch Prediction
- Model Evaluation
- About
"""
) # When you run the app, Streamlit will automatically detect the pages/ directory and add the pages to the sidebar navigation.

