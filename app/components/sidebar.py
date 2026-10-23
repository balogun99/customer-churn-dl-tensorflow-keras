# import libraries - This sidebar will appear consistently across all pages.
import streamlit as st

def build_sidebar():

    with st.sidebar:

        st.title("🤖 Customer Churn")

        st.markdown("---")

        st.success("TensorFlow 2.x")

        st.success("Keras 3")

        st.success("Streamlit")

        st.markdown("---")

        st.info(
            """
            End-to-End Deep Learning Project

            Built with TensorFlow + Keras
            """
        )