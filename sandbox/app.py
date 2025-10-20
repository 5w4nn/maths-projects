import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# title
st.set_page_config(page_title="KNN and other algorithms", layout="centered")

st.title("KNN and other algorithms,")

# read le csv
def read_csv(file):
  if file is not None:
    df = pd.read_csv(file)
    st.write("Data Preview", df.head())
    parse_data(df)
  else:
    return None
  return df


# parse the data to be ready to have its euclidean distance calculated
def parse_data(data_frame):
  x = np.arange(data_frame[0])
  st.write(x)
  return x

# calculate euclidean distance of each data point
#def euclidean_distance(array):
#  return float(np.linalg.norm(array))"""

# sidebar
st.sidebar.header("Data Input Options")
upload_option = st.sidebar.radio("Choose Data Input Method:", ("Upload CSV", "Generate Synthetic Data"))
if upload_option == "Upload CSV":
  uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])
  if uploaded_file is not None:
    read_csv(uploaded_file)
    # euclidean_distance(uploaded_file)
  else:
    data = None

# generator data using class number, label names and colours, amount of points and scatter options need to continue adding a numerical value for labels and the labels names
# should i just use a damn freaking dataset? -> Probably yes
else:
  label_numb = st.sidebar.number_input("Insert number of classes (labels) for classification 1-5",min_value=1, max_value=5, format="%0f")
  label_numerical = st.sidebar.number_input("Enter the classification label for each class you just created", min_value=1,)


# Fit data to be used for KNN



# Display data