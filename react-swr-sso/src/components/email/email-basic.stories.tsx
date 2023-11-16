import React from "react";

import { StoryFn, Meta } from "@storybook/react";
import { EmailBasicProps, EmailBasic } from "./email-basic";

export default {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/react/configure/overview#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: "Email/Email Basic",
  component: EmailBasic,
} as Meta<typeof EmailBasic>;

export const Primary = {
  args: {} as EmailBasicProps,
};
