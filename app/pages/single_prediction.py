
# 0 => No
# 1 => Yes

# 1305.5 => Churn = Yes, Model => Likely to Churn
# 491.55 => Churn No, Model => Likely to Churn


# 652.5 => Churn = No, Model => Likely to Churn - corr
# 483.52 => Churn No, Model => Likely to Churn - likely to remain

# Female	1	No	No	10	Yes	No	No	No internet service	No internet service	No internet service	No internet service	No internet service	No internet service	Two year	No	Bank transfer	65.25	652.5	(0) No - likely to churn 
# Male	0	No	Yes	8	No	No phone service	Fiber optic	No	No	Yes	No	Yes	Yes	One year	Yes	Bank transfer	60.44	483.52	Yes - churn

import pandas as pd
import streamlit as st

from components.sidebar import build_sidebar
from utils import load_dl_model, load_preprocessor

st.set_page_config(
    page_title="Single Prediction",
    page_icon="🔍",
    layout="wide"
)

build_sidebar()

st.title("🔍 Single Customer Prediction")
st.write("Enter the customer's information below and click **Predict**.")

model = load_dl_model()
preprocessor = load_preprocessor()

with st.form("prediction_form"):

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

    with col2:
        SeniorCitizen = st.number_input(
            "Senior Citizen",
            0,
            1
        )

    with col3:    
        Partner = st.selectbox(
            "Partner",
            ["No", "Yes"]
        )

    with col4:    
        Dependents = st.selectbox(
            "Dependents",
            ["No", "Yes"]
        )

    with col5:
        tenure = st.number_input(
            "Tenure",
            min_value=1,
            max_value=72
        )

    with col1:
        PhoneService = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

    with col2:
        MultipleLines = st.selectbox(
            "Multiple Lines",
            ["Yes", "No", "No phone service"]
        )

    with col3:
        InternetService = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

    with col4:
        OnlineSecurity = st.selectbox(
            "Online Security",
            ["Yes", "No", "No internet service"]
        )

    with col5:
            OnlineBackup = st.selectbox(
            "Online Backup",
            ["Yes", "No", "No internet service"]
        )

    with col1:
            DeviceProtection = st.selectbox(
            "Device Protection",
            ["Yes", "No", "No internet service"]
        )

    with col2:
            TechSupport = st.selectbox(
            "Tech Support",
            ["Yes", "No", "No internet service"]
        )

    with col3:
            StreamingTV = st.selectbox(
            "Streaming TV",
            ["Yes", "No", "No internet service"]
        )

    with col4:
            StreamingMovies = st.selectbox(
            "Streaming Movies",
            ["Yes", "No", "No internet service"]
        )

    with col5:
            Contract = st.selectbox(
            "Contract",
            ["One Year", "Two Year", "Month-to-month"]
        )

    with col1:
        PaperlessBilling = st.selectbox(
            "Paperless Billing",
            ["Yes", "No"]
        )

    with col2:
        PaymentMethod = st.selectbox(
            "Payment Method",
            [
            "Bank transfer",
            "Credit card",
            "Electronic check",
            "Mailed check"
            ]
        )

    with col3:
        MonthlyCharges = st.number_input(
            "Monthly Charges",
            min_value=20.0,
            max_value=119.99
            # value=5555
        )

    with col4:
        TotalCharges = st.number_input(
            "Total Charges",
            min_value=20.03,
            max_value=8589.6
        )

    predict_button = st.form_submit_button(
        "Predict"
    )

# 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges'

if predict_button:

    input_df = pd.DataFrame({
        "gender":[gender],
        "SeniorCitizen":[SeniorCitizen],
        "Partner":[Partner],
        "Dependents":[Dependents],
        "tenure":[tenure],
        "PhoneService":[PhoneService],
        "MultipleLines":[MultipleLines],
        "InternetService":[InternetService],
        "OnlineSecurity":[OnlineSecurity],
        "OnlineBackup":[OnlineBackup],
        "DeviceProtection":[DeviceProtection],
        "TechSupport":[TechSupport],
        "StreamingTV":[StreamingTV],
        "StreamingMovies":[StreamingMovies],
        "Contract":[Contract],
        "PaperlessBilling":[PaperlessBilling],
        "PaymentMethod":[PaymentMethod],
        "MonthlyCharges":[MonthlyCharges],
        "TotalCharges":[TotalCharges]
    })

    # st.write(input_df.columns.tolist())

    processed_input = preprocessor.transform(input_df)

    probability = model.predict(
    processed_input,
    verbose=0
    )[0][0]

    prediction = int(probability >= 0.5)

    st.subheader("Prediction Result")

    # if prediction == 0: # NO #mine
    
    #     st.error("✅ Customer is likely to stay.")
    
    # else:
    
    #     st.success("⚠️ Customer is likely to churn.")

    if prediction == 1: #chatgpt

        st.error("⚠️ Yes, Customer is likely to churn.")

    else:

        st.success("✅ No, Customer is likely to stay.")


        st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

        confidence = max(
        probability,
        1 - probability
    )

        st.metric(
        "Model Confidence",
        f"{confidence*100:.2f}%"
    )

        st.subheader("Business Recommendation")

        # if churn is predicted

    if prediction == 1:

        st.warning("""
The customer is at high risk of leaving.

Recommended actions:

• Offer a retention discount.

• Contact the customer.

• Investigate recent complaints.

• Assign a relationship manager.
""")

    else:
        st.info("""
The customer appears likely to remain.
        
Recommended actions:
        
• Continue regular engagement.
        
• Promote premium services.
        
• Encourage additional product adoption.
""")
        
# # display input summary & probability guage
    st.subheader("Customer Information")

    st.dataframe(input_df)

# risk categories
    if probability < 0.30:
        risk = "**Low**"

    elif probability < 0.70:
        risk = "**Medium**"

    else:
        risk = "**High**"

# display it
    st.metric("**Risk Level**", risk)

# prediction timestamp
from datetime import datetime

st.caption(
    f"Prediction generated on: {datetime.now():%Y-%m-%d %H:%M:%S}"
)

# Female	1	No	No	10	Yes	No	No	No internet service	No internet service	No internet service	No internet service	No internet service	No internet service	Two year	No	Bank transfer	65.25	652.5	(0) No - likely to churn 
# Male	0	No	Yes	8	No	No phone service	Fiber optic	No	No	Yes	No	Yes	Yes	One year	Yes	Bank transfer	60.44	483.52	Yes - churn
