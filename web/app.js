import { addBooking } from "./js/ui.js";
import { getBookings } from "./js/api.js";

const result = await getBookings();
result.bookings.forEach((booking) => {
  addBooking(booking);
});
