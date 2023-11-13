from fastapi import FastAPI, Request, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, HTMLResponse
from traceback import print_exc
from uuid import UUID, uuid4
from session.frontend import cookie
from session.backend import backend
from session.verify import verifier
from session.models import SessionData
from settings.config import (
    get_sdk_from_request,
    get_sdk_by_app_name,
    login_url,
    cors_origins,
)

from users.routes import router as user_router


app = FastAPI(debug=True)
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home(request: Request):
    sdk = get_sdk_from_request(request)
    try:
        session_data: SessionData = Depends(verifier)
        return HTMLResponse(
            f"""
<h1>Logged in to the App</h1>
<pre>{str(session_data.model_dump_json())}</pre>
<a href="{login_url(sdk)}">Log Out</a>
"""
        )
    except:
        return HTMLResponse(
            f"""
    <h1>Log In to the App</h1>
    <a href="{login_url(sdk)}">Log In</a>
    """
        )


@app.get("/callback")
async def callback(request: Request):
    """
    Get the JWT and decode it to see user info.
    """
    try:
        code = request.query_params["code"]
        state = request.query_params["state"]
        sdk = get_sdk_by_app_name(state)
        token = await sdk.get_oauth_token(code=code)
        access_token: str = token.get("access_token")
        # print(request.query_params, access_token)
        decoded_msg = sdk.parse_jwt_token(
            access_token
        )  # or sdk.parse_jwt_token(access_token, kwargs)
        print(access_token)
        # print(request.query_params, decoded_msg)
        session_id = uuid4()
        data = SessionData(**decoded_msg)
        await backend.create(session_id, data)
        # response = RedirectResponse("/back-to-react")
        response = RedirectResponse(f"http://localhost:5173")
        cookie.attach_to_response(response, session_id)
        return response
    except Exception as e:
        print("Could not create user session")
        print_exc(e)
    return RedirectResponse("/")


@app.get("/whoami", dependencies=[Depends(cookie)])
async def whoami(session_data: SessionData = Depends(verifier)):
    return session_data


@app.post("/delete_session")
async def del_session(response: Response, session_id: UUID = Depends(cookie)):
    await backend.delete(session_id)
    cookie.delete_from_response(response)
    return "deleted session"


app.include_router(user_router)

decoded_msg = {
    "owner": "built-in",
    "name": "admin",
    "createdTime": "2023-11-02T20:26:57Z",
    "updatedTime": "",
    "id": "1c4eedce-a575-48de-b649-f0baf62ae0cf",
    "type": "normal-user",
    "password": "",
    "passwordSalt": "",
    "passwordType": "plain",
    "displayName": "Admin",
    "firstName": "",
    "lastName": "",
    "avatar": "https://cdn.casbin.org/img/casbin.svg",
    "avatarType": "",
    "permanentAvatar": "",
    "email": "admin@example.com",
    "emailVerified": False,
    "phone": "12345678910",
    "countryCode": "US",
    "region": "",
    "location": "",
    "address": [],
    "affiliation": "Example Inc.",
    "title": "",
    "idCardType": "",
    "idCard": "",
    "homepage": "",
    "bio": "",
    "language": "",
    "gender": "",
    "birthday": "",
    "education": "",
    "score": 2000,
    "karma": 0,
    "ranking": 1,
    "isDefaultAvatar": False,
    "isOnline": False,
    "isAdmin": True,
    "isForbidden": False,
    "isDeleted": False,
    "signupApplication": "app-built-in",
    "hash": "",
    "preHash": "",
    "accessKey": "",
    "accessSecret": "",
    "github": "",
    "google": "",
    "qq": "",
    "wechat": "",
    "facebook": "",
    "dingtalk": "",
    "weibo": "",
    "gitee": "",
    "linkedin": "",
    "wecom": "",
    "lark": "",
    "gitlab": "",
    "createdIp": "127.0.0.1",
    "lastSigninTime": "",
    "lastSigninIp": "",
    "preferredMfaType": "",
    "recoveryCodes": None,
    "totpSecret": "",
    "mfaPhoneEnabled": False,
    "mfaEmailEnabled": False,
    "ldap": "",
    "properties": {},
    "roles": [],
    "permissions": [],
    "groups": [],
    "lastSigninWrongTime": "",
    "signinWrongTimes": 0,
    "tokenType": "access-token",
    "tag": "staff",
    "iss": "http://localhost:8000",
    "sub": "1c4eedce-a575-48de-b649-f0baf62ae0cf",
    "aud": ["db041defe7e8b019d2f6"],
    "exp": 1699570551,
    "nbf": 1698965751,
    "iat": 1698965751,
    "jti": "admin/ba7c2b3c-e73d-40d4-af88-669a3a0ab4b8",
}
