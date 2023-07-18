from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.table_publication import TablePublication
from ...types import Response


def _get_kwargs(
    workspace: str,
    plugin: str,
    name: str,
    publication_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/plugin/{plugin}/table-roles/{name}/publications/{publicationId}".format(
        client.base_url, workspace=workspace, plugin=plugin, name=name, publicationId=publication_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[TablePublication]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TablePublication.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[TablePublication]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    plugin: str,
    name: str,
    publication_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[TablePublication]:
    """Get a publication for a PluginTableRole

    Args:
        workspace (str):  Example: workspace-name.
        plugin (str):
        name (str):
        publication_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TablePublication]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        plugin=plugin,
        name=name,
        publication_id=publication_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    plugin: str,
    name: str,
    publication_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[TablePublication]:
    """Get a publication for a PluginTableRole

    Args:
        workspace (str):  Example: workspace-name.
        plugin (str):
        name (str):
        publication_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TablePublication
    """

    return sync_detailed(
        workspace=workspace,
        plugin=plugin,
        name=name,
        publication_id=publication_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    plugin: str,
    name: str,
    publication_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[TablePublication]:
    """Get a publication for a PluginTableRole

    Args:
        workspace (str):  Example: workspace-name.
        plugin (str):
        name (str):
        publication_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TablePublication]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        plugin=plugin,
        name=name,
        publication_id=publication_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    plugin: str,
    name: str,
    publication_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[TablePublication]:
    """Get a publication for a PluginTableRole

    Args:
        workspace (str):  Example: workspace-name.
        plugin (str):
        name (str):
        publication_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TablePublication
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            plugin=plugin,
            name=name,
            publication_id=publication_id,
            client=client,
        )
    ).parsed
