from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.presigned_url import PresignedUrl
from ...types import Response


def _get_kwargs(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/external-functions/{function}".format(
        client.base_url, workspace=workspace, function=function
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[PresignedUrl]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PresignedUrl.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
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
    function: str,
    *,
    client: AuthenticatedClient,
) -> Response[PresignedUrl]:
    """Update the code of an existing external function (Lambda)

     This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):  Example: function-name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PresignedUrl]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        function=function,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
) -> Optional[PresignedUrl]:
    """Update the code of an existing external function (Lambda)

     This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):  Example: function-name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PresignedUrl
    """

    return sync_detailed(
        workspace=workspace,
        function=function,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
) -> Response[PresignedUrl]:
    """Update the code of an existing external function (Lambda)

     This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):  Example: function-name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PresignedUrl]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        function=function,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
) -> Optional[PresignedUrl]:
    """Update the code of an existing external function (Lambda)

     This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):  Example: function-name.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PresignedUrl
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            function=function,
            client=client,
        )
    ).parsed
