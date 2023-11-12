import * as Setting from "./config";
import { logInURL } from "../auth/settings";

export type AuthGuardProps = {
  noAuthChildren?: any;
  authChildren: any;
  redirectIfNotLoggedIn?: boolean;
};

export function AuthGuard({
  noAuthChildren,
  authChildren,
  redirectIfNotLoggedIn,
}: AuthGuardProps) {
  if (Setting.isLoggedIn()) {
    return authChildren;
  } else if (redirectIfNotLoggedIn) {
    return "redirect";
  } else {
    return (
      <div>
        <a href={logInURL}>Log in</a>
      </div>
    );
  }
}
