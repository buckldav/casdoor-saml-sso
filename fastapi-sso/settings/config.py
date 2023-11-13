from casdoor import AsyncCasdoorSDK
from decouple import config
from pydantic import BaseModel
from fastapi import Request
import json


def load_sdks():
    apps_config = {}
    certs = {}
    apps = {}
    casdoor_endpoint = ""
    with open("./settings/apps.json", "r") as f:
        apps_config = json.loads(f.read())
        casdoor_endpoint = apps_config["casdoor_endpoint"]
        certs = apps_config["certificates"]
        apps = apps_config["apps"]

    sdks = {
        app["endpoint"]: AsyncCasdoorSDK(
            **{
                **app,
                "endpoint": casdoor_endpoint,
                "certificate": certs[app["certificate"]],
            }
        )
        for app in apps
    }

    cors_origins = ["http://localhost", casdoor_endpoint] + [
        app["endpoint"] for app in apps
    ]
    return (sdks, cors_origins)


sdks, cors_origins = load_sdks()


def login_url(sdk: AsyncCasdoorSDK):
    return f"{sdk.endpoint}/login/oauth/authorize?client_id={sdk.client_id}&response_type=code&state={sdk.application_name}&redirect_uri=http://localhost:8888/saml-callback"


def get_sdk(endpoint: str) -> AsyncCasdoorSDK | None:
    if endpoint in sdks:
        return sdks[endpoint]
    else:
        return None


def get_sdk_by_app_name(app_name: str) -> AsyncCasdoorSDK | None:
    for sdk in sdks.values():
        if sdk.application_name == app_name:
            return sdk
    return None


def get_sdk_from_request(request: Request) -> AsyncCasdoorSDK | None:
    return get_sdk(request.headers.get("origin"))


class Settings(BaseModel):
    db_url: str = config(
        "CASDOOR_DB_URL",
        default="postgresql://postgres:postgres@localhost:5433/casdoor",
    )


CONFIG = Settings()
