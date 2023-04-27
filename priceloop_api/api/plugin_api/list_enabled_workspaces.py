from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.plugin_name import PluginName
from ...models.plugin_workspace_list import PluginWorkspaceList
from ...types import Response


def _get_kwargs(
    plugin: PluginName,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/plugin/{plugin}/enabled-workspaces".format(client.base_url, plugin=plugin)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PluginWorkspaceList]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PluginWorkspaceList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PluginWorkspaceList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    plugin: PluginName,
    *,
    client: AuthenticatedClient,
) -> Response[PluginWorkspaceList]:
    """Lists all workspaces that have this plugin installed

    Args:
        plugin (PluginName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PluginWorkspaceList]
    """

    kwargs = _get_kwargs(
        plugin=plugin,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    plugin: PluginName,
    *,
    client: AuthenticatedClient,
) -> Optional[PluginWorkspaceList]:
    """Lists all workspaces that have this plugin installed

    Args:
        plugin (PluginName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PluginWorkspaceList]
    """

    return sync_detailed(
        plugin=plugin,
        client=client,
    ).parsed


async def asyncio_detailed(
    plugin: PluginName,
    *,
    client: AuthenticatedClient,
) -> Response[PluginWorkspaceList]:
    """Lists all workspaces that have this plugin installed

    Args:
        plugin (PluginName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PluginWorkspaceList]
    """

    kwargs = _get_kwargs(
        plugin=plugin,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    plugin: PluginName,
    *,
    client: AuthenticatedClient,
) -> Optional[PluginWorkspaceList]:
    """Lists all workspaces that have this plugin installed

    Args:
        plugin (PluginName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PluginWorkspaceList]
    """

    return (
        await asyncio_detailed(
            plugin=plugin,
            client=client,
        )
    ).parsed
