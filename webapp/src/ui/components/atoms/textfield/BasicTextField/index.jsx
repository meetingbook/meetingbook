import TextField from '@mui/material/TextField';

export const BasicTextField = (props) => (
  <TextField
    InputLabelProps={{ required: false }}
    {...props}
    variant="outlined"
  />
);
