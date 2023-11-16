import React from "react";

import { StoryFn, Meta } from "@storybook/react";
import { EmailScheduleProps, EmailSchedule } from "./email-schedule";

export default {
  /* 👇 The title prop is optional.
   * See https://storybook.js.org/docs/react/configure/overview#configure-story-loading
   * to learn how to generate automatic titles
   */
  title: "Email/Email Schedule",
  component: EmailSchedule,
} as Meta<typeof EmailSchedule>;

export const Primary = {
  args: {} as EmailScheduleProps,
};
