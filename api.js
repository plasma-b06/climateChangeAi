const API_URL = "http://localhost:5000";

export const fetchUsers = async () => {
  const res = await fetch(`${API_URL}/users`);
  return await res.json();
};

export const addUser = async (name) => {
  const res = await fetch(`${API_URL}/users`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name }),
  });
  return await res.json();
};
