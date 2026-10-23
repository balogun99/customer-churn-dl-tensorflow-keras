# import libraries
import time
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.utils.logger import logger
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import HTTPException

from api.config import (
    PROJECT_NAME,
    API_VERSION,
    DESCRIPTION
)

from api.routers.health import router as health_router
from api.dependencies import (
    model_service,
    preprocessor_service
)
from api.routers.prediction import (
    router as prediction_router
)
from api.routers.batch import (
    router as batch_router
)

# Lifespan Events
# Instead of the deprecated @app.on_event("startup"), 
# use the recommended lifespan pattern.
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting Customer Churn API...")
    # Model loading will be added here in Lesson 9.2
    yield
    print("🛑 Shutting down Customer Churn API...")

# Create the FastAPI App
app = FastAPI(
    title=PROJECT_NAME,
    version=API_VERSION,
    description=DESCRIPTION,
    lifespan=lifespan
)

# Configure CORS - This allows your Streamlit frontend to communicate with the API during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(health_router)
app.include_router(prediction_router)
app.include_router(batch_router)

# Root Endpoint
@app.get("/")
def home():

    return {
        "application": PROJECT_NAME,
        "version": API_VERSION,
        "status": "running"
    }

@asynccontextmanager # This ensures the model and preprocessor are loaded only once when the API starts.
async def lifespan(app: FastAPI):

    print("Loading model...")

    model_service.load()

    print("Loading preprocessor...")

    preprocessor_service.load()

    print("API Ready.")

    yield

    print("Shutdown Complete.")

logger.info("Loading TensorFlow model...")
logger.info("Loading preprocessing pipeline...")
logger.info("API started successfully.")
logger.info("API shutting down.")


# handle HTTP Exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    exc: HTTPException,
):
    logger.warning(
        f"HTTP {exc.status_code}: {exc.detail}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.detail,
        },
    )

# Handle Unexpected Exceptions - Notice that the client receives a generic message, 
# while the full traceback is kept in the server logs.
@app.exception_handler(Exception)
async def general_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception("Unexpected server error")

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": (
                "Internal server error."
            ),
        },
    )

# Request Logging Middleware
@app.middleware("http")
async def log_requests(
    request: Request,
    call_next,
):
    start = time.time()

    response = await call_next(request)

    duration = time.time() - start

    logger.info(
        "%s %s -> %s (%.3fs)",
        request.method,
        request.url.path,
        response.status_code,
        duration,
    )

    return response

# run the API - uvicorn api.main:app --reload
# project url -https://chatgpt.com/c/6a529cda-b44c-83ea-8981-e6cea9b66bbb