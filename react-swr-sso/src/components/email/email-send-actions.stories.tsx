import React from "react";

import { StoryFn, Meta } from "@storybook/react";
import { EmailSendActionsProps, EmailSendActions } from "./email-send-actions";

export default {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/react/configure/overview#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: "Email/Email Send Actions",
  component: EmailSendActions,
} as Meta<typeof EmailSendActions>;

export const Primary = {
  args: {} as EmailSendActionsProps,
};
