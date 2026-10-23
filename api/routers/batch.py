# import libraries
import io

import pandas as pd

from fastapi import (
    APIRouter,
    File,
    UploadFile,
    HTTPException
)

from fastapi.responses import StreamingResponse

from api.dependencies import (
    model_service,
    preprocessor_service
)

# create router
router = APIRouter(
    prefix="/batch",
    tags=["Batch Prediction"]
)

# columns in the dataset
REQUIRED_COLUMNS = [
    "CreditScore",
    "Geography",
    "Gender",
    "Age",
    "Tenure",
    "Balance",
    "NumOfProducts",
    "HasCrCard",
    "IsActiveMember",
    "EstimatedSalary"
] # These must match the features used during training.

# create endpoint
@router.post("/predict")
async def batch_predict(
    file: UploadFile = File(...)
):
    # validate file type
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
        status_code=400,
        detail="Only CSV files are supported."
    )

    # read the CSV File
    try:
        df = pd.read_csv(file.file)
    except Exception as e:
        raise HTTPException(
        status_code=400,
        detail=f"Invalid CSV file: {e}"
    )

    # batch upload size
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

    # after reading the file upload
    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
        status_code=413,
        detail="Uploaded file exceeds 5 MB."
    )

    # validate required columns
    missing = [
    col for col in REQUIRED_COLUMNS
    if col not in df.columns
]

    if missing:
        raise HTTPException(
        status_code=400,
        detail={
            "message": "Missing required columns.",
            "missing_columns": missing
        }
    ) # This produces a clearer error than allowing preprocessing to fail.

    # apply preprocessing
    processed = preprocessor_service.transform(df)

    # make predictions
    probabilities = model_service.predict(
    processed
).flatten()

    predictions = (
    probabilities >= 0.5
).astype(int)

    # add result columns
    df["Prediction"] = predictions

    df["Probability"] = probabilities

    df["Status"] = df["Prediction"].map({
    0: "Stay",
    1: "Churn"
})

    df["Risk"] = df["Probability"].apply(
    risk_level
)

    df["Recommendation"] = df[
    "Prediction"
].apply(recommendation)

    # add risks level
    def risk_level(prob):

        if prob < 0.30:
            return "Low"

        if prob < 0.70:
            return "Medium"

        return "High"

    # business recommendations
    def recommendation(pred):

        if pred == 1:
            return "Offer retention incentive."

        return "Continue engagement."

    # return JSON - For small and medium datasets, JSON is convenient
    return {
    "total_customers": len(df),
    "predicted_churn": int(df["Prediction"].sum()),
    "predicted_stay": int(
        (df["Prediction"] == 0).sum()
    ),
    "results": df.to_dict(
        orient="records"
    )
}

# CSV download endpoint - For large datasets, returning a downloadable CSV is more efficient.
@router.post("/download")
async def batch_download(
    file: UploadFile = File(...)
):
    # load the dataset
    df = pd.read_csv(file.file)
    # After generating predictions
    buffer = io.StringIO()

    df.to_csv(
    buffer,
    index=False
)

    buffer.seek(0)

    # return - This lets clients download the processed CSV directly
    return StreamingResponse(
    iter([buffer.getvalue()]),
    media_type="text/csv",
    headers={
        "Content-Disposition":
        "attachment; filename=predictions.csv"
    }
)