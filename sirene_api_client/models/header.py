from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset

T = TypeVar("T", bound="Header")


@_attrs_define
class Header:
    """Informations générales sur le résultat de la requête

    Attributes:
        statut (Union[Unset, int]): Égal au status de la réponse HTTP Example: 200.
        message (Union[Unset, str]): En cas d'erreur, message indiquant la cause de l'erreur. OK sinon Example: OK.
        total (Union[Unset, int]): Nombre total des éléments répondant à la requête
        debut (Union[Unset, int]): Numéro du premier élément fourni, défaut à 0, commence à 0
        nombre (Union[Unset, int]): Nombre d'éléments fournis, défaut à 20
        curseur (Union[Unset, str]): Curseur passé en argument dans la requête de l'utilisateur, utilisé pour la
            pagination profonde
        curseur_suivant (Union[Unset, str]): Curseur suivant pour accéder à la suite des résultat lorsqu'on utilise la
            pagination profonde
    """

    statut: Unset | int = UNSET
    message: Unset | str = UNSET
    total: Unset | int = UNSET
    debut: Unset | int = UNSET
    nombre: Unset | int = UNSET
    curseur: Unset | str = UNSET
    curseur_suivant: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statut = self.statut

        message = self.message

        total = self.total

        debut = self.debut

        nombre = self.nombre

        curseur = self.curseur

        curseur_suivant = self.curseur_suivant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if statut is not UNSET:
            field_dict["statut"] = statut
        if message is not UNSET:
            field_dict["message"] = message
        if total is not UNSET:
            field_dict["total"] = total
        if debut is not UNSET:
            field_dict["debut"] = debut
        if nombre is not UNSET:
            field_dict["nombre"] = nombre
        if curseur is not UNSET:
            field_dict["curseur"] = curseur
        if curseur_suivant is not UNSET:
            field_dict["curseurSuivant"] = curseur_suivant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        statut = d.pop("statut", UNSET)

        message = d.pop("message", UNSET)

        total = d.pop("total", UNSET)

        debut = d.pop("debut", UNSET)

        nombre = d.pop("nombre", UNSET)

        curseur = d.pop("curseur", UNSET)

        curseur_suivant = d.pop("curseurSuivant", UNSET)

        header = cls(
            statut=statut,
            message=message,
            total=total,
            debut=debut,
            nombre=nombre,
            curseur=curseur,
            curseur_suivant=curseur_suivant,
        )

        header.additional_properties = d
        return header

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
