from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset

if TYPE_CHECKING:
    from sirene_api_client.models.header import Header
    from sirene_api_client.models.unite_legale import UniteLegale


T = TypeVar("T", bound="ReponseUniteLegale")


@_attrs_define
class ReponseUniteLegale:
    """Objet renvoyé en cas de succès sur une requête demandant un ou unité légale

    Attributes:
        header (Union[Unset, Header]): Informations générales sur le résultat de la requête
        unite_legale (Union[Unset, UniteLegale]):
    """

    header: Union[Unset, "Header"] = UNSET
    unite_legale: Union[Unset, "UniteLegale"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header: Unset | dict[str, Any] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        unite_legale: Unset | dict[str, Any] = UNSET
        if not isinstance(self.unite_legale, Unset):
            unite_legale = self.unite_legale.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header is not UNSET:
            field_dict["header"] = header
        if unite_legale is not UNSET:
            field_dict["uniteLegale"] = unite_legale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from sirene_api_client.models.header import Header
        from sirene_api_client.models.unite_legale import UniteLegale

        d = dict(src_dict)
        _header = d.pop("header", UNSET)
        header: Unset | Header
        header = UNSET if isinstance(_header, Unset) else Header.from_dict(_header)

        _unite_legale = d.pop("uniteLegale", UNSET)
        unite_legale: Unset | UniteLegale
        if isinstance(_unite_legale, Unset):
            unite_legale = UNSET
        else:
            unite_legale = UniteLegale.from_dict(_unite_legale)

        reponse_unite_legale = cls(
            header=header,
            unite_legale=unite_legale,
        )

        reponse_unite_legale.additional_properties = d
        return reponse_unite_legale

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
