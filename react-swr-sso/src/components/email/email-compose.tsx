import React from "react";
import {
  Tabs,
  Tab,
  Box,
  Typography,
  Autocomplete,
  TextField,
  Chip,
} from "@mui/material";
import { EmailRecipients, EmailRecipientsType } from "./email-recipients";
import { EmailBasic } from "./email-basic";
import { EmailEditor } from "./email-editor";
import { EmailSendActions } from "./email-send-actions";

interface TabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

export type EmailComposeProps = {
  availableRecipients?: EmailRecipientsType;
  defaultFrom: string;
  availableFrom?: string[];
};

function CustomTabPanel(props: TabPanelProps) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

function a11yProps(index: number) {
  return {
    id: `simple-tab-${index}`,
    "aria-controls": `simple-tabpanel-${index}`,
  };
}

export function EmailCompose({
  availableRecipients,
  defaultFrom,
  availableFrom,
}: EmailComposeProps) {
  const [value, setValue] = React.useState(0);

  const handleChange = (event: React.SyntheticEvent, newValue: number) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ width: "100%" }}>
      <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
        <Tabs
          value={value}
          onChange={handleChange}
          aria-label="basic tabs example"
        >
          <Tab label="Basic" {...a11yProps(0)} />
          <Tab label="Templates" {...a11yProps(1)} />
          <Tab label="Item Three" {...a11yProps(2)} />
        </Tabs>
      </Box>
      <Box display="flex" flexDirection="column" gap={1}>
        <EmailRecipients availableRecipients={availableRecipients} />
        <Autocomplete
          id="tags-filled"
          options={availableFrom ?? []}
          defaultValue={defaultFrom}
          renderTags={(value: readonly string[], getTagProps) =>
            value.map((option: string, index: number) => (
              <Chip
                variant="outlined"
                label={option}
                {...getTagProps({ index })}
              />
            ))
          }
          size="small"
          readOnly={availableFrom === undefined || availableFrom.length <= 1}
          renderInput={(params) => <TextField {...params} label="From" />}
        />
        <TextField label="Subject" size="small" fullWidth />
      </Box>
      <CustomTabPanel value={value} index={0}>
        <EmailBasic />
      </CustomTabPanel>
      <CustomTabPanel value={value} index={1}>
        <EmailEditor />
      </CustomTabPanel>
      <Box>
        <EmailSendActions />
      </Box>
    </Box>
  );
}
