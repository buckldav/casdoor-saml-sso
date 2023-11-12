import React from "react";
import useSWR from "swr";
import { getUserinfo } from "../config/auth";

export const SessionContext = React.createContext({
  session: null,
});

export function SessionProvider({ children }: React.PropsWithChildren<{}>) {
  const { data, error, isLoading } = useSWR("session", getUserinfo);

  if (isLoading) {
    return "Loading...";
  } else if (error) {
    return <pre>{JSON.stringify(error, null, 2)}</pre>;
  } else {
    console.log(data);
    let session = null;
    if (!data["detail"]) {
      session = data;
    }
    return (
      <SessionContext.Provider value={{ session }}>
        {children}
      </SessionContext.Provider>
    );
  }
}
