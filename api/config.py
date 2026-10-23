from pathlib import Path

PROJECT_NAME = "Customer Churn Prediction API"

# VERSION = "1.0.0"

DESCRIPTION = """
REST API for Customer Churn Prediction
using TensorFlow 2.x + Keras 3
"""

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "best_model.keras"

PREPROCESSOR_PATH = BASE_DIR / "models" / "preprocessor.pkl"

API_VERSION = "1.0.0"

MAX_UPLOAD_SIZE = 5 * 1024 * 1024

ALLOWED_ORIGINS = [
    "http://localhost:8501"
]