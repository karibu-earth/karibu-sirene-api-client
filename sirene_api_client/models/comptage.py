from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset

if TYPE_CHECKING:
    from sirene_api_client.models.comptage_valeur import ComptageValeur


T = TypeVar("T", bound="Comptage")


@_attrs_define
class Comptage:
    """Objet représentant un comptage particulier à l'intérieur d'une facette

    Attributes:
        valeur (Union[Unset, ComptageValeur]): Modalité comptée
        nombre (Union[Unset, int]): Nombre d'éléments correspondant à la modalité comptée
    """

    valeur: Union[Unset, "ComptageValeur"] = UNSET
    nombre: Unset | int = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valeur: Unset | dict[str, Any] = UNSET
        if not isinstance(self.valeur, Unset):
            valeur = self.valeur.to_dict()

        nombre = self.nombre

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if valeur is not UNSET:
            field_dict["valeur"] = valeur
        if nombre is not UNSET:
            field_dict["nombre"] = nombre

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from sirene_api_client.models.comptage_valeur import ComptageValeur

        d = dict(src_dict)
        _valeur = d.pop("valeur", UNSET)
        valeur: Unset | ComptageValeur
        if isinstance(_valeur, Unset):
            valeur = UNSET
        else:
            valeur = ComptageValeur.from_dict(_valeur)

        nombre = d.pop("nombre", UNSET)

        comptage = cls(
            valeur=valeur,
            nombre=nombre,
        )

        comptage.additional_properties = d
        return comptage

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
