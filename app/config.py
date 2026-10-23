from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "best_model.keras"

PREPROCESSOR_PATH = BASE_DIR / "models" / "preprocessor.pkl"

REPORTS_PATH = BASE_DIR / "reports"

FIGURES_PATH = REPORTS_PATH / "figures"

APP_TITLE = "Customer Churn Prediction"

APP_ICON = "🤖"

LAYOUT = "wide"