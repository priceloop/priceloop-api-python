from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.plugin_data_update_type_0 import PluginDataUpdateType0
from ...types import Response


def _get_kwargs(
    workspace: str,
    plugin: str,
    *,
    client: AuthenticatedClient,
    json_body: "PluginDataUpdateType0",
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/plugin/{plugin}/data".format(
        client.base_url, workspace=workspace, plugin=plugin
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body: Dict[str, Any]

    if isinstance(json_body, PluginDataUpdateType0):
        json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
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
    plugin: str,
    *,
    client: AuthenticatedClient,
    json_body: "PluginDataUpdateType0",
) -> Response[Any]:
    """Patch data of a plugin installation


    # Patch data

    This endpoint allows you to update some or all of the fields inside a plugin's data using a JSON
    merge-patch.

    ## JSON Merge-Patch

    In a JSON merge-patch, all fields are optional.
    Those fields that are present will set the value accordingly.
    A field that is explicitly set to `null` will reset the value to its default.
    This means that `null`-values hold semantic relevance, so make sure to leave out fields you do not
    want to change.

    More information on JSON merge-patches can be found in [RFC
    7396](https://datatracker.ietf.org/doc/html/rfc7396).


    Args:
        workspace (str):  Example: workspace-name.
        plugin (str):
        json_body ('PluginDataUpdateType0'):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        plugin=plugin,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    workspace: str,
    plugin: str,
    *,
    client: AuthenticatedClient,
    json_body: "PluginDataUpdateType0",
) -> Response[Any]:
    """Patch data of a plugin installation


    # Patch data

    This endpoint allows you to update some or all of the fields inside a plugin's data using a JSON
    merge-patch.

    ## JSON Merge-Patch

    In a JSON merge-patch, all fields are optional.
    Those fields that are present will set the value accordingly.
    A field that is explicitly set to `null` will reset the value to its default.
    This means that `null`-values hold semantic relevance, so make sure to leave out fields you do not
    want to change.

    More information on JSON merge-patches can be found in [RFC
    7396](https://datatracker.ietf.org/doc/html/rfc7396).


    Args:
        workspace (str):  Example: workspace-name.
        plugin (str):
        json_body ('PluginDataUpdateType0'):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        plugin=plugin,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
