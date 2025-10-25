import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from utils import encode_features

# Load and encode data
df = pd.read_csv("synthetic_climate_health_data.csv")
df, le_age, le_loc = encode_features(df)

features = ['temperature', 'humidity', 'rainfall', 'AQI', 'age_group', 'location']
le_risk = LabelEncoder()

def train_model(target, name):
    df[target] = le_risk.fit_transform(df[target])
    X, y = df[features], df[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeClassifier(max_depth=4)
    model.fit(X_train, y_train)
    print(f"\n{name} Report:\n", classification_report(y_test, model.predict(X_test)))
    joblib.dump(model, f"models/{name}.pkl")

train_model('heat_risk', 'heat_model')
train_model('dengue_risk', 'dengue_model')
train_model('asthma_risk', 'asthma_model')
