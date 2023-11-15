import React from "react";

import { StoryFn, Meta } from "@storybook/react";
import { EmailEditorProps, EmailEditor } from "./email-editor";
import sample from "../../../.storybook/data/email/sample.json";

export default {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/react/configure/overview#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: "Email/Email Editor",
  component: EmailEditor,
} as Meta<typeof EmailEditor>;

export const Primary = {
  args: {} as EmailEditorProps,
};

export const LoadDesign = {
  args: { initialDesign: sample } as EmailEditorProps,
};
