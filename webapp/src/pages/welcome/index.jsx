import { Box } from '@mui/system';
import { Link } from 'react-router-dom';
import { Typography } from '../../ui/components/atoms/typography';

export const Welcome = () => {
  return (
    <>
      <Typography variant="h3" component="h1">
        Welcome
      </Typography>
      <Box>
        <Link to="/login">Login</Link>
      </Box>
      <Box>
        <Link to="/signup">Sign up</Link>
      </Box>
    </>
  );
};
