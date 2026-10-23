# import libraries
import pandas as pd
import streamlit as st

from components.sidebar import build_sidebar
from utils import load_dl_model, load_preprocessor

# configure the page
st.set_page_config(
    page_title="Batch Prediction",
    page_icon="📂",
    layout="wide"
)

build_sidebar()

st.title("📂 Batch Customer Prediction")

st.write(
    "Upload a CSV file containing customer records to predict churn."
)

# load the model
model = load_dl_model()

preprocessor = load_preprocessor()

# file upload
uploaded_file = st.file_uploader(
    "Upload Customer CSV",
    type=["csv"]
)

if uploaded_file is not None:

    # Read uploaded file
    df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")

    st.subheader("Preview of Uploaded Data")

    st.dataframe(df.head())

    st.write(f"Number of Customers: **{len(df)}**")

    st.divider()

    if st.button("Predict"):

        try:

            # Transform the data
            processed_data = preprocessor.transform(df)

            # Predict probabilities
            probabilities = model.predict(processed_data)

            # Convert to binary predictions
            predictions = (probabilities > 0.5).astype(int)

            # Add results
            df["Churn Probability"] = probabilities.flatten()

            df["Prediction"] = predictions.flatten()

            df["Prediction"] = df["Prediction"].map({
                0: "No Churn",
                1: "Churn"
            })

            st.success("✅ Prediction Completed!")

            st.subheader("Prediction Results")

            st.dataframe(df)

        
            # Download button
            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="⬇ Download Results",
                data=csv,
                file_name="batch_predictions.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"Prediction Error: {e}")

    # else:

    #     st.info("👆 Please upload a CSV file to continue.")