from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset

if TYPE_CHECKING:
    from sirene_api_client.models.header import Header


T = TypeVar("T", bound="ReponseErreur")


@_attrs_define
class ReponseErreur:
    """
    Attributes:
        header (Union[Unset, Header]): Informations générales sur le résultat de la requête
    """

    header: Union[Unset, "Header"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header: Unset | dict[str, Any] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header is not UNSET:
            field_dict["header"] = header

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from sirene_api_client.models.header import Header

        d = dict(src_dict)
        _header = d.pop("header", UNSET)
        header: Unset | Header
        header = UNSET if isinstance(_header, Unset) else Header.from_dict(_header)

        reponse_erreur = cls(
            header=header,
        )

        reponse_erreur.additional_properties = d
        return reponse_erreur

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
