from .auth import AuthState
from priceloop_api import Client
from typing import Dict
import attr

default_host = "alpha.priceloop.ai"


class PriceloopClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    auth_state: AuthState

    def __init__(self, auth_state: AuthState):
        self.base_url = auth_state.config().base_url
        self.timeout = 30.0
        self.cookies = {}
        self.headers = {}
        self.verify_ssl = True
        self.raise_on_unexpected_status = False
        self.auth_state = auth_state

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        auth_header_value = f"Bearer {self.auth_state.access_token()}"
        return {"Authorization": auth_header_value, **self.headers}

    @staticmethod
    def with_credentials(username: str, password: str, host: str = default_host):
        auth_state = AuthState(username, password, host)
        return PriceloopClient(auth_state)
