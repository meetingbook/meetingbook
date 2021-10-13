import { Link } from 'react-router-dom';
import { Typography } from '../../ui/components/atoms/typography';
import { BasicTextField } from '../../ui/components/atoms/textfield/BasicTextField';
import { PasswordTextField } from '../../ui/components/atoms/textfield/PasswordTextField';

export const Login = () => {
  return (
    <>
      <Typography variant="h3" component="h1">
        Login
      </Typography>
      <BasicTextField></BasicTextField>
      <PasswordTextField></PasswordTextField>
      <Link to="/signup">Sign Up</Link>
    </>
  );
};
