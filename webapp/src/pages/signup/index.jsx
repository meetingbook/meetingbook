import { Link, useHistory } from 'react-router-dom';
import { Title } from '../../ui/components/atoms/title';
import { BasicTextField } from '../../ui/components/atoms/textfield/BasicTextField';
import { PasswordTextField } from '../../ui/components/atoms/textfield/PasswordTextField';
import { Button } from '../../ui/components/atoms/button';
import Box from '@mui/material/Box';
import Avatar from '@mui/material/Avatar';
import GlobalStyles from '@mui/material/GlobalStyles';
import { styled } from '@mui/system';
import bg from '../../assets/images/loginbackground.svg';
import { AdaptiveContainer } from '../../ui/components/atoms/templates';
import { request } from '../../infra/webservice';

const inputGlobalStyles = (
  <GlobalStyles
    styles={{
      body: {
        background: `url(${bg}) no-repeat 50% 50%`,
        backgroundSize: 'cover',
        width: '90%',
        margin: '0 auto',
      },
    }}
  />
);

const WhiteTitle = styled(Title)(({ theme }) => ({
  color: theme.palette.white.main,
  textAlign: 'center',
}));

const WhiteAvatar = styled(Avatar)(({ theme }) => ({
  color: theme.palette.white.main,
  background: theme.palette.primary.main,
  margin: '0 auto',
}));

export const SignUp = () => {
  const history = useHistory();

  const handleOnSubmit = (e) => {
    e.preventDefault();

    const body = {
      email: e.target[0].value,
      password: e.target[2].value,
    };

    request('/registration', 'POST', JSON.stringify(body))
      .then((res) => {
        if (res.status === 409) {
          alert('Please try another email');
          return;
        }

        history.push('/login');
      })
      .catch((e) => alert(e.message));
  };

  return (
    <AdaptiveContainer>
    <Box
      onSubmit={handleOnSubmit}
      component="form"
      sx={{
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-evenly',
        height: '60vh',
        marginTop: '7em',
      }}
    >
      {inputGlobalStyles}
      <WhiteAvatar>A</WhiteAvatar>
      <WhiteTitle>Registration</WhiteTitle>
      <Box>
        <BasicTextField
          type="email"
          requried="true"
          fullWidth={true}
          label="Email"
        />
      </Box>
      <Box>
        <PasswordTextField requried="true" label="Password" />
      </Box>
      <Box>
        <PasswordTextField requried="true" label=" Confirm Password" />
      </Box>
      <Box>
        <Button type="submit" fullWidth={true}>
          Sign Up
        </Button>
      </Box>
      <Box sx={{ textAlign: 'center' }}>
        <Link to="/login">Login</Link>
      </Box>
    </Box>
    </AdaptiveContainer>
  );
};
