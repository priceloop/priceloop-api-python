from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_plugin_table_role_assignment_body import ApiPluginTableRoleAssignmentBody
from ...types import Response


def _get_kwargs(
    workspace: str,
    plugin: str,
    name: str,
    *,
    client: AuthenticatedClient,
    json_body: ApiPluginTableRoleAssignmentBody,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/plugin/{plugin}/table-roles/{name}".format(
        client.base_url, workspace=workspace, plugin=plugin, name=name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
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
    name: str,
    *,
    client: AuthenticatedClient,
    json_body: ApiPluginTableRoleAssignmentBody,
) -> Response[Any]:
    """Assign a PluginTableRole to a table in a workspace

    Args:
        workspace (str):  Example: workspace-name.
        plugin (str):
        name (str):
        json_body (ApiPluginTableRoleAssignmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        plugin=plugin,
        name=name,
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
    name: str,
    *,
    client: AuthenticatedClient,
    json_body: ApiPluginTableRoleAssignmentBody,
) -> Response[Any]:
    """Assign a PluginTableRole to a table in a workspace

    Args:
        workspace (str):  Example: workspace-name.
        plugin (str):
        name (str):
        json_body (ApiPluginTableRoleAssignmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        plugin=plugin,
        name=name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)
