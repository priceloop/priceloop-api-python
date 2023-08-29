from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_table_data import ApiTableData
from ...types import UNSET, Response


def _get_kwargs(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    json_body: List[str],
    limit: int,
    offset: int,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/tables/{table}/incomplete-query-data".format(
        client.base_url, workspace=workspace, table=table
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ApiTableData]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiTableData.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ApiTableData]:
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
    json_body: List[str],
    limit: int,
    offset: int,
) -> Response[ApiTableData]:
    """Get the specified data of a table


    Get the specified data of a table without any guarantees of completed external function. In order to
    get the complete data with all calculated values, poll this endpoint until it has no more scheduled
    jobs (check response field `scheduledJobs == 0`).

    Please respect the polling interval given in `recommendedPollingIntervalSeconds`, in order to avoid
    degrading the performance of the database.


    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        limit (int):
        offset (int):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiTableData]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        client=client,
        json_body=json_body,
        limit=limit,
        offset=offset,
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
    json_body: List[str],
    limit: int,
    offset: int,
) -> Optional[ApiTableData]:
    """Get the specified data of a table


    Get the specified data of a table without any guarantees of completed external function. In order to
    get the complete data with all calculated values, poll this endpoint until it has no more scheduled
    jobs (check response field `scheduledJobs == 0`).

    Please respect the polling interval given in `recommendedPollingIntervalSeconds`, in order to avoid
    degrading the performance of the database.


    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        limit (int):
        offset (int):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiTableData
    """

    return sync_detailed(
        workspace=workspace,
        table=table,
        client=client,
        json_body=json_body,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    json_body: List[str],
    limit: int,
    offset: int,
) -> Response[ApiTableData]:
    """Get the specified data of a table


    Get the specified data of a table without any guarantees of completed external function. In order to
    get the complete data with all calculated values, poll this endpoint until it has no more scheduled
    jobs (check response field `scheduledJobs == 0`).

    Please respect the polling interval given in `recommendedPollingIntervalSeconds`, in order to avoid
    degrading the performance of the database.


    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        limit (int):
        offset (int):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiTableData]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        client=client,
        json_body=json_body,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    json_body: List[str],
    limit: int,
    offset: int,
) -> Optional[ApiTableData]:
    """Get the specified data of a table


    Get the specified data of a table without any guarantees of completed external function. In order to
    get the complete data with all calculated values, poll this endpoint until it has no more scheduled
    jobs (check response field `scheduledJobs == 0`).

    Please respect the polling interval given in `recommendedPollingIntervalSeconds`, in order to avoid
    degrading the performance of the database.


    Args:
        workspace (str):  Example: workspace-name.
        table (str):  Example: table-name.
        limit (int):
        offset (int):
        json_body (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiTableData
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            table=table,
            client=client,
            json_body=json_body,
            limit=limit,
            offset=offset,
        )
    ).parsed
