import { Box } from '@mui/system';
import { Title } from '../../ui/components/atoms/title';
import { styled } from '@mui/system';
import { Button } from '../../ui/components/atoms/button';
import GlobalStyles from '@mui/material/GlobalStyles';
import blob from '../../assets/images/pinkblob_for_welcom.svg';

const inputGlobalStyles = (
  <GlobalStyles
    styles={{
      body: {
        background: `url(${blob}) no-repeat 50% 50%`,
        backgroundSize: 'cover',
        width: '50%',
        margin: '0 auto',
      },
    }}
  />
);

export const Welcome = () => {
  return (
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
      <Title>Welcome</Title>
      <Box>
        <Button fullWidth={true} href="/login">
          Login
        </Button>
      </Box>
      <Box>
        <Button fullWidth={true} href="/signup">
          Sign up
        </Button>
      </Box>
    </Box>
  );
};
