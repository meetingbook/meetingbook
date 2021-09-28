import { Link } from "react-router-dom";
import { Typography } from "../../ui/components/atoms/typography";

export const SignUp = () => {
  return (
    <>
      <Typography variant="h3" component="h1">
        Sign Up
      </Typography>
      <Link to="/login">Login</Link>
    </>
  );
};
