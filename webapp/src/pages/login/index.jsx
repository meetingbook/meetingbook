import { Link } from 'react-router-dom';
import { Typography } from '../../ui/components/atoms/typography';

export const Login = () => {
  return (
    <>
      <Typography variant="h3" component="h1">
        Login
      </Typography>
      <Link to="/signup">Sign Up</Link>
    </>
  );
};
