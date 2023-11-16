import React from "react";

import { StoryFn, Meta } from "@storybook/react";
import { EmailRecipientsProps, EmailRecipients } from "./email-recipients";

export default {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/react/configure/overview#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: "Email Recipients",
  component: EmailRecipients,
} as Meta<typeof EmailRecipients>;

export const Primary = {
  args: {} as EmailRecipientsProps,
};
