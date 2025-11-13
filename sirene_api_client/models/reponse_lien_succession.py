from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset

if TYPE_CHECKING:
    from sirene_api_client.models.header import Header
    from sirene_api_client.models.lien_succession import LienSuccession


T = TypeVar("T", bound="ReponseLienSuccession")


@_attrs_define
class ReponseLienSuccession:
    """Objet renvoyé en cas de succès sur une requête demandant les prédécesseurs d'un établissement

    Attributes:
        header (Union[Unset, Header]): Informations générales sur le résultat de la requête
        liens_succession (Union[Unset, list['LienSuccession']]):
    """

    header: Union[Unset, "Header"] = UNSET
    liens_succession: Unset | list["LienSuccession"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header: Unset | dict[str, Any] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        liens_succession: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.liens_succession, Unset):
            liens_succession = []
            for liens_succession_item_data in self.liens_succession:
                liens_succession_item = liens_succession_item_data.to_dict()
                liens_succession.append(liens_succession_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header is not UNSET:
            field_dict["header"] = header
        if liens_succession is not UNSET:
            field_dict["liensSuccession"] = liens_succession

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from sirene_api_client.models.header import Header
        from sirene_api_client.models.lien_succession import LienSuccession

        d = dict(src_dict)
        _header = d.pop("header", UNSET)
        header: Unset | Header
        header = UNSET if isinstance(_header, Unset) else Header.from_dict(_header)

        liens_succession = []
        _liens_succession = d.pop("liensSuccession", UNSET)
        for liens_succession_item_data in _liens_succession or []:
            liens_succession_item = LienSuccession.from_dict(liens_succession_item_data)

            liens_succession.append(liens_succession_item)

        reponse_lien_succession = cls(
            header=header,
            liens_succession=liens_succession,
        )

        reponse_lien_succession.additional_properties = d
        return reponse_lien_succession

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
