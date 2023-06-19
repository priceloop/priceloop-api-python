from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_column_attributes import ApiColumnAttributes
from ...types import Response


def _get_kwargs(
    workspace: str,
    table: str,
    column: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/tables/{table}/columns/{column}/attributes".format(
        client.base_url, workspace=workspace, table=table, column=column
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ApiColumnAttributes]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiColumnAttributes.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ApiColumnAttributes]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    table: str,
    column: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiColumnAttributes]:
    """Retrieve the attributes of a column

    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        column (str):  Example: column-name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiColumnAttributes]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        column=column,
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
    column: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ApiColumnAttributes]:
    """Retrieve the attributes of a column

    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        column (str):  Example: column-name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiColumnAttributes
    """

    return sync_detailed(
        workspace=workspace,
        table=table,
        column=column,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    table: str,
    column: str,
    *,
    client: AuthenticatedClient,
) -> Response[ApiColumnAttributes]:
    """Retrieve the attributes of a column

    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        column (str):  Example: column-name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiColumnAttributes]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        column=column,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    table: str,
    column: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ApiColumnAttributes]:
    """Retrieve the attributes of a column

    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        column (str):  Example: column-name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiColumnAttributes
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            table=table,
            column=column,
            client=client,
        )
    ).parsed
