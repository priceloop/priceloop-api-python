from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_job import ExportJob
from ...types import Response


def _get_kwargs(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/tables/{table}/exports".format(
        client.base_url, workspace=workspace, table=table
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["ExportJob"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ExportJob.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["ExportJob"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["ExportJob"]]:
    """List all table exports

     This API endpoint returns a list of all available exports for a table. Exported files are kept
    available until `.availableUntil`.

    Args:
        workspace (str):
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ExportJob']]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["ExportJob"]]:
    """List all table exports

     This API endpoint returns a list of all available exports for a table. Exported files are kept
    available until `.availableUntil`.

    Args:
        workspace (str):
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ExportJob']
    """

    return sync_detailed(
        workspace=workspace,
        table=table,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["ExportJob"]]:
    """List all table exports

     This API endpoint returns a list of all available exports for a table. Exported files are kept
    available until `.availableUntil`.

    Args:
        workspace (str):
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ExportJob']]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["ExportJob"]]:
    """List all table exports

     This API endpoint returns a list of all available exports for a table. Exported files are kept
    available until `.availableUntil`.

    Args:
        workspace (str):
        table (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ExportJob']
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            table=table,
            client=client,
        )
    ).parsed
