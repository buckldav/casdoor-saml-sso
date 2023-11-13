from typing import Optional
from pydantic import BaseModel, Field
from settings.database import Base
from sqlalchemy import String, Column, Boolean, Text, Integer, LargeBinary


class UserORM(Base):
    """
                                        Table "public.user"
             Column         |          Type           | Collation | Nullable | Default
    ------------------------+-------------------------+-----------+----------+---------
     owner                  | character varying(100)  |           | not null |
     name                   | character varying(100)  |           | not null |
     created_time           | character varying(100)  |           |          |
     updated_time           | character varying(100)  |           |          |
     id                     | character varying(100)  |           |          |
     external_id            | character varying(100)  |           |          |
     type                   | character varying(100)  |           |          |
     password               | character varying(100)  |           |          |
     password_salt          | character varying(100)  |           |          |
     password_type          | character varying(100)  |           |          |
     display_name           | character varying(100)  |           |          |
     first_name             | character varying(100)  |           |          |
     last_name              | character varying(100)  |           |          |
     avatar                 | character varying(500)  |           |          |
     avatar_type            | character varying(100)  |           |          |
     permanent_avatar       | character varying(500)  |           |          |
     email                  | character varying(100)  |           |          |
     email_verified         | boolean                 |           |          |
     phone                  | character varying(20)   |           |          |
     country_code           | character varying(6)    |           |          |
     region                 | character varying(100)  |           |          |
     location               | character varying(100)  |           |          |
     address                | text                    |           |          |
     affiliation            | character varying(100)  |           |          |
     title                  | character varying(100)  |           |          |
     id_card_type           | character varying(100)  |           |          |
     id_card                | character varying(100)  |           |          |
     homepage               | character varying(100)  |           |          |
     bio                    | character varying(100)  |           |          |
     tag                    | character varying(100)  |           |          |
     language               | character varying(100)  |           |          |
     gender                 | character varying(100)  |           |          |
     birthday               | character varying(100)  |           |          |
     education              | character varying(100)  |           |          |
     score                  | integer                 |           |          |
     karma                  | integer                 |           |          |
     ranking                | integer                 |           |          |
     is_default_avatar      | boolean                 |           |          |
     is_online              | boolean                 |           |          |
     is_admin               | boolean                 |           |          |
     is_forbidden           | boolean                 |           |          |
     is_deleted             | boolean                 |           |          |
     signup_application     | character varying(100)  |           |          |
     hash                   | character varying(100)  |           |          |
     pre_hash               | character varying(100)  |           |          |
     access_key             | character varying(100)  |           |          |
     access_secret          | character varying(100)  |           |          |
     created_ip             | character varying(100)  |           |          |
     last_signin_time       | character varying(100)  |           |          |
     last_signin_ip         | character varying(100)  |           |          |
     github                 | character varying(100)  |           |          |
     google                 | character varying(100)  |           |          |
     qq                     | character varying(100)  |           |          |
     wechat                 | character varying(100)  |           |          |
     facebook               | character varying(100)  |           |          |
     dingtalk               | character varying(100)  |           |          |
     weibo                  | character varying(100)  |           |          |
     gitee                  | character varying(100)  |           |          |
     linkedin               | character varying(100)  |           |          |
     wecom                  | character varying(100)  |           |          |
     lark                   | character varying(100)  |           |          |
     gitlab                 | character varying(100)  |           |          |
     adfs                   | character varying(100)  |           |          |
     baidu                  | character varying(100)  |           |          |
     alipay                 | character varying(100)  |           |          |
     casdoor                | character varying(100)  |           |          |
     infoflow               | character varying(100)  |           |          |
     apple                  | character varying(100)  |           |          |
     azuread                | character varying(100)  |           |          |
     slack                  | character varying(100)  |           |          |
     steam                  | character varying(100)  |           |          |
     bilibili               | character varying(100)  |           |          |
     okta                   | character varying(100)  |           |          |
     douyin                 | character varying(100)  |           |          |
     line                   | character varying(100)  |           |          |
     amazon                 | character varying(100)  |           |          |
     auth0                  | character varying(100)  |           |          |
     battlenet              | character varying(100)  |           |          |
     bitbucket              | character varying(100)  |           |          |
     box                    | character varying(100)  |           |          |
     cloudfoundry           | character varying(100)  |           |          |
     dailymotion            | character varying(100)  |           |          |
     deezer                 | character varying(100)  |           |          |
     digitalocean           | character varying(100)  |           |          |
     discord                | character varying(100)  |           |          |
     dropbox                | character varying(100)  |           |          |
     eveonline              | character varying(100)  |           |          |
     fitbit                 | character varying(100)  |           |          |
     gitea                  | character varying(100)  |           |          |
     heroku                 | character varying(100)  |           |          |
     influxcloud            | character varying(100)  |           |          |
     instagram              | character varying(100)  |           |          |
     intercom               | character varying(100)  |           |          |
     kakao                  | character varying(100)  |           |          |
     lastfm                 | character varying(100)  |           |          |
     mailru                 | character varying(100)  |           |          |
     meetup                 | character varying(100)  |           |          |
     microsoftonline        | character varying(100)  |           |          |
     naver                  | character varying(100)  |           |          |
     nextcloud              | character varying(100)  |           |          |
     onedrive               | character varying(100)  |           |          |
     oura                   | character varying(100)  |           |          |
     patreon                | character varying(100)  |           |          |
     paypal                 | character varying(100)  |           |          |
     salesforce             | character varying(100)  |           |          |
     shopify                | character varying(100)  |           |          |
     soundcloud             | character varying(100)  |           |          |
     spotify                | character varying(100)  |           |          |
     strava                 | character varying(100)  |           |          |
     stripe                 | character varying(100)  |           |          |
     tiktok                 | character varying(100)  |           |          |
     tumblr                 | character varying(100)  |           |          |
     twitch                 | character varying(100)  |           |          |
     twitter                | character varying(100)  |           |          |
     typetalk               | character varying(100)  |           |          |
     uber                   | character varying(100)  |           |          |
     vk                     | character varying(100)  |           |          |
     wepay                  | character varying(100)  |           |          |
     xero                   | character varying(100)  |           |          |
     yahoo                  | character varying(100)  |           |          |
     yammer                 | character varying(100)  |           |          |
     yandex                 | character varying(100)  |           |          |
     zoom                   | character varying(100)  |           |          |
     metamask               | character varying(100)  |           |          |
     web3onboard            | character varying(100)  |           |          |
     custom                 | character varying(100)  |           |          |
     webauthnCredentials    | bytea                   |           |          |
     preferred_mfa_type     | character varying(100)  |           |          |
     recovery_codes         | character varying(1000) |           |          |
     totp_secret            | character varying(100)  |           |          |
     mfa_phone_enabled      | boolean                 |           |          |
     mfa_email_enabled      | boolean                 |           |          |
     ldap                   | character varying(100)  |           |          |
     properties             | text                    |           |          |
     roles                  | text                    |           |          |
     permissions            | text                    |           |          |
     groups                 | character varying(1000) |           |          |
     last_signin_wrong_time | character varying(100)  |           |          |
     signin_wrong_times     | integer                 |           |          |
     managedAccounts        | bytea                   |           |          |
    Indexes:
        "user_pkey" PRIMARY KEY, btree (owner, name)
        "IDX_user_created_time" btree (created_time)
        "IDX_user_email" btree (email)
        "IDX_user_external_id" btree (external_id)
        "IDX_user_id" btree (id)
        "IDX_user_id_card" btree (id_card)
        "IDX_user_phone" btree (phone)
    """

    __tablename__ = "user"

    # varchar does not need length if no CREATE TABLE is issued
    # https://docs.sqlalchemy.org/en/20/core/type_basics.html#sqlalchemy.types.String.params.length
    owner = Column(String, primary_key=True, index=True)
    name = Column(String, primary_key=True, index=True)
    created_time = Column(String, index=True)
    updated_time = Column(String)
    id = Column(String, index=True)
    external_id = Column(String, index=True)
    type = Column(String)
    password = Column(String)
    password_salt = Column(String)
    password_type = Column(String)
    display_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    avatar = Column(String)
    avatar_type = Column(String)
    permanent_avatar = Column(String)
    email = Column(String, index=True)
    email_verified = Column(Boolean)
    phone = Column(String, index=True)
    country_code = Column(String)
    region = Column(String)
    location = Column(String)
    address = Column(Text)
    affiliation = Column(String)
    title = Column(String)
    id_card_type = Column(String)
    id_card = Column(String, index=True)
    homepage = Column(String)
    bio = Column(String)
    tag = Column(String)
    language = Column(String)
    gender = Column(String)
    birthday = Column(String)
    education = Column(String)
    score = Column(Integer)
    karma = Column(Integer)
    ranking = Column(Integer)
    is_default_avatar = Column(Boolean)
    is_online = Column(Boolean)
    is_admin = Column(Boolean)
    is_forbidden = Column(Boolean)
    is_deleted = Column(Boolean)
    signup_application = Column(String)
    hash = Column(String)
    pre_hash = Column(String)
    access_key = Column(String)
    access_secret = Column(String)
    created_ip = Column(String)
    last_signin_time = Column(String)
    last_signin_ip = Column(String)
    github = Column(String)
    google = Column(String)
    qq = Column(String)
    wechat = Column(String)
    facebook = Column(String)
    dingtalk = Column(String)
    weibo = Column(String)
    gitee = Column(String)
    linkedin = Column(String)
    wecom = Column(String)
    lark = Column(String)
    gitlab = Column(String)
    adfs = Column(String)
    baidu = Column(String)
    alipay = Column(String)
    casdoor = Column(String)
    infoflow = Column(String)
    apple = Column(String)
    azuread = Column(String)
    slack = Column(String)
    steam = Column(String)
    bilibili = Column(String)
    okta = Column(String)
    douyin = Column(String)
    line = Column(String)
    amazon = Column(String)
    auth0 = Column(String)
    battlenet = Column(String)
    bitbucket = Column(String)
    box = Column(String)
    cloudfoundry = Column(String)
    dailymotion = Column(String)
    deezer = Column(String)
    digitalocean = Column(String)
    discord = Column(String)
    dropbox = Column(String)
    eveonline = Column(String)
    fitbit = Column(String)
    gitea = Column(String)
    heroku = Column(String)
    influxcloud = Column(String)
    instagram = Column(String)
    intercom = Column(String)
    kakao = Column(String)
    lastfm = Column(String)
    mailru = Column(String)
    meetup = Column(String)
    microsoftonline = Column(String)
    naver = Column(String)
    nextcloud = Column(String)
    onedrive = Column(String)
    oura = Column(String)
    patreon = Column(String)
    paypal = Column(String)
    salesforce = Column(String)
    shopify = Column(String)
    soundcloud = Column(String)
    spotify = Column(String)
    strava = Column(String)
    stripe = Column(String)
    tiktok = Column(String)
    tumblr = Column(String)
    twitch = Column(String)
    twitter = Column(String)
    typetalk = Column(String)
    uber = Column(String)
    vk = Column(String)
    wepay = Column(String)
    xero = Column(String)
    yahoo = Column(String)
    yammer = Column(String)
    yandex = Column(String)
    zoom = Column(String)
    metamask = Column(String)
    web3onboard = Column(String)
    custom = Column(String)
    webauthnCredentials = Column(LargeBinary)
    preferred_mfa_type = Column(String)
    recovery_codes = Column(String)
    totp_secret = Column(String)
    mfa_phone_enabled = Column(Boolean)
    mfa_email_enabled = Column(Boolean)
    ldap = Column(String)
    properties = Column(Text)
    roles = Column(Text)
    permissions = Column(Text)
    groups = Column(String)
    last_signin_wrong_time = Column(String)
    signin_wrong_times = Column(Integer)
    managedAccounts = Column(LargeBinary)


class UserShared(BaseModel):
    display_name: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    signup_application: Optional[str] = Field(
        description="Where the sign up came from", default="app-built-in"
    )


class UserCreate(UserShared):
    """
    From sign-up info.
    Default sign-up items can be found in a Casdoor application's edit screen.
    """

    owner: Optional[str] = Field(
        description="Added by the client or by the backend process"
    )
    name: str = Field(description="Username")
    confirm: Optional[str] = Field(description="confirm password", default=None)
    agreement: Optional[bool] = None


class User(UserShared):
    """
    Require owner and name.
    """

    owner: str = Field(description="organization name")
    name: str

    class Config:
        """
        https://fastapi.tiangolo.com/tutorial/sql-databases/#create-initial-pydantic-models-schemas
        """

        orm_mode = True
