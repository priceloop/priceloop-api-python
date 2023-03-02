from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_csv_import_job_mode import CreateCsvImportJobMode
from ...models.import_job_response import ImportJobResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    mode: CreateCsvImportJobMode,
    separator: Union[Unset, None, str] = ",",
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/tables/{table}/csv-import-jobs".format(
        client.base_url, workspace=workspace, table=table
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_mode = mode.value

    params["mode"] = json_mode

    params["separator"] = separator

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ImportJobResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ImportJobResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ImportJobResponse]:
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
    mode: CreateCsvImportJobMode,
    separator: Union[Unset, None, str] = ",",
) -> Response[ImportJobResponse]:
    """Upload a CSV file into your table. This API endpoint returns a url, to which you can upload your csv
    file. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <csv-file> '<url>'.

    Args:
        workspace (str):
        table (str):
        mode (CreateCsvImportJobMode):
        separator (Union[Unset, None, str]):  Default: ','.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportJobResponse]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        client=client,
        mode=mode,
        separator=separator,
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
    mode: CreateCsvImportJobMode,
    separator: Union[Unset, None, str] = ",",
) -> Optional[ImportJobResponse]:
    """Upload a CSV file into your table. This API endpoint returns a url, to which you can upload your csv
    file. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <csv-file> '<url>'.

    Args:
        workspace (str):
        table (str):
        mode (CreateCsvImportJobMode):
        separator (Union[Unset, None, str]):  Default: ','.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportJobResponse]
    """

    return sync_detailed(
        workspace=workspace,
        table=table,
        client=client,
        mode=mode,
        separator=separator,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    mode: CreateCsvImportJobMode,
    separator: Union[Unset, None, str] = ",",
) -> Response[ImportJobResponse]:
    """Upload a CSV file into your table. This API endpoint returns a url, to which you can upload your csv
    file. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <csv-file> '<url>'.

    Args:
        workspace (str):
        table (str):
        mode (CreateCsvImportJobMode):
        separator (Union[Unset, None, str]):  Default: ','.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportJobResponse]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        client=client,
        mode=mode,
        separator=separator,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    mode: CreateCsvImportJobMode,
    separator: Union[Unset, None, str] = ",",
) -> Optional[ImportJobResponse]:
    """Upload a CSV file into your table. This API endpoint returns a url, to which you can upload your csv
    file. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <csv-file> '<url>'.

    Args:
        workspace (str):
        table (str):
        mode (CreateCsvImportJobMode):
        separator (Union[Unset, None, str]):  Default: ','.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportJobResponse]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            table=table,
            client=client,
            mode=mode,
            separator=separator,
        )
    ).parsed
