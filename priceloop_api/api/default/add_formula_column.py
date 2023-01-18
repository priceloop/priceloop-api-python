from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_column import ApiColumn
from ...types import UNSET, Response


def _get_kwargs(
    workspace: str,
    table: str,
    column: str,
    *,
    client: AuthenticatedClient,
    expression: str,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/tables/{table}/columns/{column}/formula".format(
        client.base_url, workspace=workspace, table=table, column=column
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["expression"] = expression

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ApiColumn]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiColumn.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ApiColumn]:
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
    expression: str,
) -> Response[ApiColumn]:
    """Add an expression column to a table.

    Args:
        workspace (str):
        table (str):
        column (str):
        expression (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiColumn]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        column=column,
        client=client,
        expression=expression,
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
    expression: str,
) -> Optional[ApiColumn]:
    """Add an expression column to a table.

    Args:
        workspace (str):
        table (str):
        column (str):
        expression (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiColumn]
    """

    return sync_detailed(
        workspace=workspace,
        table=table,
        column=column,
        client=client,
        expression=expression,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    table: str,
    column: str,
    *,
    client: AuthenticatedClient,
    expression: str,
) -> Response[ApiColumn]:
    """Add an expression column to a table.

    Args:
        workspace (str):
        table (str):
        column (str):
        expression (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiColumn]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        column=column,
        client=client,
        expression=expression,
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
    expression: str,
) -> Optional[ApiColumn]:
    """Add an expression column to a table.

    Args:
        workspace (str):
        table (str):
        column (str):
        expression (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiColumn]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            table=table,
            column=column,
            client=client,
            expression=expression,
        )
    ).parsed
