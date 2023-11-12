import React from "react";
import { SessionContext } from "../context/session";
import { getRedirectUrl } from "../config/auth";

export default function Page() {
  const { session } = React.useContext(SessionContext);
  return (
    <>
      <h1>Home</h1>
      <p>yeeeee</p>
      {session ? (
        <pre>{JSON.stringify(session, null, 2)}</pre>
      ) : (
        <a href={getRedirectUrl()}>Log in</a>
      )}
    </>
  );
}
