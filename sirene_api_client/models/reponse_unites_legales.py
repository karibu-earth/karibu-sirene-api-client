from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset

if TYPE_CHECKING:
    from sirene_api_client.models.facette import Facette
    from sirene_api_client.models.header import Header
    from sirene_api_client.models.unite_legale import UniteLegale


T = TypeVar("T", bound="ReponseUnitesLegales")


@_attrs_define
class ReponseUnitesLegales:
    """Objet renvoyé en cas de succès sur une requête demandant des unités légales

    Attributes:
        header (Union[Unset, Header]): Informations générales sur le résultat de la requête
        unites_legales (Union[Unset, list['UniteLegale']]):
        facettes (Union[Unset, list['Facette']]):
    """

    header: Union[Unset, "Header"] = UNSET
    unites_legales: Unset | list["UniteLegale"] = UNSET
    facettes: Unset | list["Facette"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header: Unset | dict[str, Any] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        unites_legales: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.unites_legales, Unset):
            unites_legales = []
            for unites_legales_item_data in self.unites_legales:
                unites_legales_item = unites_legales_item_data.to_dict()
                unites_legales.append(unites_legales_item)

        facettes: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.facettes, Unset):
            facettes = []
            for facettes_item_data in self.facettes:
                facettes_item = facettes_item_data.to_dict()
                facettes.append(facettes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header is not UNSET:
            field_dict["header"] = header
        if unites_legales is not UNSET:
            field_dict["unitesLegales"] = unites_legales
        if facettes is not UNSET:
            field_dict["facettes"] = facettes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from sirene_api_client.models.facette import Facette
        from sirene_api_client.models.header import Header
        from sirene_api_client.models.unite_legale import UniteLegale

        d = dict(src_dict)
        _header = d.pop("header", UNSET)
        header: Unset | Header
        header = UNSET if isinstance(_header, Unset) else Header.from_dict(_header)

        unites_legales = []
        _unites_legales = d.pop("unitesLegales", UNSET)
        for unites_legales_item_data in _unites_legales or []:
            unites_legales_item = UniteLegale.from_dict(unites_legales_item_data)

            unites_legales.append(unites_legales_item)

        facettes = []
        _facettes = d.pop("facettes", UNSET)
        for facettes_item_data in _facettes or []:
            facettes_item = Facette.from_dict(facettes_item_data)

            facettes.append(facettes_item)

        reponse_unites_legales = cls(
            header=header,
            unites_legales=unites_legales,
            facettes=facettes,
        )

        reponse_unites_legales.additional_properties = d
        return reponse_unites_legales

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
