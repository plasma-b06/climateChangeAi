from sklearn.preprocessing import LabelEncoder

def encode_features(df):
    le_age = LabelEncoder()
    le_loc = LabelEncoder()

    df['age_group'] = le_age.fit_transform(df['age_group'])  # Child=0, Adult=1, Elderly=2
    df['location'] = le_loc.fit_transform(df['location'])    # Urban=0, Slum=1, Rural=2

    return df, le_age, le_loc

def label_heat_risk(temp, humidity):
    if temp > 38 and humidity > 60:
        return "High"
    elif temp > 35:
        return "Moderate"
    else:
        return "Low"

def label_dengue_risk(rainfall, humidity):
    if rainfall > 50 and humidity > 75:
        return "High"
    elif rainfall > 30:
        return "Moderate"
    else:
        return "Low"

def label_asthma_risk(aqi):
    if aqi > 150:
        return "High"
    elif aqi > 100:
        return "Moderate"
    else:
        return "Low"

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def validate_input(data):
    assert 0 <= data['humidity'] <= 100, "Humidity must be between 0 and 100"
    assert 0 <= data['AQI'] <= 500, "AQI must be between 0 and 500"
    # Add more checks as needed

def decode_risk_label(label):
    mapping = {0: "Low", 1: "Moderate", 2: "High"}
    return mapping.get(label, "Unknown")
