from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.choice import Choice
from ...types import UNSET, Response


def _get_kwargs(
    workspace: str,
    choice_name: str,
    *,
    client: AuthenticatedClient,
    new_name: str,
) -> Dict[str, Any]:
    url = "{}/api/v1.0/workspaces/{workspace}/choices/{choiceName}/rename".format(
        client.base_url, workspace=workspace, choiceName=choice_name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["new-name"] = new_name

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
    new_name: str,
) -> Response[List["Choice"]]:
    """Rename a choice

     Renames a choice. It also renames its usage in the columnAttributes.

    Args:
        workspace (str):  Example: workspace-name.
        choice_name (str):
        new_name (str):

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
        new_name=new_name,
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
    new_name: str,
) -> Optional[List["Choice"]]:
    """Rename a choice

     Renames a choice. It also renames its usage in the columnAttributes.

    Args:
        workspace (str):  Example: workspace-name.
        choice_name (str):
        new_name (str):

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
        new_name=new_name,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    choice_name: str,
    *,
    client: AuthenticatedClient,
    new_name: str,
) -> Response[List["Choice"]]:
    """Rename a choice

     Renames a choice. It also renames its usage in the columnAttributes.

    Args:
        workspace (str):  Example: workspace-name.
        choice_name (str):
        new_name (str):

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
        new_name=new_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    choice_name: str,
    *,
    client: AuthenticatedClient,
    new_name: str,
) -> Optional[List["Choice"]]:
    """Rename a choice

     Renames a choice. It also renames its usage in the columnAttributes.

    Args:
        workspace (str):  Example: workspace-name.
        choice_name (str):
        new_name (str):

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
            new_name=new_name,
        )
    ).parsed
