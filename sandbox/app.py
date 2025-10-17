import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="KNN and other algorithms", layout="centered")

st.title("KNN and other algorithms,")

# --- sidebar ---
st.sidebar.header("Data Input Options")
upload_option = st.sidebar.radio("Choose Data Input Method:", ("Upload CSV", "Generate Synthetic Data"))
if upload_option == "Upload CSV":
  uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
  if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview", data.head())
  else:
    data = None

# generator data using class number, label names and colours, amount of points and scatter options
else:
  label_numb = st.sidebar.number_input("Insert number of classes (labels) for classification 1-5",min_value=1, max_value=5, format="%0f")


df = pd.DataFrame({
  'first column': [1,2,3,4],
  'second column':[10,20,30,40]
})
df