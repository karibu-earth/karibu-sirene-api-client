from http import HTTPStatus
from typing import Any

import httpx

from sirene_api_client import errors
from sirene_api_client.api_types import Response
from sirene_api_client.client import AuthenticatedClient
from sirene_api_client.models.reponse_erreur import ReponseErreur
from sirene_api_client.models.reponse_informations import ReponseInformations


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/informations",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> ReponseErreur | ReponseInformations | None:
    if response.status_code == 200:
        response_200 = ReponseInformations.from_dict(response.json())

        return response_200

    if response.status_code == 503:
        response_503 = ReponseErreur.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatusError(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Response[ReponseErreur | ReponseInformations]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ReponseErreur | ReponseInformations]:
    """État du service, dates de mise à jour et numéro de version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ReponseErreur, ReponseInformations]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ReponseErreur | ReponseInformations | None:
    """État du service, dates de mise à jour et numéro de version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReponseErreur, ReponseInformations]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ReponseErreur | ReponseInformations]:
    """État du service, dates de mise à jour et numéro de version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ReponseErreur, ReponseInformations]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ReponseErreur | ReponseInformations | None:
    """État du service, dates de mise à jour et numéro de version

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReponseErreur, ReponseInformations]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
