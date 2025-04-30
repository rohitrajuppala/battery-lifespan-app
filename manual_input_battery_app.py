
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

st.set_page_config(page_title="Manual Battery Lifespan Predictor", layout="wide")
st.title("🔋 Battery Lifespan Prediction from Manual Inputs")

# User input
st.sidebar.header("Enter Battery Test Features")

ambient_temp = st.sidebar.number_input("Ambient Temperature (°C)", value=25.0)
avg_voltage = st.sidebar.number_input("Average Voltage Measured (V)", value=3.7)
avg_temperature = st.sidebar.number_input("Average Temperature Measured (°C)", value=30.0)
time_duration = st.sidebar.number_input("Test Time Duration (seconds)", value=3600.0)

# Simulated historical dataset (for model training)
st.subheader("📊 Simulated Historical Data (for training)")
np.random.seed(42)
sample_data = {
    "ambient_temp": np.random.normal(25, 2, 100),
    "avg_voltage": np.random.normal(3.7, 0.1, 100),
    "avg_temperature": np.random.normal(30, 3, 100),
    "time_duration": np.random.normal(3600, 300, 100),
    "capacity": np.random.normal(1.8, 0.1, 100)
}
df = pd.DataFrame(sample_data)
st.dataframe(df.head())

# Train a regression model
X = df[["avg_voltage", "avg_temperature", "time_duration"]]
y = df["capacity"]
model = LinearRegression()
model.fit(X, y)

# Prediction based on user input
user_input = pd.DataFrame([[avg_voltage, avg_temperature, time_duration]],
                          columns=["avg_voltage", "avg_temperature", "time_duration"])
predicted_capacity = model.predict(user_input)[0]

st.markdown("### 🔮 Predicted Battery Capacity")
st.metric("Estimated Capacity (Ah)", f"{predicted_capacity:.3f}")

# Optional visualization
st.subheader("📈 Data Relationships")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="avg_temperature", y="capacity", ax=ax)
plt.axvline(avg_temperature, color='red', linestyle='--', label='Your Input')
plt.legend()
st.pyplot(fig)
