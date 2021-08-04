export const createLi = (text) => {
  const li = document.createElement("li");
  li.innerHTML = text;
  return li;
};

export const addBooking = (booking) => {
  document
    .querySelector("ul")
    .appendChild(createLi(`${booking.id} – ${booking.name}`));
};
