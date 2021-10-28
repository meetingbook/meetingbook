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
import { request, toBase64, createAuthHeader } from '../../infra/webservice';
import { saveCredentials } from '../../infra/storage';

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

export const Login = () => {
  const history = useHistory();
  const handleOnSubmit = (e) => {
    e.preventDefault();
    const email = e.target[0].value;
    const password = e.target[2].value;
    const credentials = toBase64(email, password);

    request({
      path: '/login',
      method: 'GET',
      headers: createAuthHeader(credentials),
    })
      .then((res) => {
        if (res.status === 401) {
          alert('Try another email or password');
          return;
        }
        saveCredentials(credentials), history.push('/calendar');
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
          height: '50vh',
          marginTop: '7em',
        }}
      >
        {inputGlobalStyles}
        <WhiteAvatar>A</WhiteAvatar>
        <WhiteTitle>Login</WhiteTitle>
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
          <Button type="submit" fullWidth={true}>
            Login
          </Button>
        </Box>
        <Box sx={{ textAlign: 'center' }}>
          <Link to="/signup">Sign Up</Link>
        </Box>
      </Box>
    </AdaptiveContainer>
  );
};
