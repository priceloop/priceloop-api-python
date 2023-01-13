from priceloop_api.auth import AuthState, get_config

default_host = "alpha.priceloop.ai"


class PriceloopClient():
    @staticmethod
    def with_credentials(username: str, password: str, host: str = default_host):
        auth_state = AuthState(username, password, host)
        token = auth_state.access_token()
        nocode_config = get_config(f"https://{host}/app_config.json")
        return AuthenticatedClient(base_url=nocode_config.base_url, token=token, timeout=30.0)
