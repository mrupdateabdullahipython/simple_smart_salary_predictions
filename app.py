# app.py
# 💼 SalarySense AI (NEW CLEAN PREMIUM VERSION)
# Works easier + no PDF package needed

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Simple Smart Salary Estimator",
    page_icon="💼",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("salary_model.pkl")
training_columns = joblib.load("training_columns.pkl")

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
            url("background.jpg");
background-size: cover;
background-position: center;
background-attachment: fixed;
}

h1,h2,h3,h4,p,label {
color:white !important;
}

.block-container {
background: rgba(255,255,255,0.08);
padding: 2rem;
border-radius: 20px;
backdrop-filter: blur(10px);
}

.stButton>button {
background: linear-gradient(90deg,#22c55e,#16a34a);
color:white;
border:none;
border-radius:12px;
height:50px;
width:100%;
font-size:18px;
font-weight:bold;
}

@keyframes fadeIn {
from {opacity:0; transform:translateY(20px);}
to {opacity:1; transform:translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div style="text-align:center; animation: fadeIn 1s;">
<h1>💼 SalarySense AI</h1>
<h3>Premium Employee Salary Prediction Platform</h3>
<p>World Class Machine Learning Web App</p>
</div>
""", unsafe_allow_html=True)

st.markdown("Project Developed by updateabdullahi")

# ---------------- SIDEBAR ----------------
import os

if os.path.exists("EBT LOGO.png"):
    st.sidebar.image("https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Fwww.fao.org%2Fnigeria%2Ffao-in-nigeria%2Ffr%2F&ved=0CBYQjRxqFwoTCPC20tPvt5QDFQAAAAAdAAAAABAF&opi=89978449.png", use_container_width=True)
else:
    st.sidebar.markdown("## 💼 Salary Price Predictions Using  AI")
theme = st.sidebar.selectbox("Theme", ["Dark Mode", "Light Mode"])
st.sidebar.markdown("## Salary Estimation Using  AI")
st.sidebar.caption("Built with Python + Scikit Learn")

# ---------------- INPUTS ----------------
col1, col2 = st.columns(2)

with col1:
    experience = st.slider("Experience (Years)", 0, 20, 3)
    age = st.slider("Age", 18, 60, 25)
    skills = st.slider("Skills Count", 1, 20, 5)
    education = st.selectbox(
        "Education",
        ["ND", "HND", "Degree", "MSc", "PhD"]
    )

with col2:
    jobrole = st.selectbox(
        "Job Role",
        ["Intern", "Analyst", "Developer",
         "Engineer", "Manager", "Data Scientist"]
    )

    location = st.selectbox(
        "Location",
        ["Lagos", "Abuja", "Kano",
         "Kaduna", "Jigawa", "Remote"]
    )

    remote = st.selectbox("Remote Work", ["Yes", "No"])

# ---------------- PREDICT ----------------
if st.button("🚀 Predict Salary"):

    # create dataframe
    new_data = pd.DataFrame({
        "EXPERIENCE":[experience],
        "AGE":[age],
        "SKILLS":[skills],
        "EDUCATION":[education],
        "JOBROLE":[jobrole],
        "LOCATION":[location],
        "REMOTEWORK":[remote]
    })

    # encode
    new_data = pd.get_dummies(new_data)

    # match training columns
    new_data = new_data.reindex(
        columns=training_columns,
        fill_value=0
    )

    # predict
    prediction = model.predict(new_data)[0]

    # counter animation
    counter = st.empty()

    step = max(int(prediction / 40), 1)

    for i in range(0, int(prediction), step):
        counter.markdown(
            f"<h1 style='text-align:center;color:#22c55e;'>₦{i:,.0f}</h1>",
            unsafe_allow_html=True
        )
        time.sleep(0.02)

    # final card
    st.markdown(f"""
    <div style="
        background:rgba(255,255,255,0.10);
        padding:30px;
        border-radius:20px;
        text-align:center;
        animation: fadeIn 1s;
        box-shadow:0 0 20px rgba(0,255,0,0.30);
        margin-top:20px;
    ">
        <h2>💼 Estimated Monthly Salary</h2>
        <h1 style="color:#22c55e;">₦{prediction:,.0f}</h1>
        <p>AI Powered Salary Forecast</p>
    </div>
    """, unsafe_allow_html=True)

    # badge
    if prediction < 200000:
        st.warning("🟡 Entry Level Salary")
    elif prediction < 600000:
        st.info("🔵 Mid Level Salary")
    else:
        st.success("🟢 Senior Executive Salary")

    # ---------------- CHART 1 ----------------
    st.subheader("📈 Career Salary Growth")

    levels = ["Current", "Next Level", "Senior"]
    values = [prediction, prediction * 1.25, prediction * 1.60]

    fig, ax = plt.subplots(figsize=(8,4))
    ax.bar(levels, values)
    ax.set_title("Salary Growth Projection")
    ax.set_ylabel("₦ Salary")
    st.pyplot(fig)

    # ---------------- CHART 2 ----------------
    st.subheader("🥧 Salary Allocation Suggestion")

    labels = ["Expenses", "Savings", "Investment"]
    sizes = [50, 30, 20]

    fig2, ax2 = plt.subplots()
    ax2.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )
    ax2.axis("equal")
    st.pyplot(fig2)

# ---------------- FOOTER ----------------
st.markdown("Designed by UpdateCodesML")
st.caption("Built with Python • Streamlit • Machine Learning")