from flask import Flask, request, jsonify, Response
import numpy as np
import pickle
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for React Native frontend

# Load the pre-trained ML model
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    print("Model file not found. Please ensure model.pkl exists.")
    exit(1)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from React Native frontend
        data = request.get_json()
        if not data or 'features' not in data:
            return jsonify({'error': 'No features provided'}), 400

        # Extract features
        features = np.array(data['features']).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features).tolist()

        # Stream response
        def generate():
            yield json.dumps({'status': 'processing', 'progress': 50}) + '\n'
            yield json.dumps({'status': 'complete', 'prediction': prediction[0]}) + '\n'

        return Response(generate(), mimetype='application/json')

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
