# import libraries
import logging

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    ),
)

# Use this logger throughout the project instead of print()
logger = logging.getLogger("customer_churn_api")