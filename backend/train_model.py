from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle

# Generate sample data (replace with your dataset)
X = np.random.rand(100, 4)  # 100 samples, 4 features
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Simple binary classification

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
print("Model trained and saved as model.pkl")
