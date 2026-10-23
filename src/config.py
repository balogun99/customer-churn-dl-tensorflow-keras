from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw" / "customer_churn_data.csv"
PROCESSED_DATA = BASE_DIR / "data" / "processed"
MODEL_DIR = BASE_DIR / "models"