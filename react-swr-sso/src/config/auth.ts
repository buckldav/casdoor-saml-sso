import Sdk from "casdoor-js-sdk";

export const ServerUrl = "http://localhost:8888";

const sdkConfig = {
  serverUrl: "http://localhost:8001",
  clientId: "0a2cd1b53ff7f709be97",
  appName: "react-sso",
  organizationName: "built-in",
  redirectPath: "/callback",
  signinPath: "/callback",
};

export const CasdoorSDK = new Sdk(sdkConfig);

export const isLoggedIn = () => {
  const token = localStorage.getItem("token");
  return token !== null && token.length > 0;
};

export const setToken = (token: string) => {
  localStorage.setItem("token", token);
};

export const goToLink = (link: string) => {
  window.location.href = link;
};

export const getRedirectUrl = () => {
  return `${sdkConfig.serverUrl}/login/oauth/authorize?client_id=${sdkConfig.clientId}&response_type=code&state=${sdkConfig.appName}&redirect_uri=http://localhost:8888/callback`;
};

export const getUserinfo = () => {
  return fetch(`${ServerUrl}/whoami`, {
    method: "GET",
    credentials: "include",
  }).then((res) => res.json());
};

export const logout = () => {
  localStorage.removeItem("token");
};

export const showMessage = (message: string) => {
  alert(message);
};
