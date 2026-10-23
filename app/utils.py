# import libraries
import joblib
import streamlit as st

from keras.models import load_model

from config import MODEL_PATH
from config import PREPROCESSOR_PATH

# cached the models
@st.cache_resource
def load_dl_model():

    return load_model(MODEL_PATH)

# cache the preprocessor
@st.cache_resource
def load_preprocessor():

    return joblib.load(PREPROCESSOR_PATH)

# NB: Using @st.cache_resource ensures the model and 
# preprocessing pipeline are loaded only once, improving app performance.