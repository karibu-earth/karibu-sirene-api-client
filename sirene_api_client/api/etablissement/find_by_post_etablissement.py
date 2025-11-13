from http import HTTPStatus
from typing import Any, cast

import httpx

from sirene_api_client import errors
from sirene_api_client.api_types import Response
from sirene_api_client.client import AuthenticatedClient
from sirene_api_client.models.etablissement_post_multi_criteres import (
    EtablissementPostMultiCriteres,
)
from sirene_api_client.models.reponse_erreur import ReponseErreur
from sirene_api_client.models.reponse_etablissements import ReponseEtablissements


def _get_kwargs(
    *,
    body: EtablissementPostMultiCriteres,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/siret",
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Any | ReponseErreur | ReponseEtablissements | None:
    if response.status_code == 200:
        response_200 = ReponseEtablissements.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast("Any", None)
        return response_400

    if response.status_code == 401:
        response_401 = cast("Any", None)
        return response_401

    if response.status_code == 404:
        response_404 = ReponseErreur.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = cast("Any", None)
        return response_406

    if response.status_code == 414:
        response_414 = ReponseErreur.from_dict(response.json())

        return response_414

    if response.status_code == 429:
        response_429 = cast("Any", None)
        return response_429

    if response.status_code == 500:
        response_500 = ReponseErreur.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = ReponseErreur.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatusError(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Response[Any | ReponseErreur | ReponseEtablissements]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: EtablissementPostMultiCriteres,
) -> Response[Any | ReponseErreur | ReponseEtablissements]:
    """Recherche multicritère d'établissements

    Args:
        body (EtablissementPostMultiCriteres):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReponseErreur, ReponseEtablissements]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: EtablissementPostMultiCriteres,
) -> Any | ReponseErreur | ReponseEtablissements | None:
    """Recherche multicritère d'établissements

    Args:
        body (EtablissementPostMultiCriteres):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReponseErreur, ReponseEtablissements]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: EtablissementPostMultiCriteres,
) -> Response[Any | ReponseErreur | ReponseEtablissements]:
    """Recherche multicritère d'établissements

    Args:
        body (EtablissementPostMultiCriteres):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReponseErreur, ReponseEtablissements]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: EtablissementPostMultiCriteres,
) -> Any | ReponseErreur | ReponseEtablissements | None:
    """Recherche multicritère d'établissements

    Args:
        body (EtablissementPostMultiCriteres):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReponseErreur, ReponseEtablissements]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
