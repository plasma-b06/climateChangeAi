import React, { useEffect, useState } from "react";
import { View, Text, Button, TextInput } from "react-native";

export default function App() {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");

  const API_URL = "http://localhost:5000/users";

  // Fetch users from Flask
  const fetchUsers = async () => {
    const response = await fetch(API_URL);
    const data = await response.json();
    setUsers(data);
  };

  // Add a new user
  const addUser = async () => {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name }),
    });
    const newUser = await response.json();
    setUsers([...users, newUser]);
    setName("");
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <View style={{ padding: 20 }}>
      {users.map((user) => (
        <Text key={user.id}>{user.name}</Text>
      ))}
      <TextInput
        placeholder="Enter name"
        value={name}
        onChangeText={setName}
        style={{ borderWidth: 1, marginVertical: 10, padding: 5 }}
      />
      <Button title="Add User" onPress={addUser} />
    </View>
  );
}
