import * as React from "react";
import { TextField } from "@mui/material";

export type EmailBasicProps = {};

export function EmailBasic({}: EmailBasicProps) {
  return <TextField size="small" multiline rows={4} />;
}
