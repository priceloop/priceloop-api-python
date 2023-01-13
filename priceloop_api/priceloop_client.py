from priceloop_api.auth import AuthState, get_config

import attr

default_host = "alpha.priceloop.ai"


@attr.s(auto_attribs=True)
class PriceloopClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    _auth_state: AuthState

    def __init__(auth_state: AuthState):
        self._auth_state = auth_state

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        auth_header_value = f"Bearer {self._auth_state.access_token}"
        return {"Authorization": auth_header_value, **self.headers}

    @staticmethod
    def with_credentials(username: str, password: str, host: str = default_host):
        auth_state = AuthState(username, password, host)
        return PriceloopClient(auth_state)
