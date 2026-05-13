import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="SalarySense AI",
    page_icon="💼",
    layout="wide"
)

# Load model
model = joblib.load("salary_model.pkl")
training_columns = joblib.load("training_columns.pkl")

# CSS
st.markdown("""
<style>
.stApp {
background: linear-gradient(135deg,#0f172a,#1e293b,#111827);
color:white;
}
h1,h2,h3,p,label {
color:white !important;
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
.block-container {
padding-top:2rem;
}
[data-testid="stMetricValue"] {
color:#22c55e;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("💼 Simple Smart Salary Estimator Machine")
st.subheader("World Class Employee Salary Prediction Platform")

st.markdown("---")

# Inputs
col1, col2 = st.columns(2)

with col1:
    experience = st.slider("Experience (Years)",0,20,3)
    age = st.slider("Age",18,60,25)
    skills = st.slider("Skills Count",1,20,5)
    education = st.selectbox("Education",["ND","HND","Degree","MSc","PhD"])

with col2:
    jobrole = st.selectbox("Job Role",["Intern","Analyst","Developer","Engineer","Manager","Data Scientist"])
    location = st.selectbox("Location",["Lagos","Abuja","Kano","Kaduna","Jigawa","Remote"])
    remote = st.selectbox("Remote Work",["Yes","No"])

st.markdown("")

if st.button("🚀 Predict Salary"):

    new_data = pd.DataFrame({
        "EXPERIENCE":[experience],
        "AGE":[age],
        "SKILLS":[skills],
        "EDUCATION":[education],
        "JOBROLE":[jobrole],
        "LOCATION":[location],
        "REMOTEWORK":[remote]
    })

    new_data = pd.get_dummies(new_data)
    new_data = new_data.reindex(columns=training_columns, fill_value=0)

    prediction = model.predict(new_data)[0]

    st.markdown("## 📊 Prediction Result")
    st.success(f"Estimated Monthly Salary: ₦{prediction:,.0f}")

    if prediction < 200000:
        st.info("Entry-Level Salary Range")
    elif prediction < 600000:
        st.info("Mid-Level Salary Range")
    else:
        st.info("Senior / High Income Salary Range")

st.markdown("---")
st.caption("Built with AI • Machine Learning • Streamlit")