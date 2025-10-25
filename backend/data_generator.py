# Generates realistic climate-health data
import pandas as pd, numpy as np, random

np.random.seed(42)
data = []

for _ in range(1000):
    temp = np.random.normal(35, 5)
    humidity = np.random.normal(70, 15)
    rainfall = np.random.exponential(30)
    AQI = np.random.normal(120, 40)
    age = random.choice(['Child', 'Adult', 'Elderly'])
    loc = random.choice(['Urban', 'Slum', 'Rural'])

    heat = 'High' if temp > 38 and humidity > 60 else 'Moderate' if temp > 35 else 'Low'
    dengue = 'High' if rainfall > 50 and humidity > 75 else 'Moderate' if rainfall > 30 else 'Low'
    asthma = 'High' if AQI > 150 else 'Moderate' if AQI > 100 else 'Low'

    data.append([temp, humidity, rainfall, AQI, age, loc, heat, dengue, asthma])

df = pd.DataFrame(data, columns=[
    'temperature', 'humidity', 'rainfall', 'AQI',
    'age_group', 'location',
    'heat_risk', 'dengue_risk', 'asthma_risk'
])
df.to_csv("synthetic_climate_health_data.csv", index=False)
