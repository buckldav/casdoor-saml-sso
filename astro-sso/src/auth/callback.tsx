import * as Setting from "../auth/config";
import React from "react";

export function AuthHandlerCallback() {
  React.useEffect(() => {
    Setting.callback();
  }, []);
  return <div>Logging in...</div>;
}
