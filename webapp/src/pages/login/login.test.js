import { render, screen } from "@testing-library/react";
import { BrowserRouter as Router } from "react-router-dom";

import { Login } from ".";

test("should render <Login> page", () => {
  render(
    <Router>
      <Login />
    </Router>
  );
  const linkElement = screen.getByText(/Login/i);
  expect(linkElement).toBeInTheDocument();
});
