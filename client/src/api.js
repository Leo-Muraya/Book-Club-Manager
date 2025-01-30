const API_URL = "http://localhost:5000";

export async function fetchClubs() {
  const response = await fetch(`${API_URL}/clubs`);
  return response.json();
}

export async function loginUser(credentials) {
  const response = await fetch(`${API_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials),
  });
  return response.json();
}

export async function registerUser(credentials) {
  const response = await fetch(`${API_URL}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials),
  });
  return response.json();
}

export async function fetchClubDetails(id) {
  const response = await fetch(`${API_URL}/clubs/${id}`);
  return response.json();
}