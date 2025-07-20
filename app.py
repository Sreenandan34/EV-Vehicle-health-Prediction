import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("ev_health_model.pkl")

st.title("EV Two-Wheeler Health Prediction System")

# Input form
with st.form("input_form"):
    trip_distance_km = st.number_input("Trip Distance (km)", 0.0, 100.0, 10.0)
    trip_duration_minutes = st.number_input("Trip Duration (minutes)", 0.0, 360.0, 60.0)
    average_speed_kmph = st.slider("Average Speed (km/h)", 0, 100, 45)
    max_speed_kmph = st.slider("Max Speed (km/h)", 0, 100, 60)
    battery_discharge_percentage = st.slider("Battery Discharge (%)", 0, 100, 50)
    regenerative_braking_kwh = st.number_input("Regenerative Braking (kWh)", 0.0, 5.0, 1.0)
    rider_weight_kg = st.number_input("Rider Weight (kg)", 30.0, 150.0, 70.0)
    payload_weight_kg = st.number_input("Payload Weight (kg)", 0.0, 50.0, 10.0)
    number_of_hard_braking_events = st.slider("Hard Braking Events", 0, 50, 2)
    number_of_hard_acceleration_events = st.slider("Hard Acceleration Events", 0, 50, 2)
    average_battery_temperature_celsius = st.slider("Avg Battery Temp (°C)", 10, 60, 35)
    max_battery_temperature_celsius = st.slider("Max Battery Temp (°C)", 10, 70, 40)
    average_motor_temperature_celsius = st.slider("Avg Motor Temp (°C)", 20, 100, 60)
    max_motor_temperature_celsius = st.slider("Max Motor Temp (°C)", 20, 120, 70)
    average_suspension_activity_index = st.number_input("Suspension Index", 0, 5000, 200)
    total_pothole_count = st.slider("Total Potholes", 0, 100, 5)
    terrain_score = st.slider("Terrain Score (0–100)", 0, 100, 70)
    total_elevation_gain_meters = st.number_input("Elevation Gain (m)", 0, 2000, 100)
    braking_induced_speed_drops_per_km = st.slider("Braking Drops/km", 0, 10, 2)
    average_coefficient_of_friction_indicator = st.slider("Avg Friction Coefficient", 0.0, 1.0, 0.7)
    ambient_temperature_celsius = st.slider("Ambient Temperature (°C)", -10, 50, 30)
    average_humidity_percentage = st.slider("Average Humidity (%)", 0, 100, 50)
    precipitation = st.selectbox("Precipitation", ["Dry", "Rain"])
    precipitation_indicator = 0 if precipitation == "Dry" else 1

    submit = st.form_submit_button("Predict Health Score")

# Prepare input for model
if submit:
    input_dict = {
        'trip_distance_km': trip_distance_km,
        'trip_duration_minutes': trip_duration_minutes,
        'average_speed_kmph': average_speed_kmph,
        'max_speed_kmph': max_speed_kmph,
        'battery_discharge_percentage': battery_discharge_percentage,
        'regenerative_braking_kwh': regenerative_braking_kwh,
        'rider_weight_kg': rider_weight_kg,
        'payload_weight_kg': payload_weight_kg,
        'number_of_hard_braking_events': number_of_hard_braking_events,
        'number_of_hard_acceleration_events': number_of_hard_acceleration_events,
        'average_battery_temperature_celsius': average_battery_temperature_celsius,
        'max_battery_temperature_celsius': max_battery_temperature_celsius,
        'average_motor_temperature_celsius': average_motor_temperature_celsius,
        'max_motor_temperature_celsius': max_motor_temperature_celsius,
        'average_suspension_activity_index': average_suspension_activity_index,
        'total_pothole_count': total_pothole_count,
        'terrain_score': terrain_score,
        'total_elevation_gain_meters': total_elevation_gain_meters,
        'braking_induced_speed_drops_per_km': braking_induced_speed_drops_per_km,
        'average_coefficient_of_friction_indicator': average_coefficient_of_friction_indicator,
        'ambient_temperature_celsius': ambient_temperature_celsius,
        'average_humidity_percentage': average_humidity_percentage,
        'precipitation_indicator': precipitation_indicator
    }

    input_df = pd.DataFrame([input_dict])

    try:
        score = model.predict(input_df)[0]
        st.success(f"Predicted Health Score: {score:.2f}/100")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
