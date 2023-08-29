from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_external_function_http_param_type_item import CreateExternalFunctionHttpParamTypeItem
from ...models.create_external_function_http_return_type import CreateExternalFunctionHttpReturnType
from ...models.http_endpoint import HttpEndpoint
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
    json_body: HttpEndpoint,
    return_type: CreateExternalFunctionHttpReturnType,
    param_type: Union[Unset, None, List[CreateExternalFunctionHttpParamTypeItem]] = UNSET,
    batch_size: Union[Unset, None, int] = 300,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/external-functions/{function}/http".format(
        client.base_url, workspace=workspace, function=function
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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

    json_json_body = json_body.to_dict()

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
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
    json_body: HttpEndpoint,
    return_type: CreateExternalFunctionHttpReturnType,
    param_type: Union[Unset, None, List[CreateExternalFunctionHttpParamTypeItem]] = UNSET,
    batch_size: Union[Unset, None, int] = 300,
) -> Response[Any]:
    """Create a new external function (HTTP Endpoint)

     Create external functions, specifying the function name, return type and the parameter types. You
    just need to provide an HTTP endpoint to which external function requests will be sent. You also
    need to provide a secret - it will be used to sign requests from our platform. This hash signature
    is included with the headers of each request as `x-nocode-signature-256`. You should calculate a
    hash using your secret, and ensure that the result matches the hash from our platform. We use an
    HMAC-SHA256 hex digest to compute the hash.

    Args:
        workspace (str):
        function (str):  Example: function-name.
        return_type (CreateExternalFunctionHttpReturnType):
        param_type (Union[Unset, None, List[CreateExternalFunctionHttpParamTypeItem]]):
        batch_size (Union[Unset, None, int]):  Default: 300.
        json_body (HttpEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        function=function,
        client=client,
        json_body=json_body,
        return_type=return_type,
        param_type=param_type,
        batch_size=batch_size,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    workspace: str,
    function: str,
    *,
    client: AuthenticatedClient,
    json_body: HttpEndpoint,
    return_type: CreateExternalFunctionHttpReturnType,
    param_type: Union[Unset, None, List[CreateExternalFunctionHttpParamTypeItem]] = UNSET,
    batch_size: Union[Unset, None, int] = 300,
) -> Response[Any]:
    """Create a new external function (HTTP Endpoint)

     Create external functions, specifying the function name, return type and the parameter types. You
    just need to provide an HTTP endpoint to which external function requests will be sent. You also
    need to provide a secret - it will be used to sign requests from our platform. This hash signature
    is included with the headers of each request as `x-nocode-signature-256`. You should calculate a
    hash using your secret, and ensure that the result matches the hash from our platform. We use an
    HMAC-SHA256 hex digest to compute the hash.

    Args:
        workspace (str):
        function (str):  Example: function-name.
        return_type (CreateExternalFunctionHttpReturnType):
        param_type (Union[Unset, None, List[CreateExternalFunctionHttpParamTypeItem]]):
        batch_size (Union[Unset, None, int]):  Default: 300.
        json_body (HttpEndpoint):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        function=function,
        client=client,
        json_body=json_body,
        return_type=return_type,
        param_type=param_type,
        batch_size=batch_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
