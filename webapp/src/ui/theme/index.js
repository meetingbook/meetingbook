import { createTheme } from '@mui/material/styles';

export const theme = createTheme({
  palette: {
    primary: {
      main: '#d55a5a',
    },
    white: {
      main: '#fff',
    },
  },
  typography: {
    fontFamily: 'Rubik, sans-serif',
  },
  components: {
    // Name of the component
    MuiButton: {
      styleOverrides: {
        // Name of the slot
        root: {},
      },
    },
  },
});
