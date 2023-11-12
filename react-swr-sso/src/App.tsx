import * as authConfig from "./config/auth";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { AuthCallback } from "casdoor-react-sdk";
import "./App.css";
import Page from "./pages/index";
import { SessionProvider } from "./context/session";

function App() {
  const authCallback = (
    <AuthCallback
      sdk={authConfig.CasdoorSDK}
      serverUrl={authConfig.ServerUrl}
      saveTokenFromResponse={(res) => {
        authConfig.setToken(res?.data);
        authConfig.goToLink("/");
      }}
      isGetTokenSuccessful={(res) => res?.status === "ok"}
    />
  );

  return (
    <SessionProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/callback" element={authCallback} />
          <Route path="/" element={<Page />} />
        </Routes>
      </BrowserRouter>
    </SessionProvider>
  );
}

export default App;
