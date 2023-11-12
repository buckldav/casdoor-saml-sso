import Sdk from "casdoor-js-sdk";
import { sdkConfig, logInURL } from "./settings";

export const ServerUrl = "http://localhost:4321";

export const CasdoorSDK = new Sdk(sdkConfig);

export const isLoggedIn = () => {
  return localStorage.getItem("token") !== null;
};

export const callback = () => {
  const params = new URLSearchParams(window.location.search);
  //if (CasdoorSDK.isSilentSigninRequested()
  // CasdoorSDK.silentSignin(
  //   () => {
  //     alert("success");
  //   },
  //   () => {
  //     alert("fail");
  //   }
  // );
  CasdoorSDK.signin(
    sdkConfig.serverUrl,
    sdkConfig.signinPath,
    params.get("code") ?? "",
    params.get("state") ?? ""
  ).then((value) => {
    if (value.status === "error") {
      console.log(value);
      alert("error");
    } else {
      window.location.href = "/";
    }
  });
};
