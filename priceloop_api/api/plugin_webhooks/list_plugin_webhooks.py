from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_plugin_webhooks_plugin_name import ListPluginWebhooksPluginName
from ...models.webhook_info import WebhookInfo
from ...types import Response


def _get_kwargs(
    plugin_name: ListPluginWebhooksPluginName,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/plugin/{pluginName}/webhooks".format(client.base_url, pluginName=plugin_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["WebhookInfo"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = WebhookInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["WebhookInfo"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plugin_name: ListPluginWebhooksPluginName,
    *,
    client: AuthenticatedClient,
) -> Response[List["WebhookInfo"]]:
    """List all plugin webhooks

    Args:
        plugin_name (ListPluginWebhooksPluginName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['WebhookInfo']]
    """

    kwargs = _get_kwargs(
        plugin_name=plugin_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    plugin_name: ListPluginWebhooksPluginName,
    *,
    client: AuthenticatedClient,
) -> Optional[List["WebhookInfo"]]:
    """List all plugin webhooks

    Args:
        plugin_name (ListPluginWebhooksPluginName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['WebhookInfo']]
    """

    return sync_detailed(
        plugin_name=plugin_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    plugin_name: ListPluginWebhooksPluginName,
    *,
    client: AuthenticatedClient,
) -> Response[List["WebhookInfo"]]:
    """List all plugin webhooks

    Args:
        plugin_name (ListPluginWebhooksPluginName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['WebhookInfo']]
    """

    kwargs = _get_kwargs(
        plugin_name=plugin_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plugin_name: ListPluginWebhooksPluginName,
    *,
    client: AuthenticatedClient,
) -> Optional[List["WebhookInfo"]]:
    """List all plugin webhooks

    Args:
        plugin_name (ListPluginWebhooksPluginName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['WebhookInfo']]
    """

    return (
        await asyncio_detailed(
            plugin_name=plugin_name,
            client=client,
        )
    ).parsed
