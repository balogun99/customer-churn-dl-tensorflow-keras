from fastapi import APIRouter
from api.config import API_VERSION
from datetime import datetime
from api.config import API_VERSION

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health_check():

    return {
        "status": "healthy",
        "message": "API is running successfully."
    }

@router.get("/version")
def version():

    return {
        "version": API_VERSION
    }

# improve health endpoint
@router.get("/")
def health_check():
    return {
        "status": "healthy",
        "version": API_VERSION,
        "timestamp": datetime.utcnow().isoformat(),
        "model_loaded": True,
        "preprocessor_loaded": True,
        "success": True,
        "message": "Prediction completed successfully.",
        "data": {
            "prediction": 1,
            "status": "Churn",
            "probability": 0.91
    }
}
