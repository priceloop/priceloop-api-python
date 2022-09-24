from dataclasses import dataclass
from datetime import datetime, timedelta

import boto3
import requests


@dataclass(frozen=True)
class ApiConfig:
    region: str
    client_id: str
    api_scopes: str
    auth_url: str


@dataclass(frozen=True)
class AuthTokens:
    access_token: str
    expires_in_seconds: int
    expiry_date: datetime
    id_token: str
    refresh_token: str
    token_type: str


class AuthState(object):
    nocode_config: ApiConfig = None
    auth_tokens: AuthTokens = None

    def access_token(self):
        if self.nocode_config is None:
            self.nocode_config = get_config(f'https://{self.host}/app_config.json')

        if self.auth_tokens is None or is_expired(datetime.now(), self.auth_tokens):
            self.auth_tokens = get_oauth_tokens(self.nocode_config, self.username, self.password)

        return self.auth_tokens.access_token

    def __init__(self, username, password, host):
        self.host = host
        self.username = username
        self.password = password


def is_expired(now: datetime, tokens: AuthTokens) -> bool:
    return tokens.expiry_date - timedelta(minutes=1) > now


def get_config(app_config_url: str) -> ApiConfig:
    cfg = requests.get(app_config_url).json()

    return ApiConfig(
            region=cfg['region'],
            client_id=cfg['auth']['clientId'],
            api_scopes=cfg['auth']['apiScopes'],
            auth_url=cfg['auth']['url']
    )


def get_oauth_tokens(config: ApiConfig, user_email: str, user_password: str) -> AuthTokens:
    cognito_client = boto3.client('cognito-idp', region_name=config.region)
    auth_response = cognito_client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': user_email,
                'PASSWORD': user_password
            },
            ClientId=config.client_id
    )

    # calculate expiry date, because cognito only gives the number of seconds
    now = datetime.today()
    expires_in_seconds = int(auth_response['AuthenticationResult']['ExpiresIn'])
    expiry_date = now + timedelta(seconds=expires_in_seconds)

    return AuthTokens(
            access_token=auth_response['AuthenticationResult']['AccessToken'],
            expires_in_seconds=expires_in_seconds,
            expiry_date=expiry_date,
            id_token=auth_response['AuthenticationResult']['IdToken'],
            refresh_token=auth_response['AuthenticationResult']['RefreshToken'],
            token_type=auth_response['AuthenticationResult']['TokenType']
    )
