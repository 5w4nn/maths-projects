import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# title
st.set_page_config(page_title="KNN and other algorithms", layout="centered")

st.title("KNN and other algorithms,")

# read le csv
def read_csv(uploaded_file):
  df = pd.read_csv(uploaded_file)
  st.dataFrame(df.head()) # display the mf data

# calculate euclidean distance of each data point
def euclidean_distance(row1, row2):
  row1 = 1
  row2 = 2
  st.write(row1 + row2)
  return None

# sidebar
st.sidebar.header("Data Input Options")
upload_option = st.sidebar.radio("Choose Data Input Method:", ("Upload CSV", "Generate Synthetic Data"))
if upload_option == "Upload CSV":
  uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
  if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview", data.head())
    euclidean_distance()
  else:
    data = None

# generator data using class number, label names and colours, amount of points and scatter options need to continue adding a numerical value for labels and the labels names
# should i just use a damn freaking dataset? -> Probably yes
else:
  label_numb = st.sidebar.number_input("Insert number of classes (labels) for classification 1-5",min_value=1, max_value=5, format="%0f")
  label_numerical = st.sidebar.number_input("Enter the classification label for each class you just created", min_value=1,)


# Fit data to be used for KNN



# Display data