import streamlit as st
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Loading the model we created 
model = joblib.load('best_heart_disease_model.pkl')

#Scaler
scale = StandardScaler()

# Title and description
st.title("Predictor for heart disease")
st.write("Enter the patient's details to predict how likely they have heart disease.")

# Collect user input
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
cp = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3], format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"][x])
trestbps = st.number_input("Resting Blood Pressure", min_value=50, max_value=200, value=120)
chol = st.number_input("Serum Cholestoral", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "True" if x == 1 else "False")
restecg = st.selectbox("Resting ECG", options=[0, 1, 2], format_func=lambda x: ["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"][x])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=[0, 1, 2], format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x])
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", options=[0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia", options=[0, 1, 2], format_func=lambda x: ["Normal", "Fixed Defect", "Reversible Defect"][x])

# Prepare the input data
input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

# Scale the input data
input_data[:, [0, 3, 4, 7, 9]] = scale.fit_transform(input_data[:, [0, 3, 4, 7, 9]])

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    prediction_prob = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error(f"The patient is likely to have heart disease. Probability: {prediction_prob[0][1]:.2f}")
    else:
        st.success(f"The patient is unlikely to have heart disease. Probability: {prediction_prob[0][0]:.2f}")

