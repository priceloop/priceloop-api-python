from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.choice import Choice
from ...types import Response


def _get_kwargs(
    workspace: str,
    choice_name: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/choices/{choiceName}".format(
        client.base_url, workspace=workspace, choiceName=choice_name
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["Choice"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Choice.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["Choice"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    choice_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["Choice"]]:
    """Delete a choice

     This also removes the assignment from all columns that use this choice.

    Args:
        workspace (str):  Example: workspace-name.
        choice_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Choice']]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        choice_name=choice_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    choice_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["Choice"]]:
    """Delete a choice

     This also removes the assignment from all columns that use this choice.

    Args:
        workspace (str):  Example: workspace-name.
        choice_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Choice']
    """

    return sync_detailed(
        workspace=workspace,
        choice_name=choice_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    choice_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[List["Choice"]]:
    """Delete a choice

     This also removes the assignment from all columns that use this choice.

    Args:
        workspace (str):  Example: workspace-name.
        choice_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Choice']]
    """

    kwargs = _get_kwargs(
        workspace=workspace,
        choice_name=choice_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    choice_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List["Choice"]]:
    """Delete a choice

     This also removes the assignment from all columns that use this choice.

    Args:
        workspace (str):  Example: workspace-name.
        choice_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Choice']
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            choice_name=choice_name,
            client=client,
        )
    ).parsed
