import requests

class AuthState(object):
    nocode_config = None
    auth_response = None

    def access_token():
        if nocode_config is None:
            nocode_config = requests.get(f'https://{self.host}/app_config.json').json()

        print(nocode_config.get("region"))
        print(nocode_config.get("auth").get("clientId"))
        print(nocode_config.get("auth").get("apiScopes").split(" "))

        if self.auth_response is None: #TODO: only get new one when expired
            self.auth_response = "???"

        return self.auth_response.access_token


    def __init__(self, username, password, host):
        self.host = host
        self.username = username
        self.password = password
