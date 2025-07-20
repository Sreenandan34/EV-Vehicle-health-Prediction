# Generating the complete and correct app.py content based on the feature order from the uploaded training script

# Define the complete and correct app.py code as a string
app_py_content = """
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="EV Health Score Predictor", layout="centered")

st.title("🔋 EV Two-Wheeler Health Prediction System")
st.markdown("Predict the post-trip health score of an electric two-wheeler using real-world trip data.")

# Load model
model = joblib.load("ev_health_model.pkl")

# Feature input UI
st.subheader("Enter Trip and Environmental Details")

trip_distance_km = st.number_input("Trip Distance (km)", 0.0, 200.0, 10.0)
trip_duration_minutes = st.number_input("Trip Duration (minutes)", 0.0, 500.0, 30.0)
average_speed_kmph = st.slider("Average Speed (kmph)", 0, 100, 45)
max_speed_kmph = st.slider("Max Speed (kmph)", 0, 120, 70)
battery_discharge_percentage = st.slider("Battery Discharge (%)", 0, 100, 50)
regenerative_braking_kwh = st.number_input("Regenerative Braking (kWh)", 0.0, 5.0, 1.0)
rider_weight_kg = st.number_input("Rider Weight (kg)", 40.0, 150.0, 70.0)
payload_weight_kg = st.number_input("Payload Weight (kg)", 0.0, 50.0, 10.0)
average_motor_temperature_celsius = st.slider("Avg. Motor Temp (°C)", 20, 100, 60)
max_motor_temperature_celsius = st.slider("Max Motor Temp (°C)", 20, 120, 70)
average_battery_temperature_celsius = st.slider("Avg. Battery Temp (°C)", 10, 60, 35)
max_battery_temperature_celsius = st.slider("Max Battery Temp (°C)", 10, 70, 40)
terrain_score = st.slider("Terrain Score (0-100)", 0, 100, 80)
average_suspension_activity_index = st.number_input("Suspension Activity Index", 0, 5000, 180)
total_elevation_gain_meters = st.number_input("Total Elevation Gain (m)", 0.0, 1000.0, 100.0)
total_pothole_count = st.number_input("Pothole Count", 0, 100, 10)
average_coefficient_of_friction_indicator = st.number_input("Avg. Coefficient of Friction", 0.0, 1.0, 0.75)
braking_induced_speed_drops_per_km = st.number_input("Braking-Induced Speed Drops/km", 0.0, 10.0, 1.0)
number_of_hard_braking_events = st.number_input("Hard Braking Events", 0, 50, 2)
number_of_hard_acceleration_events = st.number_input("Hard Acceleration Events", 0, 50, 2)
ambient_temperature_celsius = st.slider("Ambient Temperature (°C)", -10, 50, 30)
precipitation = st.selectbox("Precipitation", ["Dry", "Rain"])
precipitation_indicator = 0 if precipitation == "Dry" else 1
average_humidity_percentage = st.slider("Average Humidity (%)", 0, 100, 50)

# Create input DataFrame with correct order
input_data = pd.DataFrame([{
    "trip_distance_km": trip_distance_km,
    "trip_duration_minutes": trip_duration_minutes,
    "average_speed_kmph": average_speed_kmph,
    "max_speed_kmph": max_speed_kmph,
    "battery_discharge_percentage": battery_discharge_percentage,
    "regenerative_braking_kwh": regenerative_braking_kwh,
    "rider_weight_kg": rider_weight_kg,
    "payload_weight_kg": payload_weight_kg,
    "average_motor_temperature_celsius": average_motor_temperature_celsius,
    "max_motor_temperature_celsius": max_motor_temperature_celsius,
    "average_battery_temperature_celsius": average_battery_temperature_celsius,
    "max_battery_temperature_celsius": max_battery_temperature_celsius,
    "terrain_score": terrain_score,
    "average_suspension_activity_index": average_suspension_activity_index,
    "total_elevation_gain_meters": total_elevation_gain_meters,
    "total_pothole_count": total_pothole_count,
    "average_coefficient_of_friction_indicator": average_coefficient_of_friction_indicator,
    "braking_induced_speed_drops_per_km": braking_induced_speed_drops_per_km,
    "number_of_hard_braking_events": number_of_hard_braking_events,
    "number_of_hard_acceleration_events": number_of_hard_acceleration_events,
    "ambient_temperature_celsius": ambient_temperature_celsius,
    "precipitation_indicator": precipitation_indicator,
    "average_humidity_percentage": average_humidity_percentage
}])

# Predict and display result
if st.button("🚀 Predict Health Score"):
    score = model.predict(input_data)[0]
    st.success(f"Predicted Health Score: {score:.2f} / 100")
"""

# Save the app.py file for user to download or view
with open("/mnt/data/app.py", "w") as f:
    f.write(app_py_content)

"/mnt/data/app.py"
