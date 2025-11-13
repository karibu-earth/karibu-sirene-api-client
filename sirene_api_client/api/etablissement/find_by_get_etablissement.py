from http import HTTPStatus
from typing import Any, cast

import httpx

from sirene_api_client import errors
from sirene_api_client.api_types import UNSET, Response, Unset
from sirene_api_client.client import AuthenticatedClient
from sirene_api_client.models.reponse_erreur import ReponseErreur
from sirene_api_client.models.reponse_etablissements import ReponseEtablissements


def _get_kwargs(
    *,
    q: Unset | str = UNSET,
    date: Unset | str = UNSET,
    champs: Unset | str = UNSET,
    masquer_valeurs_nulles: Unset | str = UNSET,
    facette_champ: Unset | str = UNSET,
    tri: Unset | str = UNSET,
    nombre: Unset | str = UNSET,
    debut: Unset | str = UNSET,
    curseur: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q

    params["date"] = date

    params["champs"] = champs

    params["masquerValeursNulles"] = masquer_valeurs_nulles

    params["facette.champ"] = facette_champ

    params["tri"] = tri

    params["nombre"] = nombre

    params["debut"] = debut

    params["curseur"] = curseur

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/siret",
        "params": params,
    }

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
        response_414 = cast("Any", None)
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
    q: Unset | str = UNSET,
    date: Unset | str = UNSET,
    champs: Unset | str = UNSET,
    masquer_valeurs_nulles: Unset | str = UNSET,
    facette_champ: Unset | str = UNSET,
    tri: Unset | str = UNSET,
    nombre: Unset | str = UNSET,
    debut: Unset | str = UNSET,
    curseur: Unset | str = UNSET,
) -> Response[Any | ReponseErreur | ReponseEtablissements]:
    """Recherche multicritère d'établissements

    Args:
        q (Union[Unset, str]):
        date (Union[Unset, str]):
        champs (Union[Unset, str]):
        masquer_valeurs_nulles (Union[Unset, str]):
        facette_champ (Union[Unset, str]):
        tri (Union[Unset, str]):
        nombre (Union[Unset, str]):
        debut (Union[Unset, str]):
        curseur (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReponseErreur, ReponseEtablissements]]
    """

    kwargs = _get_kwargs(
        q=q,
        date=date,
        champs=champs,
        masquer_valeurs_nulles=masquer_valeurs_nulles,
        facette_champ=facette_champ,
        tri=tri,
        nombre=nombre,
        debut=debut,
        curseur=curseur,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: Unset | str = UNSET,
    date: Unset | str = UNSET,
    champs: Unset | str = UNSET,
    masquer_valeurs_nulles: Unset | str = UNSET,
    facette_champ: Unset | str = UNSET,
    tri: Unset | str = UNSET,
    nombre: Unset | str = UNSET,
    debut: Unset | str = UNSET,
    curseur: Unset | str = UNSET,
) -> Any | ReponseErreur | ReponseEtablissements | None:
    """Recherche multicritère d'établissements

    Args:
        q (Union[Unset, str]):
        date (Union[Unset, str]):
        champs (Union[Unset, str]):
        masquer_valeurs_nulles (Union[Unset, str]):
        facette_champ (Union[Unset, str]):
        tri (Union[Unset, str]):
        nombre (Union[Unset, str]):
        debut (Union[Unset, str]):
        curseur (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReponseErreur, ReponseEtablissements]
    """

    return sync_detailed(
        client=client,
        q=q,
        date=date,
        champs=champs,
        masquer_valeurs_nulles=masquer_valeurs_nulles,
        facette_champ=facette_champ,
        tri=tri,
        nombre=nombre,
        debut=debut,
        curseur=curseur,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: Unset | str = UNSET,
    date: Unset | str = UNSET,
    champs: Unset | str = UNSET,
    masquer_valeurs_nulles: Unset | str = UNSET,
    facette_champ: Unset | str = UNSET,
    tri: Unset | str = UNSET,
    nombre: Unset | str = UNSET,
    debut: Unset | str = UNSET,
    curseur: Unset | str = UNSET,
) -> Response[Any | ReponseErreur | ReponseEtablissements]:
    """Recherche multicritère d'établissements

    Args:
        q (Union[Unset, str]):
        date (Union[Unset, str]):
        champs (Union[Unset, str]):
        masquer_valeurs_nulles (Union[Unset, str]):
        facette_champ (Union[Unset, str]):
        tri (Union[Unset, str]):
        nombre (Union[Unset, str]):
        debut (Union[Unset, str]):
        curseur (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ReponseErreur, ReponseEtablissements]]
    """

    kwargs = _get_kwargs(
        q=q,
        date=date,
        champs=champs,
        masquer_valeurs_nulles=masquer_valeurs_nulles,
        facette_champ=facette_champ,
        tri=tri,
        nombre=nombre,
        debut=debut,
        curseur=curseur,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: Unset | str = UNSET,
    date: Unset | str = UNSET,
    champs: Unset | str = UNSET,
    masquer_valeurs_nulles: Unset | str = UNSET,
    facette_champ: Unset | str = UNSET,
    tri: Unset | str = UNSET,
    nombre: Unset | str = UNSET,
    debut: Unset | str = UNSET,
    curseur: Unset | str = UNSET,
) -> Any | ReponseErreur | ReponseEtablissements | None:
    """Recherche multicritère d'établissements

    Args:
        q (Union[Unset, str]):
        date (Union[Unset, str]):
        champs (Union[Unset, str]):
        masquer_valeurs_nulles (Union[Unset, str]):
        facette_champ (Union[Unset, str]):
        tri (Union[Unset, str]):
        nombre (Union[Unset, str]):
        debut (Union[Unset, str]):
        curseur (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ReponseErreur, ReponseEtablissements]
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            date=date,
            champs=champs,
            masquer_valeurs_nulles=masquer_valeurs_nulles,
            facette_champ=facette_champ,
            tri=tri,
            nombre=nombre,
            debut=debut,
            curseur=curseur,
        )
    ).parsed
