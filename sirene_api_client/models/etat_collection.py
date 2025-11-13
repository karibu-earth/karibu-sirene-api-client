from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset
from sirene_api_client.models.etat_collection_etat_collection import (
    EtatCollectionEtatCollection,
)

T = TypeVar("T", bound="EtatCollection")


@_attrs_define
class EtatCollection:
    """
    Attributes:
        collection (Union[Unset, str]): Collection
        etat_collection (Union[Unset, EtatCollectionEtatCollection]): Etat du service
    """

    collection: Unset | str = UNSET
    etat_collection: Unset | EtatCollectionEtatCollection = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection = self.collection

        etat_collection: Unset | str = UNSET
        if not isinstance(self.etat_collection, Unset):
            etat_collection = self.etat_collection.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection is not UNSET:
            field_dict["Collection"] = collection
        if etat_collection is not UNSET:
            field_dict["etatCollection"] = etat_collection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection = d.pop("Collection", UNSET)

        _etat_collection = d.pop("etatCollection", UNSET)
        etat_collection: Unset | EtatCollectionEtatCollection
        if isinstance(_etat_collection, Unset):
            etat_collection = UNSET
        else:
            etat_collection = EtatCollectionEtatCollection(_etat_collection)

        etat_collection_obj = cls(
            collection=collection,
            etat_collection=etat_collection,
        )

        etat_collection_obj.additional_properties = d
        return etat_collection_obj

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
