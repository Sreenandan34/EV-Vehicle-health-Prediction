import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("ev_health_model.pkl")

st.title("EV Two-Wheeler Health Prediction System")

# Inputs
battery_discharge = st.slider("Battery Discharge (%)", 0, 100, 50)
regen_braking = st.number_input("Regenerative Braking (kWh)", 0.0, 10.0, 1.0)
avg_batt_temp = st.slider("Average Battery Temp (°C)", 10, 60, 35)
max_batt_temp = st.slider("Max Battery Temp (°C)", 10, 70, 40)
avg_motor_temp = st.slider("Average Motor Temp (°C)", 20, 100, 60)
max_motor_temp = st.slider("Max Motor Temp (°C)", 20, 120, 70)
trip_distance = st.slider("Trip Distance (km)", 0, 100, 10)
trip_duration = st.slider("Trip Duration (minutes)", 0, 360, 30)
avg_speed = st.slider("Average Speed (kmph)", 0, 100, 40)
max_speed = st.slider("Max Speed (kmph)", 0, 120, 60)
hard_brakes = st.slider("Hard Braking Events", 0, 50, 2)
hard_accel = st.slider("Hard Acceleration Events", 0, 50, 2)
suspension_index = st.slider("Suspension Activity Index", 0, 5000, 200)
potholes = st.slider("Total Pothole Count", 0, 100, 5)
terrain_score = st.slider("Terrain Score", 0, 100, 75)
elevation_gain = st.slider("Total Elevation Gain (meters)", 0, 1000, 100)
rider_weight = st.slider("Rider Weight (kg)", 40, 150, 70)
payload_weight = st.slider("Payload Weight (kg)", 0, 50, 10)
friction_indicator = st.slider("Avg Coefficient of Friction", 0.0, 1.0, 0.7)
brake_speed_drops = st.slider("Braking-Induced Speed Drops/km", 0.0, 10.0, 3.0)
ambient_temp = st.slider("Ambient Temperature (°C)", -10, 50, 30)
precipitation = st.selectbox("Precipitation", ["Dry", "Rain"])
precipitation_val = 0 if precipitation == "Dry" else 1
humidity = st.slider("Humidity (%)", 0, 100, 50)

# Create DataFrame in correct order
input_df = pd.DataFrame([{
    "battery_discharge_percentage": battery_discharge,
    "regenerative_braking_kwh": regen_braking,
    "average_battery_temperature_celsius": avg_batt_temp,
    "max_battery_temperature_celsius": max_batt_temp,
    "average_motor_temperature_celsius": avg_motor_temp,
    "max_motor_temperature_celsius": max_motor_temp,
    "trip_distance_km": trip_distance,
    "trip_duration_minutes": trip_duration,
    "average_speed_kmph": avg_speed,
    "max_speed_kmph": max_speed,
    "number_of_hard_braking_events": hard_brakes,
    "number_of_hard_acceleration_events": hard_accel,
    "average_suspension_activity_index": suspension_index,
    "total_pothole_count": potholes,
    "terrain_score": terrain_score,
    "total_elevation_gain_meters": elevation_gain,
    "rider_weight_kg": rider_weight,
    "payload_weight_kg": payload_weight,
    "average_coefficient_of_friction_indicator": friction_indicator,
    "braking_induced_speed_drops_per_km": brake_speed_drops,
    "ambient_temperature_celsius": ambient_temp,
    "precipitation_indicator": precipitation_val,
    "average_humidity_percentage": humidity
}])

# Prediction
if st.button("Predict Health Score"):
    try:
        score = model.predict(input_df)[0]
        st.success(f"Predicted Health Score: {score:.2f} / 100")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
