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

export type EmailRecipientType = {
  type: "individual" | "group";
  name: string;
  email?: string;
};

export type EmailRecipientsType = Array<EmailRecipientType>;

export type EmailRecipientFieldProps = {
  availableRecipients?: EmailRecipientsType;
  label: "To" | "Cc" | "Bcc";
};

export type EmailRecipientsProps = {
  availableRecipients?: EmailRecipientsType;
};

const displayRecipient = (r: EmailRecipientType) => {
  if (r.type === "individual") {
    return `${r.name} <${r.email}>`;
  } else {
    return `${r.name}`;
  }
};

export function EmailRecipientField({
  availableRecipients,
  label,
}: EmailRecipientFieldProps) {
  const recipientList = availableRecipients ?? [];

  return (
    <Autocomplete
      multiple
      id="tags-filled"
      options={recipientList.map((option) => JSON.stringify(option))}
      defaultValue={[]}
      freeSolo
      renderTags={(value: readonly string[], getTagProps) =>
        value.map((option: string, index: number) => (
          <Chip
            variant="outlined"
            label={displayRecipient(JSON.parse(option))}
            {...getTagProps({ index })}
          />
        ))
      }
      size="small"
      renderInput={(params) => (
        <TextField required={label === "To"} {...params} label={label} />
      )}
    />
  );
}

export function EmailRecipients({ availableRecipients }: EmailRecipientsProps) {
  return (
    <>
      <EmailRecipientField
        availableRecipients={availableRecipients}
        label="To"
      />
      <EmailRecipientField
        availableRecipients={availableRecipients}
        label="Cc"
      />
      <EmailRecipientField
        availableRecipients={availableRecipients}
        label="Bcc"
      />
    </>
  );
}
