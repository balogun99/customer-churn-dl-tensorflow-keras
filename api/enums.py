from enum import Enum

# to change this later with the current dataset
class gender(str, Enum):
    male = "Male"
    female = "Female"

class Partner(str, Enum):
    yes = "Yes"
    no = "No"

class Dependents(str, Enum):
    yes = "Yes"
    no = "No"

class PhoneService(str, Enum):
    yes = "Yes"
    no = "No"

class MultipleLines(str, Enum):
    yes = "Yes"
    no = "No"
    no_phone_service = "No Phone Service"

class InternetService(str, Enum):
    dsl = "DSL"
    fiber_optic = "Fiber Optic"
    no = "No"

class OnlineSecurity(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No Internet Service"

class OnlineBackup(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No Internet Service"

class DeviceProtection(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No Internet Service"

class TechSupport(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No Internet Service"

class StreamingTV(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No Internet Service"

class StreamingMovies(str, Enum):
    yes = "Yes"
    no = "No"
    no_internet_service = "No Internet Service"

class Contract(str, Enum):
    one_year = "One Year"
    two_year = "Two Year"
    month_to_month = "Month-to-Month"

class PaperlessBilling(str, Enum):
    yes = "yes"
    no = "no"

class PaymentMethod(str, Enum):
    bank_transfer = "Bank Transfer"
    credit_card = "Credit Card"
    electronic_check = "Electronic Check"
    mailed_check = "Mailed Check"

class MonthlyCharges(float, Enum):
    monthly_charges = "MonthlyCharges"
    ge=20.0,
    le=119.99

class TotalCharges(float, Enum):
    total_charges = "TotalCharges"
    ge=20.03,
    le=8589.6
