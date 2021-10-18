import { Box } from '@mui/system';
import { Title } from '../../ui/components/atoms/title';
import { styled } from '@mui/system';
import { Button } from '../../ui/components/atoms/button';
import GlobalStyles from '@mui/material/GlobalStyles';
import blob from '../../assets/images/pinkblob_for_welcom.svg';
import girl from '../../assets/images/undraw_Online_calendar.svg';
import { Paragraph } from '../../ui/components/atoms/paragraph';

const inputGlobalStyles = (
  <GlobalStyles
    styles={{
      body: {
        background: `url(${blob}) no-repeat 50% 50%`,
        backgroundSize: '100%',
        width: '50%',
        margin: '0 auto',
      },
    }}
  />
);

const WhiteTitle = styled(Title)(({ theme }) => ({
  color: theme.palette.white.main,
  textAlign: 'center',
}));

export const Welcome = () => {
  return (
    <Box>
      <img src={girl} />
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-evenly',
          height: '50vh',
          marginTop: '2em',
        }}
      >
        {inputGlobalStyles}

        <WhiteTitle>Welcome</WhiteTitle>
        <Paragraph sx={{ textAlign: 'center' }}>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </Paragraph>
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
    </Box>
  );
};
