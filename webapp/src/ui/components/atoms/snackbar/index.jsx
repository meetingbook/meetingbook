import React from 'react';
import MuiAlert from '@mui/material/Alert';
import MUISnackbar from '@mui/material/Snackbar';

const Alert = React.forwardRef(function Alert(props, ref) {
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

// open, message, severity
export const Snackbar = (props) => {
  return (
    <MUISnackbar
      open={props.open}
      autoHideDuration={6000}
      anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
    >
      <Alert severity={props.severity} sx={{ width: '100%' }}>
        {props.message}
      </Alert>
    </MUISnackbar>
  );
};
