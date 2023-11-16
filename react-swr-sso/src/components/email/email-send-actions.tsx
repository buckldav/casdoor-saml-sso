import React from "react";
import { Box, Button, Modal, Typography } from "@mui/material";
import { DateTimePicker } from "@mui/x-date-pickers/DateTimePicker";
import dayjs, { Dayjs } from "dayjs";

export type EmailSendActionsProps = {};
const style = {
  position: "absolute" as "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: 400,
  bgcolor: "background.paper",
  border: "2px solid #000",
  boxShadow: 24,
  p: 4,
};

export default function ScheduleSend() {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return (
    <div>
      <Button onClick={handleOpen} variant="outlined">
        Schedule Send
      </Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-schedule-send-title"
        aria-describedby="modal-schedule-send-description"
      >
        <Box sx={style}>
          <Typography
            id="modal-schedule-send-title"
            variant="h6"
            component="h2"
          >
            Schedule Send
          </Typography>
          <Typography id="modal-schedule-send-description" sx={{ mt: 2 }}>
            Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
          </Typography>
          <DateTimePicker
            defaultValue={dayjs(
              new Date(new Date().getTime() + 24 * 60 * 60 * 1000).toISOString()
            )}
          />
          <Box display="flex" gap={1}>
            <Button onClick={handleClose}>Cancel</Button>
            <Button variant="contained">Schedule Send</Button>
          </Box>
        </Box>
      </Modal>
    </div>
  );
}

export function EmailSendActions({}: EmailSendActionsProps) {
  return (
    <Box display="flex" gap={1}>
      <Button variant="outlined">Send Now</Button>
      <ScheduleSend />
    </Box>
  );
}
