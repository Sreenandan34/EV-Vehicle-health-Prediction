import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("ev_health_model.pkl")  # Make sure this file is in the same directory

st.title("EV Two-Wheeler Health Prediction System")

# User inputs (must match model training feature names exactly and in same order)
battery_discharge = st.slider("Battery Discharge (%)", 0, 100, 50)
regen_braking = st.number_input("Regenerative Braking (kWh)", 0.0, 5.0, 1.0)
avg_batt_temp = st.slider("Average Battery Temp (°C)", 10, 60, 35)
max_batt_temp = st.slider("Max Battery Temp (°C)", 10, 70, 40)
avg_motor_temp = st.slider("Average Motor Temp (°C)", 20, 100, 60)
max_motor_temp = st.slider("Max Motor Temp (°C)", 20, 120, 70)
terrain_score = st.slider("Terrain Score (0-100)", 0, 100, 80)
hard_brakes = st.number_input("Hard Braking Events", 0, 50, 2)
suspension = st.number_input("Suspension Activity Index", 0, 5000, 180)
humidity = st.slider("Humidity (%)", 0, 100, 50)
ambient_temp = st.slider("Ambient Temperature (°C)", -10, 50, 30)
precipitation = st.selectbox("Precipitation", ["Dry", "Rain"])
precipitation_val = 0 if precipitation == "Dry" else 1

# Prepare the input DataFrame in the EXACT order as used during training
input_data = pd.DataFrame([{
    "battery_discharge_percentage": battery_discharge,
    "regenerative_braking_kwh": regen_braking,
    "average_battery_temperature_celsius": avg_batt_temp,
    "max_battery_temperature_celsius": max_batt_temp,
    "average_motor_temperature_celsius": avg_motor_temp,
    "max_motor_temperature_celsius": max_motor_temp,
    "terrain_score": terrain_score,
    "number_of_hard_braking_events": hard_brakes,
    "average_suspension_activity_index": suspension,
    "average_humidity_percentage": humidity,
    "ambient_temperature_celsius": ambient_temp,
    "precipitation_indicator": precipitation_val
}])

# Predict and show result
if st.button("Predict Health Score"):
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Health Score: {prediction:.2f}/100")
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
