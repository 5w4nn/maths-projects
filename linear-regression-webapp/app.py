import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="Linear Regression App", layout="centered")

# --- App Title ---
st.title("📈 Linear Regression from Scratch")
st.write(
    "This is an educational tool to explore the math behind linear regression.\n"
    "You can upload your own CSV or generate sample data to see the model in action."
)

st.sidebar.header("Data Input Options")
# --- Sidebar Options ---
upload_option = st.sidebar.radio("Choose Data Input Method:", ("Upload CSV", "Generate Synthetic Data"))
# --- Data Upload ---#
if upload_option == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("Data Preview:", data.head())
    else:
        data = None

