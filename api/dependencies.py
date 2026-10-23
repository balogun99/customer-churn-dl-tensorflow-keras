from api.services.model_service import ModelService
from api.services.preprocessing_service import (
    PreprocessingService
)

model_service = ModelService()

preprocessor_service = PreprocessingService()
# NB -These objects will be shared across requests.