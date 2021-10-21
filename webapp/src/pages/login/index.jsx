import { Link } from 'react-router-dom';
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
  return (
    <AdaptiveContainer>
      <Box
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
          <BasicTextField fullWidth={true} label="Email" />
        </Box>
        <Box>
          <PasswordTextField label="Password" />
        </Box>
        <Box>
          <Button fullWidth={true}>Login</Button>
        </Box>
        <Box sx={{ textAlign: 'center' }}>
          <Link to="/signup">Sign Up</Link>
        </Box>
      </Box>
    </AdaptiveContainer>
  );
};
