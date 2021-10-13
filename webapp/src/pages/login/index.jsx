import { Link } from 'react-router-dom';
import { Title } from '../../ui/components/atoms/title';
import { BasicTextField } from '../../ui/components/atoms/textfield/BasicTextField';
import { PasswordTextField } from '../../ui/components/atoms/textfield/PasswordTextField';
import { Button } from '../../ui/components/atoms/button';
import GlobalStyles from '@mui/material/GlobalStyles';
import bg from '../../assets/images/loginbackground.svg';

const inputGlobalStyles = (
  <GlobalStyles
    styles={{
      body: {
        background: `url(${bg}) no-repeat 50% 50%`,
        backgroundSize: 'cover',
        display: 'flex',
        flexDirection: 'column',
        width: '50%',
        margin: '0 auto',
      },
    }}
  />
);

export const Login = () => {
  return (
    <div>
      {inputGlobalStyles}
      <Title>Login</Title>
      <BasicTextField label="Email" />
      <PasswordTextField label="Password" />
      <Button>Login</Button>
      <Link to="/signup">Sign Up</Link>
    </div>
  );
};
