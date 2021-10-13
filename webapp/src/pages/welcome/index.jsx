import { Box } from '@mui/system';
import { Link } from 'react-router-dom';
import { Title } from '../../ui/components/atoms/title';

export const Welcome = () => {
  return (
    <>
      <Title>Welcome</Title>
      <Box>
        <Link to="/login">Login</Link>
      </Box>
      <Box>
        <Link to="/signup">Sign up</Link>
      </Box>
    </>
  );
};
