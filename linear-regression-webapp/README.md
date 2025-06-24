# 📈 Linear Regression Web App

A simple, interactive web application built with Python and Streamlit that demonstrates **linear regression** from scratch using **NumPy**. This project is part of a larger series exploring the mathematics behind machine learning.

---

## 🎯 Project Goal

To build an educational and useful web tool that:
- Helps users understand how linear regression works.
- Lets users upload or generate data, visualize it, and fit a linear model to it.
- Reinforces concepts from **linear algebra** (matrix multiplication, transpose, inverse) and **calculus** (optimization, cost function minimization).

---

## 📊 Features

- Upload your own CSV file or use example data
- Visualize the raw data and regression line
- View the learned parameters (slope & intercept)
- See the cost function and how it changes with different parameters

---

## 🧮 The Math Behind It

This app uses the **closed-form solution** to linear regression, also known as the **normal equation**:
$
\theta = (X^T X)^{-1} X^T y
$

Where:

- \( X \) is the feature matrix (with a column of 1s for bias),
- \( y \) is the target vector,
- \( \theta \) is the learned parameter vector.

This solution comes from minimizing the mean squared error (MSE) cost function with respect to $ \theta $
$
J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} \left( h_\theta(x^{(i)}) - y^{(i)} \right)^2
$
---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/maths-projects.git
cd maths-projects/linear-regression-webapp

2. Set up the virtual environment
bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For macOS/Linux

3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Run the app
bash
Copy
Edit
streamlit run app.py

📁 File Structure
bash
Copy
Edit
linear-regression-webapp/
│
├── app.py                # Main Streamlit app
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── .gitignore            # Git exclusions
└── venv/                 # Virtual environment (excluded from Git)

📂 Example Data
If the user doesn't upload a CSV file, the app provides generated test data using a random linear function with added noise.

Expected CSV format:

c
Copy
Edit
x,y
1,2.1
2,4.3
3,5.9

✅ Technologies Used
Python

NumPy

Pandas

Streamlit

Matplotlib

🧠 What You'll Learn
Linear algebra: matrix notation, dot products, transposes, inverse matrices

Calculus: cost function minimization via derivatives

Programming: building apps in Python, file handling, plotting, structuring code

Git & GitHub: project structure, commits, version control

📜 License
This project is open-source and licensed under the MIT License.

🙋‍♂️ Want to Learn More?
This is part of a personal learning journey through the mathematics behind machine learning. Feel free to explore other projects in this repository and star or fork the repo if you're interested in contributing or following along.

yaml
Copy
Edit

---


