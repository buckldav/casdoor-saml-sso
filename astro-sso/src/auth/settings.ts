export const sdkConfig = {
  serverUrl: "http://localhost:8001",
  clientId: "fe289a70c81ee64224fc",
  appName: "astro-sso",
  organizationName: "built-in",
  redirectPath: "/callback",
  signinPath: "/api/login",
};

export const logInURL = `${sdkConfig.serverUrl}/login/oauth/authorize?client_id=${sdkConfig.clientId}&response_type=code&state=${sdkConfig.appName}&redirect_uri=http://localhost:4321/callback`;
