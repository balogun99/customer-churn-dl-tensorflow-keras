from pydantic import BaseModel, Field # FastAPI will automatically validate incoming JSON against this schema.
from pydantic import field_validator
from api.enums import (
    gender, Partner, Dependents, PhoneService,
    MultipleLines, InternetService, OnlineSecurity,
    OnlineBackup, DeviceProtection, TechSupport,
    StreamingTV, StreamingMovies, Contract,
    PaperlessBilling, PaymentMethod, MonthlyCharges,
    TotalCharges
)


class CustomerRequest(BaseModel):

    gender: gender

    seniorCitizen: int = Field(ge=1, le=0)

    Partner: Partner

    Dependents: Dependents

    tenure: int = Field(ge=1, le=72)

    PhoneService: PhoneService

    MultipleLines: MultipleLines

    InternetService: InternetService

    OnlineSecurity: OnlineSecurity

    OnlineBackup: OnlineBackup

    DeviceProtection: DeviceProtection

    TechSupport: TechSupport

    StreamingTV: StreamingTV

    StreamingMovies: StreamingMovies

    Contract: Contract

    PaperlessBilling: PaperlessBilling

    PaymentMethod: PaymentMethod

    MonthlyCharges: float = Field(ge=20.0, le=119.99)

    TotalCharges: float = Field(ge=20.03, le=8589.6)

    # @field_validator("Age")
    # @classmethod
    # def validate_age(cls, value):
    #     if value < 18:
    #         raise ValueError(
    #             "Customer must be at least 18 years old."
    #         )
    #     return value

    