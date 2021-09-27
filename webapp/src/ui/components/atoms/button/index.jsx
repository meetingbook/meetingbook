import { styled } from "@mui/material/styles";
import MUIButton from "@mui/material/Button";
import { purple } from "@mui/material/colors";

export const Button = styled(MUIButton)(({ theme }) => ({
  color: theme.palette.getContrastText(purple[500]),
  backgroundColor: purple[500],
  "&:hover": {
    backgroundColor: purple[700],
  },
}));
