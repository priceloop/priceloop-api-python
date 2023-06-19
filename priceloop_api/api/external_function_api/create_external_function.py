from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_external_function_param_type_item import CreateExternalFunctionParamTypeItem
from ...models.create_external_function_return_type import CreateExternalFunctionReturnType
from ...models.external_function_runtime import ExternalFunctionRuntime
from ...models.presigned_url import PresignedUrl
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
    runtime: ExternalFunctionRuntime,
    return_type: CreateExternalFunctionReturnType,
    param_type: Union[Unset, None, List[CreateExternalFunctionParamTypeItem]] = UNSET,
    batch_size: Union[Unset, None, int] = 300,
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
            json_param_type = []
            for param_type_item_data in param_type:
                param_type_item = param_type_item_data.value

                json_param_type.append(param_type_item)

    params["paramType"] = json_param_type

    params["batchSize"] = batch_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
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
    runtime: ExternalFunctionRuntime,
    return_type: CreateExternalFunctionReturnType,
    param_type: Union[Unset, None, List[CreateExternalFunctionParamTypeItem]] = UNSET,
    batch_size: Union[Unset, None, int] = 300,
) -> Response[PresignedUrl]:
    """Create a new external function

     Create external functions, specifying the function name, runtime, return type and the paremeter
    types. This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):  Example: function-name.
        runtime (ExternalFunctionRuntime):
        return_type (CreateExternalFunctionReturnType):
        param_type (Union[Unset, None, List[CreateExternalFunctionParamTypeItem]]):
        batch_size (Union[Unset, None, int]):  Default: 300.

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
        batch_size=batch_size,
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
    runtime: ExternalFunctionRuntime,
    return_type: CreateExternalFunctionReturnType,
    param_type: Union[Unset, None, List[CreateExternalFunctionParamTypeItem]] = UNSET,
    batch_size: Union[Unset, None, int] = 300,
) -> Optional[PresignedUrl]:
    """Create a new external function

     Create external functions, specifying the function name, runtime, return type and the paremeter
    types. This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):  Example: function-name.
        runtime (ExternalFunctionRuntime):
        return_type (CreateExternalFunctionReturnType):
        param_type (Union[Unset, None, List[CreateExternalFunctionParamTypeItem]]):
        batch_size (Union[Unset, None, int]):  Default: 300.

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
        runtime=runtime,
        return_type=return_type,
        param_type=param_type,
        batch_size=batch_size,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
    runtime: ExternalFunctionRuntime,
    return_type: CreateExternalFunctionReturnType,
    param_type: Union[Unset, None, List[CreateExternalFunctionParamTypeItem]] = UNSET,
    batch_size: Union[Unset, None, int] = 300,
) -> Response[PresignedUrl]:
    """Create a new external function

     Create external functions, specifying the function name, runtime, return type and the paremeter
    types. This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):  Example: function-name.
        runtime (ExternalFunctionRuntime):
        return_type (CreateExternalFunctionReturnType):
        param_type (Union[Unset, None, List[CreateExternalFunctionParamTypeItem]]):
        batch_size (Union[Unset, None, int]):  Default: 300.

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
        batch_size=batch_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
    runtime: ExternalFunctionRuntime,
    return_type: CreateExternalFunctionReturnType,
    param_type: Union[Unset, None, List[CreateExternalFunctionParamTypeItem]] = UNSET,
    batch_size: Union[Unset, None, int] = 300,
) -> Optional[PresignedUrl]:
    """Create a new external function

     Create external functions, specifying the function name, runtime, return type and the paremeter
    types. This API endpoint returns a url, to which you can upload your function code. You can do a PUT
    request on the returned url, e.g.: curl -XPUT -T <zip-file> '<url>'.

    Args:
        workspace (str):
        function (str):  Example: function-name.
        runtime (ExternalFunctionRuntime):
        return_type (CreateExternalFunctionReturnType):
        param_type (Union[Unset, None, List[CreateExternalFunctionParamTypeItem]]):
        batch_size (Union[Unset, None, int]):  Default: 300.

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
            runtime=runtime,
            return_type=return_type,
            param_type=param_type,
            batch_size=batch_size,
        )
    ).parsed
