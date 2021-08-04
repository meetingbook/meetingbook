const BASE_URL = "http://localhost:5000/api";

export const getBookings = async () => {
  const response = await fetch(`${BASE_URL}/bookings`);
  return await response.json();
};
