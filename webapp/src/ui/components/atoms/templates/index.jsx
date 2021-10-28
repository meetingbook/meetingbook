import Grid from '@mui/material/Grid';

export const AdaptiveContainer = (props) => (
  <Grid container sx={{ justifyContent: 'center' }}>
    <Grid item xs={12} sm={10} md={8} lg={6} xl={6}>
      {props.children}
    </Grid>
  </Grid>
);
