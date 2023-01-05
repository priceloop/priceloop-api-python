from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_table_upload_csv_url_mode import GetTableUploadCsvUrlMode
from ...models.presigned_url import PresignedUrl
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    mode: Union[Unset, None, GetTableUploadCsvUrlMode] = GetTableUploadCsvUrlMode.NEW,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/tables/{table}/upload-csv-url".format(
        client.base_url, workspace=workspace, table=table
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_mode: Union[Unset, None, str] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value if mode else None

    params["mode"] = json_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PresignedUrl]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PresignedUrl.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[PresignedUrl]:
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
    mode: Union[Unset, None, GetTableUploadCsvUrlMode] = GetTableUploadCsvUrlMode.NEW,
) -> Response[PresignedUrl]:
    """Upload a CSV file into your table. This API endpoint returns a url, to which you can upload your csv
    file. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <csv-file> '<url>'.

    Args:
        workspace (str):
        table (str):
        mode (Union[Unset, None, GetTableUploadCsvUrlMode]):  Default:
            GetTableUploadCsvUrlMode.NEW.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PresignedUrl]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        client=client,
        mode=mode,
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
    mode: Union[Unset, None, GetTableUploadCsvUrlMode] = GetTableUploadCsvUrlMode.NEW,
) -> Optional[PresignedUrl]:
    """Upload a CSV file into your table. This API endpoint returns a url, to which you can upload your csv
    file. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <csv-file> '<url>'.

    Args:
        workspace (str):
        table (str):
        mode (Union[Unset, None, GetTableUploadCsvUrlMode]):  Default:
            GetTableUploadCsvUrlMode.NEW.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PresignedUrl]
    """

    return sync_detailed(
        workspace=workspace,
        table=table,
        client=client,
        mode=mode,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    mode: Union[Unset, None, GetTableUploadCsvUrlMode] = GetTableUploadCsvUrlMode.NEW,
) -> Response[PresignedUrl]:
    """Upload a CSV file into your table. This API endpoint returns a url, to which you can upload your csv
    file. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <csv-file> '<url>'.

    Args:
        workspace (str):
        table (str):
        mode (Union[Unset, None, GetTableUploadCsvUrlMode]):  Default:
            GetTableUploadCsvUrlMode.NEW.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PresignedUrl]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        table=table,
        client=client,
        mode=mode,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    table: str,
    *,
    client: AuthenticatedClient,
    mode: Union[Unset, None, GetTableUploadCsvUrlMode] = GetTableUploadCsvUrlMode.NEW,
) -> Optional[PresignedUrl]:
    """Upload a CSV file into your table. This API endpoint returns a url, to which you can upload your csv
    file. You can do a PUT request on the returned url, e.g.: curl -XPUT -T <csv-file> '<url>'.

    Args:
        workspace (str):
        table (str):
        mode (Union[Unset, None, GetTableUploadCsvUrlMode]):  Default:
            GetTableUploadCsvUrlMode.NEW.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PresignedUrl]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            table=table,
            client=client,
            mode=mode,
        )
    ).parsed
