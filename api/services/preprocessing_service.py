# Create the Preprocessing Service
# load libraries
import joblib

from api.config import PREPROCESSOR_PATH
# from api.services import prediction


class PreprocessingService:

    def __init__(self):
        self.pipeline = None

    def load(self):
        self.pipeline = joblib.load(
            PREPROCESSOR_PATH
        )

    def transform(self, df):
        return self.pipeline.transform(df)
    
    #     try:
    #         processed = preprocessor_service.transform(df)
    #         probability = float(
    #             model_service.predict(processed)[0][0]
    #         )
    #     except Exception as e:
    #         return {
    #             "error": str(e)
    # }

#     raise HTTPException(
#     status_code=500,
#     detail="Prediction failed."
# )