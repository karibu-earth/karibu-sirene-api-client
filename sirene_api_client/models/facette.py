from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset

if TYPE_CHECKING:
    from sirene_api_client.models.comptage import Comptage


T = TypeVar("T", bound="Facette")


@_attrs_define
class Facette:
    """Objet représentant une facette (un ensemble de comptages selon un champ, une requête ou une série d'intervalles)

    Attributes:
        nom (Union[Unset, str]): Nom de la facette
        manquants (Union[Unset, int]): Nombre d'éléments pour lesquels la facette vaut null
        total (Union[Unset, int]): Nombre total d'éléments ayant une valeur non nulle pour la facette
        modalites (Union[Unset, int]): Nombre de valeurs distinctes pour la facette
        avant (Union[Unset, int]): Nombre d'éléments dont la valeur est inférieure au premier intervalle, uniquement
            pour les facettes de type intervalle
        apres (Union[Unset, int]): Nombre d'éléments dont la valeur est supérieure au dernier intervalle, uniquement
            pour les facettes de type intervalle
        entre (Union[Unset, int]): Nombre d'élements compris entre la borne inférieure du premier intervalle et la borne
            supérieure du dernier intervalle, uniquement pour les facettes de type intervalle
        comptages (Union[Unset, list['Comptage']]):
    """

    nom: Unset | str = UNSET
    manquants: Unset | int = UNSET
    total: Unset | int = UNSET
    modalites: Unset | int = UNSET
    avant: Unset | int = UNSET
    apres: Unset | int = UNSET
    entre: Unset | int = UNSET
    comptages: Unset | list["Comptage"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        nom = self.nom

        manquants = self.manquants

        total = self.total

        modalites = self.modalites

        avant = self.avant

        apres = self.apres

        entre = self.entre

        comptages: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.comptages, Unset):
            comptages = []
            for comptages_item_data in self.comptages:
                comptages_item = comptages_item_data.to_dict()
                comptages.append(comptages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nom is not UNSET:
            field_dict["nom"] = nom
        if manquants is not UNSET:
            field_dict["manquants"] = manquants
        if total is not UNSET:
            field_dict["total"] = total
        if modalites is not UNSET:
            field_dict["modalites"] = modalites
        if avant is not UNSET:
            field_dict["avant"] = avant
        if apres is not UNSET:
            field_dict["apres"] = apres
        if entre is not UNSET:
            field_dict["entre"] = entre
        if comptages is not UNSET:
            field_dict["comptages"] = comptages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from sirene_api_client.models.comptage import Comptage

        d = dict(src_dict)
        nom = d.pop("nom", UNSET)

        manquants = d.pop("manquants", UNSET)

        total = d.pop("total", UNSET)

        modalites = d.pop("modalites", UNSET)

        avant = d.pop("avant", UNSET)

        apres = d.pop("apres", UNSET)

        entre = d.pop("entre", UNSET)

        comptages = []
        _comptages = d.pop("comptages", UNSET)
        for comptages_item_data in _comptages or []:
            comptages_item = Comptage.from_dict(comptages_item_data)

            comptages.append(comptages_item)

        facette = cls(
            nom=nom,
            manquants=manquants,
            total=total,
            modalites=modalites,
            avant=avant,
            apres=apres,
            entre=entre,
            comptages=comptages,
        )

        facette.additional_properties = d
        return facette

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
