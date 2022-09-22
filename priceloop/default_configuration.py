import priceloop_api

from priceloop.auth_state import AuthState

default_host_name = "pr-1039.dyn.alpha-dev.priceloop.ai"

class DefaultConfiguration(priceloop_api.Configuration):
    @staticmethod
    def with_user_credentials(username, password, host=default_host_name):
        auth_state = AuthState(username, password, host)
        return DefaultConfiguration(
            host = f"api.{host}",
            access_token_func = auth_state.access_token
        )

    def __init__(self, host=default_host_name, access_token_func=None):
        super().__init__(host = host)
        self._access_token_func = access_token_func

    def auth_settings(self):
        print("Auth settings called")
        if self._access_token_func is not None:
            self.accessToken = self._access_token_func()

        return super().auth_settings(self)

