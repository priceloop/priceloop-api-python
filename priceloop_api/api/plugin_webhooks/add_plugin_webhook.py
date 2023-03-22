from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_plugin_webhook_event import AddPluginWebhookEvent
from ...models.add_plugin_webhook_plugin_name import AddPluginWebhookPluginName
from ...models.webhook_config import WebhookConfig
from ...types import UNSET, Response


def _get_kwargs(
    plugin_name: AddPluginWebhookPluginName,
    *,
    client: AuthenticatedClient,
    json_body: WebhookConfig,
    event: AddPluginWebhookEvent,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/plugin/{pluginName}/webhooks".format(client.base_url, pluginName=plugin_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_event = event.value

    params["event"] = json_event

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plugin_name: AddPluginWebhookPluginName,
    *,
    client: AuthenticatedClient,
    json_body: WebhookConfig,
    event: AddPluginWebhookEvent,
) -> Response[Any]:
    """Register a plugin webhook


    # Plugin Webhooks

    This API allows you to register a webhook endpoint that receives plugin events from our platform.
    All events will be sent as *POST* requests to the provided webhook url.

    In case your webhook endpoint is down or responds with non-success status codes, we will retry to
    deliver the event up to 10 times over a time period of 1 hour.

    ## Registration/Confirmation

    After registering, you will receive a first message on your webhook endpoint to confirm the
    registration.
    The registration message looks like this:
    ```json
    {
      \"SubscribeURL\": \"https://...\"
    }
    ```

    You have to make a *GET* request to the `SubscribeURL` in order to receive further events.

    ## Events

    After confirmation, you will start receiving the desired plugin events.
    The event messages look like this:
    ```json
    {
      \"event\" : \"PluginInstalled\",
      \"pluginName\" : \"ape\",
      \"workspaceName\" : \"some-workspace-name\"
    }
    ```
    ```json
    {
      \"event\" : \"PluginUninstalled\",
      \"pluginName\" : \"ape\",
      \"workspaceName\" : \"some-workspace-name\"
    }
    ```
    ```json
    {
      \"event\" : \"PluginTokensUpdated\",
      \"pluginName\" : \"ape\",
      \"workspaceName\" : \"some-workspace-name\"
    }
    ```

    Args:
        plugin_name (AddPluginWebhookPluginName):
        event (AddPluginWebhookEvent):
        json_body (WebhookConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        plugin_name=plugin_name,
        client=client,
        json_body=json_body,
        event=event,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    plugin_name: AddPluginWebhookPluginName,
    *,
    client: AuthenticatedClient,
    json_body: WebhookConfig,
    event: AddPluginWebhookEvent,
) -> Response[Any]:
    """Register a plugin webhook


    # Plugin Webhooks

    This API allows you to register a webhook endpoint that receives plugin events from our platform.
    All events will be sent as *POST* requests to the provided webhook url.

    In case your webhook endpoint is down or responds with non-success status codes, we will retry to
    deliver the event up to 10 times over a time period of 1 hour.

    ## Registration/Confirmation

    After registering, you will receive a first message on your webhook endpoint to confirm the
    registration.
    The registration message looks like this:
    ```json
    {
      \"SubscribeURL\": \"https://...\"
    }
    ```

    You have to make a *GET* request to the `SubscribeURL` in order to receive further events.

    ## Events

    After confirmation, you will start receiving the desired plugin events.
    The event messages look like this:
    ```json
    {
      \"event\" : \"PluginInstalled\",
      \"pluginName\" : \"ape\",
      \"workspaceName\" : \"some-workspace-name\"
    }
    ```
    ```json
    {
      \"event\" : \"PluginUninstalled\",
      \"pluginName\" : \"ape\",
      \"workspaceName\" : \"some-workspace-name\"
    }
    ```
    ```json
    {
      \"event\" : \"PluginTokensUpdated\",
      \"pluginName\" : \"ape\",
      \"workspaceName\" : \"some-workspace-name\"
    }
    ```

    Args:
        plugin_name (AddPluginWebhookPluginName):
        event (AddPluginWebhookEvent):
        json_body (WebhookConfig):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        plugin_name=plugin_name,
        client=client,
        json_body=json_body,
        event=event,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
