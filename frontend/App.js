import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet, ActivityIndicator } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient'; // For enhanced UI in Expo

const App = () => {
  const [features, setFeatures] = useState(['', '', '', '']);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handlePredict = async () => {
    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          features: features.map(f => parseFloat(f) || 0),
        }),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      // Handle streaming response
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let result = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        result += decoder.decode(value);
        const lines = result.split('\n');
        result = lines.pop(); // Keep incomplete line
        for (const line of lines) {
          if (line) {
            const data = JSON.parse(line);
            if (data.status === 'complete') {
              setPrediction(data.prediction);
            }
          }
        }
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <LinearGradient colors={['#4c669f', '#3b5998', '#192f6a']} style={styles.container}>
      <Text style={styles.title}>ML Model Predictor</Text>
      {features.map((value, index) => (
        <TextInput
          key={index}
          style={styles.input}
          placeholder={`Feature ${index + 1}`}
          placeholderTextColor="#aaa"
          keyboardType="numeric"
          value={value}
          onChangeText={text => {
            const newFeatures = [...features];
            newFeatures[index] = text;
            setFeatures(newFeatures);
          }}
        />
      ))}
      <Button title="Predict" onPress={handlePredict} disabled={loading} color="#007AFF" />
      {loading && <ActivityIndicator size="large" color="#ffffff" />}
      {error && <Text style={styles.error}>Error: {error}</Text>}
      {prediction !== null && (
        <Text style={styles.result}>Prediction: {prediction}</Text>
      )}
    </LinearGradient>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, justifyContent: 'center' },
  title: { fontSize: 24, fontWeight: 'bold', color: '#ffffff', marginBottom: 20, textAlign: 'center' },
  input: {
    borderWidth: 1,
    borderColor: '#ffffff',
    padding: 10,
    marginBottom: 10,
    borderRadius: 5,
    color: '#ffffff',
    backgroundColor: 'rgba(255,255,255,0.1)',
  },
  error: { color: '#ff4444', marginTop: 10, textAlign: 'center' },
  result: { fontSize: 18, color: '#ffffff', marginTop: 20, textAlign: 'center' },
});

export default App;
