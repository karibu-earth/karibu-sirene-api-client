from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset

if TYPE_CHECKING:
    from sirene_api_client.models.etablissement import Etablissement
    from sirene_api_client.models.facette import Facette
    from sirene_api_client.models.header import Header


T = TypeVar("T", bound="ReponseEtablissements")


@_attrs_define
class ReponseEtablissements:
    """Objet renvoyé en cas de succès sur une requête demandant des établissements

    Attributes:
        header (Union[Unset, Header]): Informations générales sur le résultat de la requête
        etablissements (Union[Unset, list['Etablissement']]):
        facettes (Union[Unset, list['Facette']]):
    """

    header: Union[Unset, "Header"] = UNSET
    etablissements: Unset | list["Etablissement"] = UNSET
    facettes: Unset | list["Facette"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header: Unset | dict[str, Any] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        etablissements: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.etablissements, Unset):
            etablissements = []
            for etablissements_item_data in self.etablissements:
                etablissements_item = etablissements_item_data.to_dict()
                etablissements.append(etablissements_item)

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
        if etablissements is not UNSET:
            field_dict["etablissements"] = etablissements
        if facettes is not UNSET:
            field_dict["facettes"] = facettes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from sirene_api_client.models.etablissement import Etablissement
        from sirene_api_client.models.facette import Facette
        from sirene_api_client.models.header import Header

        d = dict(src_dict)
        _header = d.pop("header", UNSET)
        header: Unset | Header
        header = UNSET if isinstance(_header, Unset) else Header.from_dict(_header)

        etablissements = []
        _etablissements = d.pop("etablissements", UNSET)
        for etablissements_item_data in _etablissements or []:
            etablissements_item = Etablissement.from_dict(etablissements_item_data)

            etablissements.append(etablissements_item)

        facettes = []
        _facettes = d.pop("facettes", UNSET)
        for facettes_item_data in _facettes or []:
            facettes_item = Facette.from_dict(facettes_item_data)

            facettes.append(facettes_item)

        reponse_etablissements = cls(
            header=header,
            etablissements=etablissements,
            facettes=facettes,
        )

        reponse_etablissements.additional_properties = d
        return reponse_etablissements

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
