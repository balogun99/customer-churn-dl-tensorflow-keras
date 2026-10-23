# import libraries
import pandas as pd

from fastapi import APIRouter
from api.schemas import CustomerRequest
from api.response_schemas import PredictionResponse
from fastapi import HTTPException
from api.dependencies import (
    model_service,
    preprocessor_service
)

# create router
router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)

# validate model availability (before prediction)
# if model_service.model is None:
#     raise HTTPException(
#         status_code=503,
#         detail="Model not LOADED"      
#     )

# Create Prediction Endpoint 
@router.post("/")
def predict(customer: CustomerRequest):
        df = pd.DataFrame([

        customer.model_dump() # NB: Using model_dump() is the recommended approach with Pydantic v2

    ])
        
        processed = preprocessor_service.transform(df)

        # prediction
        probability = float(

        model_service.predict(
            processed
        )[0][0]

    )

        prediction = int(
        probability >= 0.5
    )

        try:

            processed = preprocessor_service.transform(df)
            probability = float(
            model_service.predict(processed)[0][0]
            )

        except Exception as e:
             raise HTTPException( # The global exception handler will take care of formatting the response.
                status_code=500,
                detail="Prediction failed."
            )

        # risk level
        if probability < 0.30:

            risk = "Low"

        elif probability < 0.70:

            risk = "Medium"

        else:

            risk = "High"

    # recommendation
        if prediction:

            recommendation = (
            "Offer retention incentive."
        )

        else:

            recommendation = (
            "Continue normal engagement."
        )
            
    # return JSON
        return {

        "prediction": prediction,

        "status": (
            "Churn"
            if prediction
            else "Stay"
        ),

        "probability": round(
            probability,
            4
        ),

        "confidence": round(
            max(
                probability,
                1 - probability
            ),
            4
        ),

        "risk": risk,

        "recommendation":
            recommendation
    }

        # except Exception as e:
        # return {
        #     "error": str(e)
        # }
# run the api - uvicorn api.main:app --reload