from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_workspace_membership_response_200 import DeleteWorkspaceMembershipResponse200
from ...types import Response


def _get_kwargs(
    workspace: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/members/{userId}".format(
        client.base_url, workspace=workspace, userId=user_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[DeleteWorkspaceMembershipResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteWorkspaceMembershipResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[DeleteWorkspaceMembershipResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteWorkspaceMembershipResponse200]:
    """Delete a workspace membership

    Args:
        workspace (str):  Example: workspace-name.
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkspaceMembershipResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        user_id=user_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DeleteWorkspaceMembershipResponse200]:
    """Delete a workspace membership

    Args:
        workspace (str):  Example: workspace-name.
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkspaceMembershipResponse200
    """

    return sync_detailed(
        workspace=workspace,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[DeleteWorkspaceMembershipResponse200]:
    """Delete a workspace membership

    Args:
        workspace (str):  Example: workspace-name.
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWorkspaceMembershipResponse200]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[DeleteWorkspaceMembershipResponse200]:
    """Delete a workspace membership

    Args:
        workspace (str):  Example: workspace-name.
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWorkspaceMembershipResponse200
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            user_id=user_id,
            client=client,
        )
    ).parsed
