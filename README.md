# EV Two-Wheeler Health Prediction System

This project is a machine learning–based system designed to estimate the health of electric two-wheelers after each trip using real-world driving data. Built during my internship at **Revelec AutomotiEV**, it enables predictive maintenance by analyzing how various trip and rider conditions affect vehicle wear.

## 📌 Objective

Traditional maintenance is often reactive—problems are identified only after failure. This system aims to flip that approach by using **trip-level sensor data** to monitor degradation in real time and **predict vehicle health scores (0–100)** dynamically.

## 🔍 Key Features

- Predicts vehicle health immediately after each trip
- Uses 24 input features across categories:
  - **Battery**: Discharge %, temperature readings, regen braking
  - **Motor**: Avg. and peak temperatures
  - **Trip Summary**: Speed, time, distance
  - **Road & Terrain**: Elevation, potholes, suspension, road friction
  - **Driver Behavior**: Braking and acceleration events
  - **Environment**: Humidity, temperature, weather condition
- Triggers maintenance suggestions based on health score category (Excellent, Good, Degraded, Poor, Very Poor)

## ⚙️ How It Works

The model is trained using a **Random Forest Regressor**, which learns patterns from historical/simulated data and predicts post-trip vehicle health. The score is based on how much stress or damage the trip may have caused, derived from real-world parameters.

A hand-crafted formula is also used to validate and interpret predictions based on known EV behavior from research and lab tests.

## 📈 Model Performance

- **R² Score:** 96%
- **MAE:** 1.8
- Consistently produces reliable health scores across a wide range of trip conditions (from smooth urban rides to rough terrain).

## 🛠 Tech Stack

- **Language:** Python  
- **Libraries:** Scikit-learn, Pandas, NumPy  
- **Platform:** Google Colab  
- **Data Simulation:** Excel (for synthetic trip data)



## 💡 Problem Solved

This system helps EV startups and fleet operators:
- Predict wear and tear in advance
- Avoid sudden breakdowns
- Extend vehicle life
- Make smarter, data-backed maintenance decisions

## ✅ Usage

You can run the project by uploading the dataset and executing the model notebook or script. It will ask for input values or take them from the sheet and return the predicted health score along with insights if the vehicle condition is degraded.

🚀 [Live Demo on Streamlit](https://ev-vehicle-health-prediction-fyrou78hmu2jakupvv5gbs.streamlit.app)





