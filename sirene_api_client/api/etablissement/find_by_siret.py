from http import HTTPStatus
from typing import Any, cast

import httpx

from sirene_api_client import errors
from sirene_api_client.api_types import UNSET, Response, Unset
from sirene_api_client.client import AuthenticatedClient
from sirene_api_client.models.reponse_erreur import ReponseErreur
from sirene_api_client.models.reponse_etablissement import ReponseEtablissement


def _get_kwargs(
    siret: str,
    *,
    date: Unset | str = UNSET,
    champs: Unset | str = UNSET,
    masquer_valeurs_nulles: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["date"] = date

    params["champs"] = champs

    params["masquerValeursNulles"] = masquer_valeurs_nulles

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/siret/{siret}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Any | ReponseErreur | ReponseEtablissement | None:
    if response.status_code == 200:
        response_200 = ReponseEtablissement.from_dict(response.json())

        return response_200

    if response.status_code == 301:
        response_301 = cast("Any", None)
        return response_301

    if response.status_code == 400:
        response_400 = cast("Any", None)
        return response_400

    if response.status_code == 401:
        response_401 = cast("Any", None)
        return response_401

    if response.status_code == 403:
        response_403 = cast("Any", None)
        return response_403

    if response.status_code == 404:
        response_404 = ReponseErreur.from_dict(response.json())

        return response_404

    if response.status_code == 406:
        response_406 = cast("Any", None)
        return response_406

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
) -> Response[Any | ReponseErreur | ReponseEtablissement]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    siret: str,
    *,
    client: AuthenticatedClient,
    date: Unset | str = UNSET,
    champs: Unset | str = UNSET,
    masquer_valeurs_nulles: Unset | str = UNSET,
) -> Response[Any | ReponseErreur | ReponseEtablissement]:
    """Recherche d'un établissement par son numéro Siret

     Recherche d'un établissement par son numéro Siret (14 chiffres)

    Args:
        siret (str):
        date (Union[Unset, str]):
        champs (Union[Unset, str]):
        masquer_valeurs_nulles (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReponseErreur, ReponseEtablissement]]
    """

    kwargs = _get_kwargs(
        siret=siret,
        date=date,
        champs=champs,
        masquer_valeurs_nulles=masquer_valeurs_nulles,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    siret: str,
    *,
    client: AuthenticatedClient,
    date: Unset | str = UNSET,
    champs: Unset | str = UNSET,
    masquer_valeurs_nulles: Unset | str = UNSET,
) -> Any | ReponseErreur | ReponseEtablissement | None:
    """Recherche d'un établissement par son numéro Siret

     Recherche d'un établissement par son numéro Siret (14 chiffres)

    Args:
        siret (str):
        date (Union[Unset, str]):
        champs (Union[Unset, str]):
        masquer_valeurs_nulles (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReponseErreur, ReponseEtablissement]
    """

    return sync_detailed(
        siret=siret,
        client=client,
        date=date,
        champs=champs,
        masquer_valeurs_nulles=masquer_valeurs_nulles,
    ).parsed


async def asyncio_detailed(
    siret: str,
    *,
    client: AuthenticatedClient,
    date: Unset | str = UNSET,
    champs: Unset | str = UNSET,
    masquer_valeurs_nulles: Unset | str = UNSET,
) -> Response[Any | ReponseErreur | ReponseEtablissement]:
    """Recherche d'un établissement par son numéro Siret

     Recherche d'un établissement par son numéro Siret (14 chiffres)

    Args:
        siret (str):
        date (Union[Unset, str]):
        champs (Union[Unset, str]):
        masquer_valeurs_nulles (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReponseErreur, ReponseEtablissement]]
    """

    kwargs = _get_kwargs(
        siret=siret,
        date=date,
        champs=champs,
        masquer_valeurs_nulles=masquer_valeurs_nulles,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    siret: str,
    *,
    client: AuthenticatedClient,
    date: Unset | str = UNSET,
    champs: Unset | str = UNSET,
    masquer_valeurs_nulles: Unset | str = UNSET,
) -> Any | ReponseErreur | ReponseEtablissement | None:
    """Recherche d'un établissement par son numéro Siret

     Recherche d'un établissement par son numéro Siret (14 chiffres)

    Args:
        siret (str):
        date (Union[Unset, str]):
        champs (Union[Unset, str]):
        masquer_valeurs_nulles (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReponseErreur, ReponseEtablissement]
    """

    return (
        await asyncio_detailed(
            siret=siret,
            client=client,
            date=date,
            champs=champs,
            masquer_valeurs_nulles=masquer_valeurs_nulles,
        )
    ).parsed
