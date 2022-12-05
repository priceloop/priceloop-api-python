import priceloop_api
from typing import Callable

from priceloop_api.utils.auth_state import AuthState

default_host_name = 'alpha.priceloop.ai'

class DefaultConfiguration(priceloop_api.Configuration):

    @staticmethod
    def with_access_token(
        access_token: str,
        host: str = default_host_name,
        api_endpoint: str = None,
    ):
        return DefaultConfiguration( access_token_func = lambda: access_token, host = host, api_endpoint = api_endpoint)

    @staticmethod
    def with_user_credentials(
        username: str,
        password: str,
        host: str = default_host_name,
        host_endpoint: str = None,
        api_endpoint: str = None,
        auth_endpoint: str = None,
    ):
        auth_state = AuthState( username = username, password = password, host = host, host_endpoint = host_endpoint, auth_endpoint = auth_endpoint)
        return DefaultConfiguration( access_token_func = auth_state.access_token, host = host, api_endpoint = api_endpoint)

    @staticmethod
    def anon(
        host: str = default_host_name,
        api_endpoint: str = None,
    ):
        return DefaultConfiguration(host = host, api_endpoint = api_endpoint)

    def __init__(
        self, access_token_func: Callable[[], str] = None,
        host: str = default_host_name,
        api_endpoint: str = None,
    ):
        endpoint = None

        if api_endpoint is None:
            endpoint = f'https://api.{host}'
        else:
            endpoint = api_endpoint

        super().__init__(host = endpoint)
        self._access_token_func = access_token_func

    def auth_settings(self):
        if self._access_token_func is not None:
            self.access_token = self._access_token_func()

        return super().auth_settings()
