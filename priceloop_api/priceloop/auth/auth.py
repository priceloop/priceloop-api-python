from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

import boto3  # type: ignore
import requests


@dataclass(frozen=True)
class ApiConfig:
    region: str
    client_id: str
    api_scopes: str
    auth_url: str
    base_url: str


@dataclass(frozen=True)
class AuthTokens:
    access_token: str
    expires_in_seconds: int
    expiry_date: datetime
    id_token: str
    refresh_token: str
    token_type: str


class AuthState:
    nocode_config: Optional[ApiConfig] = None
    auth_tokens: Optional[AuthTokens] = None
    username: str
    password: str
    host: str

    def config(self) -> ApiConfig:
        if self.nocode_config is None:
            endpoint = f"https://{self.host}/app_config.json"

            self.nocode_config = get_config(endpoint)

        return self.nocode_config

    def access_token(self) -> str:
        if self.auth_tokens is None or is_expired(datetime.now(), self.auth_tokens):
            self.auth_tokens = get_oauth_tokens(self.config(), self.username, self.password)

        return self.auth_tokens.access_token

    def __init__(self, username: str, password: str, host: str):
        self.username = username
        self.password = password
        self.host = host


def is_expired(now: datetime, tokens: AuthTokens) -> bool:
    return tokens.expiry_date - timedelta(minutes=1) > now


def get_config(app_config_url: str, auth_endpoint: Optional[str] = None) -> ApiConfig:
    response = requests.get(app_config_url)
    cfg = response.json()
    endpoint = None

    if auth_endpoint is None:
        endpoint = cfg["auth"]["url"]
    else:
        endpoint = auth_endpoint

    return ApiConfig(
        region=cfg["region"],
        client_id=cfg["auth"]["clientId"],
        api_scopes=cfg["auth"]["apiScopes"],
        auth_url=endpoint,
        base_url=cfg["http"]["url"],
    )


def get_oauth_tokens(config: ApiConfig, user_email: str, user_password: str) -> AuthTokens:
    cognito_client = boto3.client("cognito-idp", region_name=config.region)

    auth_response = cognito_client.initiate_auth(
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={"USERNAME": user_email, "PASSWORD": user_password},
        ClientId=config.client_id,
    )

    # calculate expiry date, because cognito only gives the number of seconds
    now = datetime.today()
    expires_in_seconds = int(auth_response["AuthenticationResult"]["ExpiresIn"])
    expiry_date = now + timedelta(seconds=expires_in_seconds)

    return AuthTokens(
        access_token=auth_response["AuthenticationResult"]["AccessToken"],
        expires_in_seconds=expires_in_seconds,
        expiry_date=expiry_date,
        id_token=auth_response["AuthenticationResult"]["IdToken"],
        refresh_token=auth_response["AuthenticationResult"]["RefreshToken"],
        token_type=auth_response["AuthenticationResult"]["TokenType"],
    )
