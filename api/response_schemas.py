from pydantic import BaseModel

class PredictionResponse(BaseModel):

    prediction: int

    status: str

    probability: float

    confidence: float

    risk: str

    recommendation: str

class APIResponse(BaseModel):

    success: bool

    data: PredictionResponse

    message: str