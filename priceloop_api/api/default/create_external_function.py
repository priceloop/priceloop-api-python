from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_external_function_return_type import CreateExternalFunctionReturnType
from ...models.create_external_function_runtime import CreateExternalFunctionRuntime
from ...models.presigned_url import PresignedUrl
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
    runtime: CreateExternalFunctionRuntime,
    return_type: CreateExternalFunctionReturnType,
    param_type: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/external-functions/{function}".format(
        client.base_url, workspace=workspace, function=function
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_runtime = runtime.value

    params["runtime"] = json_runtime

    json_return_type = return_type.value

    params["returnType"] = json_return_type

    json_param_type: Union[Unset, None, List[str]] = UNSET
    if not isinstance(param_type, Unset):
        if param_type is None:
            json_param_type = None
        else:
            json_param_type = param_type

    params["paramType"] = json_param_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
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
    function: str,
    *,
    client: AuthenticatedClient,
    runtime: CreateExternalFunctionRuntime,
    return_type: CreateExternalFunctionReturnType,
    param_type: Union[Unset, None, List[str]] = UNSET,
) -> Response[PresignedUrl]:
    """Create a new external function, specifying the function name, runtime, return type and the paremeter
    types. This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):
        runtime (CreateExternalFunctionRuntime):
        return_type (CreateExternalFunctionReturnType):
        param_type (Union[Unset, None, List[str]]):

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
        runtime=runtime,
        return_type=return_type,
        param_type=param_type,
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
    runtime: CreateExternalFunctionRuntime,
    return_type: CreateExternalFunctionReturnType,
    param_type: Union[Unset, None, List[str]] = UNSET,
) -> Optional[PresignedUrl]:
    """Create a new external function, specifying the function name, runtime, return type and the paremeter
    types. This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):
        runtime (CreateExternalFunctionRuntime):
        return_type (CreateExternalFunctionReturnType):
        param_type (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PresignedUrl]
    """

    return sync_detailed(
        workspace=workspace,
        function=function,
        client=client,
        runtime=runtime,
        return_type=return_type,
        param_type=param_type,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
    runtime: CreateExternalFunctionRuntime,
    return_type: CreateExternalFunctionReturnType,
    param_type: Union[Unset, None, List[str]] = UNSET,
) -> Response[PresignedUrl]:
    """Create a new external function, specifying the function name, runtime, return type and the paremeter
    types. This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):
        runtime (CreateExternalFunctionRuntime):
        return_type (CreateExternalFunctionReturnType):
        param_type (Union[Unset, None, List[str]]):

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
        runtime=runtime,
        return_type=return_type,
        param_type=param_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
    runtime: CreateExternalFunctionRuntime,
    return_type: CreateExternalFunctionReturnType,
    param_type: Union[Unset, None, List[str]] = UNSET,
) -> Optional[PresignedUrl]:
    """Create a new external function, specifying the function name, runtime, return type and the paremeter
    types. This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):
        runtime (CreateExternalFunctionRuntime):
        return_type (CreateExternalFunctionReturnType):
        param_type (Union[Unset, None, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PresignedUrl]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            function=function,
            client=client,
            runtime=runtime,
            return_type=return_type,
            param_type=param_type,
        )
    ).parsed
