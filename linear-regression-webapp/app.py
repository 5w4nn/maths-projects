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

# --- Data Generation ---
else:
    num_points = st.sidebar.slider("Number of Data Points", 10, 200, 75)
    slope = st.sidebar.slider("Gradient (m)", -10.0, 10.0, 2.0)
    intercept = st.sidebar.slider("Intercept (b)", -20.0, 20.0, 5.0)
    noise_level = st.sidebar.slider("Noise Level", 0.0, 10.0, 2.0)
    x = np.linspace(0, 20, num_points)
    y = slope * x + intercept + np.random.normal(0, noise_level, num_points)
    data = pd.DataFrame({"x": x, "y": y})
    

# --- Display Data ---
if data is not None:
    st.subheader("Data Preview")
    #st.write(data.head())

    fig, ax = plt.subplots()
    ax.scatter(data['x'], data['y'], color='purple', label='Data Points')
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    st.pyplot(fig)
else:
    st.warning("Please upload a CSV file or generate synthetic data to proceed.")


# --- The fun bit (maths) --- #
if data is not None:
    x = data["x"].values
    y = data["y"].values

    x = x.reshape(-1,1)
    X = np.column_stack((np.ones(x.shape[0]),x))
    st.write(X) #the above code puts x into a matrix with the first column being 1s to represent the intercept


#TODO: keep reading on normal equation linear regression.