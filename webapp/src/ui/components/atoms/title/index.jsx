import { Typography } from '../typography';

export const Title = (props) => (
  <Typography
    {...props}
    variant="h3"
    component="h1"
    sx={{ ...props.sx, fontWeight: 700 }}
  />
);
