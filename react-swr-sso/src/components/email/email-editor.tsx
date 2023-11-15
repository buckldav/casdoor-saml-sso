import React from "react";
import { Button, Box, Typography } from "@mui/material";
import * as REE from "react-email-editor";

export type EmailEditorProps = {
  initialDesign?: any;
};

export function EmailEditor({ initialDesign }: EmailEditorProps) {
  const [emailHtml, setEmailHtml] = React.useState("");
  const [emailText, setEmailText] = React.useState("");
  const [emailDesign, setEmailDesign] = React.useState("");
  const emailEditorRef = React.useRef<REE.EditorRef>(null);

  const saveDesign = () => {
    const unlayer = emailEditorRef.current?.editor;

    unlayer?.saveDesign((design: any) => {
      setEmailDesign(JSON.stringify(design, null, 2));
    });
  };

  const exportHtml = () => {
    const unlayer = emailEditorRef.current?.editor;

    unlayer?.exportHtml((data) => {
      const { design, html } = data;
      setEmailDesign(JSON.stringify(design, null, 2));
      setEmailHtml(html);
    });

    unlayer?.exportPlainText((data) => {
      // console.log("text", data.text);
      setEmailText(data.text);
    });
  };

  const onReady: REE.EmailEditorProps["onReady"] = (unlayer) => {
    // editor is ready
    // you can load your template here;
    if (initialDesign) {
      unlayer.loadDesign(initialDesign);
    }
  };

  return (
    <Box display="flex" gap={2}>
      <Box>
        <Box display="flex" gap={1} mb={2}>
          <Button onClick={exportHtml} variant="contained">
            Export HTML
          </Button>
          <Button onClick={saveDesign} variant="contained">
            Save Design
          </Button>
        </Box>

        <REE.EmailEditor ref={emailEditorRef} onReady={onReady} />
      </Box>
      <Box width={300}>
        <Typography my={2} variant="h6">
          Design
        </Typography>
        <Box component="pre" maxHeight={300} overflow="scroll">
          {emailDesign}
        </Box>
        <Typography my={2} variant="h6">
          HTML
        </Typography>
        <Box component="pre" maxHeight={300} overflow="scroll">
          {emailHtml}
        </Box>
        <Typography my={2} variant="h6">
          Text
        </Typography>
        <Box component="pre" maxHeight={300} overflow="scroll">
          {emailText}
        </Box>
      </Box>
    </Box>
  );
}
