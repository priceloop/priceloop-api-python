from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.export_info import ExportInfo
from ...types import Response


def _get_kwargs(
    workspace: str,
    export_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/exports/{exportJobId}".format(
        client.base_url, workspace=workspace, exportJobId=export_job_id
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[ExportInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ExportInfo.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[ExportInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    export_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ExportInfo]:
    """Get a table export with download url

     This API endpoint returns information about an export and a url, from which you can download the
    exported csv file. This download url will be valid for up to `.expiresInSeconds` seconds. You can
    always request a new download if the old one expires.

    Args:
        workspace (str):  Example: workspace-name.
        export_job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportInfo]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        export_job_id=export_job_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    export_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[ExportInfo]:
    """Get a table export with download url

     This API endpoint returns information about an export and a url, from which you can download the
    exported csv file. This download url will be valid for up to `.expiresInSeconds` seconds. You can
    always request a new download if the old one expires.

    Args:
        workspace (str):  Example: workspace-name.
        export_job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportInfo
    """

    return sync_detailed(
        workspace=workspace,
        export_job_id=export_job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    export_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[ExportInfo]:
    """Get a table export with download url

     This API endpoint returns information about an export and a url, from which you can download the
    exported csv file. This download url will be valid for up to `.expiresInSeconds` seconds. You can
    always request a new download if the old one expires.

    Args:
        workspace (str):  Example: workspace-name.
        export_job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExportInfo]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        export_job_id=export_job_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    export_job_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[ExportInfo]:
    """Get a table export with download url

     This API endpoint returns information about an export and a url, from which you can download the
    exported csv file. This download url will be valid for up to `.expiresInSeconds` seconds. You can
    always request a new download if the old one expires.

    Args:
        workspace (str):  Example: workspace-name.
        export_job_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExportInfo
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            export_job_id=export_job_id,
            client=client,
        )
    ).parsed
