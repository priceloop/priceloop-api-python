import json
import os
from typing import Any, Optional

from priceloop_api.client import AuthenticatedClient
from priceloop_api.priceloop.auth import PriceloopClient


def get_token() -> Any:
    path = os.getcwd()
    with open(f"{path}/local_test/credentials") as f:
        crededentials = json.load(f)
    return crededentials["token"]["access_token"]


def get_priceloop_client(
    username: str = os.environ["NOCODE_USERNAME"],
    password: str = os.environ["NOCODE_PASSWORD"],
    raise_on_unexpected_status: bool = True,
) -> AuthenticatedClient:
    env = "dev" if os.environ["APP_ENV"] == "dev" else os.environ["APP_ENV"]
    if env == "local":
        return AuthenticatedClient(
            base_url="http://localhost:18080",
            token=get_token(),
            raise_on_unexpected_status=True,
            timeout=30.0,
        )
    host: Optional[str] = os.getenv("NOCODE_HOST")
    if host is None:
        env = "dev" if os.environ["APP_ENV"] == "local" else os.environ["APP_ENV"]
        host = "alpha.priceloop.ai" if env == "prod" else f"alpha-{env}.priceloop.ai"
    return PriceloopClient.with_credentials(
        username,
        password,
        host=host,
        raise_on_unexpected_status=raise_on_unexpected_status,
    )
