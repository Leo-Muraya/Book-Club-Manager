const API_URL = "http://127.0.0.1:5000";

export const fetchClubs = async () => {
  const response = await fetch(`${API_URL}/clubs`);
  return response.json();
};

export const fetchClubDetails = async (id) => {
  const response = await fetch(`${API_URL}/clubs/${id}`);
  return response.json();
};
