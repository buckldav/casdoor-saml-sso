from casdoor import AsyncCasdoorSDK
from fastapi import FastAPI, Request, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, HTMLResponse
from traceback import print_exc
from uuid import UUID, uuid4
from session.frontend import cookie
from session.backend import backend
from session.verify import verifier
from session.models import SessionData

# http://localhost:8001/certs/admin/cert-built-in
certificate = """-----BEGIN CERTIFICATE-----
MIIE3TCCAsWgAwIBAgIDAeJAMA0GCSqGSIb3DQEBCwUAMCgxDjAMBgNVBAoTBWFk
bWluMRYwFAYDVQQDEw1jZXJ0LWJ1aWx0LWluMB4XDTIzMTEwOTIwMjczMVoXDTQz
MTEwOTIwMjczMVowKDEOMAwGA1UEChMFYWRtaW4xFjAUBgNVBAMTDWNlcnQtYnVp
bHQtaW4wggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDJ21EKxS77+1pb
2a2s2TItSWutBkMRTZUDbJJTJDbseJNhtmNq44Mroo3ADxjAE4eMajyPau+fJchC
nD/n5gYZYuLpWeJzZFgz7dZ+c+LVgsE9AyfUJod9gEOJ+hIPcyZ7gFXssxOKJjEB
3BlT4MTgpzxKy2cbXnAkdM5T4cvkI/aawdJ346Nlt6G7cQuGca6uSMVEyeOV6zv6
u7BD2w4MALYPopguG74dsr96CykvKU3cw9XlZ/SYoSkC+NTn3AAeqWqqweaaki7u
SHi1uDreA2km7LDzd6t1XvUbst9PWOIiYLhtbAfqmNT1qV4j3QNnbDe1rOlZ8RrK
piR4OQQmOBlkM1ci+/y6F2GNKP9c9r/fAV1ZuP7xes9Geaj97HTgvTIZBfcX3W6U
avzHSoED7s3bC07qjHoJJL2LRxgy95NUvdKwngsG97g/Pi2YF0df02f8nyrrO+/b
hQQid4R2r9ZraRqYKref3TB+Z0J3FrJm/l1xTcVRo0d6waX09dEDDL9XzNHtpMA1
K08zSrzfZhWghBpQLxb5dL0K6yI37kRrvNM0jlDEuVWTOPaheq4iMKczv79aYHRD
otzWr/pZVAAwmrzN2rX1thAB3jjyQBL8IkwObF5GV7Gq7DKTvlWFOxo0rz1SYLPy
2yQURzW6PTI/4EhZcP0vtmZM4bhSDwIDAQABoxAwDjAMBgNVHRMBAf8EAjAAMA0G
CSqGSIb3DQEBCwUAA4ICAQAsjfIsv5GzQBTclqMvq23fahQ/ZzFpvKp3u5yTMMwY
132kf/5F5uh2MIKCdKGfXgoAN0WX+SuuoJKWCCM/lr+7m4nxhY8qHUFyrp6ByQCC
ArOVpJ/54OWpuESz0skhz2Sx8v9Lq7BSxI0ysHKjoE7Nj95n/TEvATAdki8oxNdW
vR111gu4Qatg8PBprAkanyckQi/RGNQzw0+Oy+G0FylPJTOxC3jjCYP7xUfnnMbd
ddrsmz0jlXYuqEx94gxfUFbLe2yx7LtPy+U8yj8YZcU+MoV1SlycB5cXyf44pj3z
27ziKC69r6jQlCbpIT1QEcZ5EzvwObg6lK5SXXAccUzM67rpnRqTm65kUBTHaLhp
xqfg4DZKbiM9zYlhLbhWCbKZ7FeAlrThGcQvzO2n//mjaGPNvPZtIbxBeOKyaNGq
Kx+ckosZwhGbX5nNBmYr1D7C9GAffLC/PhLDtQl87Mv/xpfkcfloyLgiQUf89TmE
2F5or+D8yFbgXQGdxmLUdhQhE6T/CH9UBhk60+46YxLFV0N2DZDltyY3ttcRQvkN
LMRfBI7F+7DEdKeBHGlzhVA2EjA54R+9audn8uGDhaVUDyTAIumQSVASo5cbn3FX
fl/RUMnusAItIvsSSzOZ4zMg1wZOXGl0Dw0YnxOygTVXGAh6q97VQZklwqwSNAZY
hA==
-----END CERTIFICATE-----"""

# casdoor server
endpoint = "http://localhost:8001"
# from http://localhost:8000/applications/built-in/application_859qtl
client_id = "0a2cd1b53ff7f709be97"
client_secret = "d2a972cc6c56e45e375498c8e8d329b38395bf2a"
org_name = "built-in"
application_name = "fast-sso"


# my settings
def login_url(sdk: AsyncCasdoorSDK):
    return f"{sdk.endpoint}/login/oauth/authorize?client_id={sdk.client_id}&response_type=code&state={sdk.application_name}&redirect_uri=http://localhost:8888/saml-callback"


sdk = AsyncCasdoorSDK(
    endpoint, client_id, client_secret, certificate, org_name, application_name
)


app = FastAPI(debug=True)
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:4321",
    "http://localhost:5173",
    "http://localhost:8888",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
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
        token = await sdk.get_oauth_token(code=code)
        access_token: str = token.get("access_token")
        # print(request.query_params, access_token)
        decoded_msg = sdk.parse_jwt_token(
            access_token
        )  # or sdk.parse_jwt_token(access_token, kwargs)
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


# @app.get("/back-to-react")
# async def after(session_id: UUID = Depends(cookie)):
#     response = RedirectResponse(f"http://localhost:5173")
#     cookie.attach_to_response(response, session_id)
#     return response


@app.get("/whoami", dependencies=[Depends(cookie)])
async def whoami(session_data: SessionData = Depends(verifier)):
    return session_data


@app.post("/delete_session")
async def del_session(response: Response, session_id: UUID = Depends(cookie)):
    await backend.delete(session_id)
    cookie.delete_from_response(response)
    return "deleted session"


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
