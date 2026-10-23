# Architecture Workflow
# Client
#    │
# HTTP POST
#    │
#    ▼
# FastAPI
#    │
# Request Validation
#    │
#    ▼
# Preprocessor
#    │
#    ▼
# TensorFlow Model
#    │
#    ▼
# Prediction
#    │
#    ▼
# JSON Response

# load libraries
# create model service
from keras.models import load_model

from api.config import MODEL_PATH


class ModelService:
    def __init__(self):
        self.model = None

    def load(self):
        self.model = load_model(MODEL_PATH)

    def predict(self, processed_data):
        return self.model.predict(
            processed_data,
            verbose=0
        )
    

