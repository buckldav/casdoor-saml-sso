import React from "react";

import { StoryFn, Meta } from "@storybook/react";
import { EmailComposeProps, EmailCompose } from "./email-compose";

export default {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/react/configure/overview#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: "Email/Email Compose",
  component: EmailCompose,
} as Meta<typeof EmailCompose>;

export const Primary = {
  args: {
    defaultFrom: "me@example.com",
  } as EmailComposeProps,
};
