from collections.abc import Mapping
import datetime
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sirene_api_client.api_types import UNSET, Unset
from sirene_api_client.models.dates_mise_a_jour_donnees_collection import (
    DatesMiseAJourDonneesCollection,
)

T = TypeVar("T", bound="DatesMiseAJourDonnees")


@_attrs_define
class DatesMiseAJourDonnees:
    """Dates des dernières mises à jour de chaque collection de données

    Attributes:
        collection (Union[Unset, DatesMiseAJourDonneesCollection]): Nom de la collection
        date_derniere_mise_a_disposition (Union[Unset, datetime.datetime]): Date et heure (yyyy-MM-ddTHH:mm:ss.SSS) de
            la dernière mise à disposition des données de la collection Example: 2025-05-10 15:18:50.255000.
        date_dernier_traitement_maximum (Union[Unset, datetime.datetime]): Date (yyyy-MM-ddTHH:mm:ss.SSS) correspondant
            à la date de validité des données consultées Example: 2025-05-10 15:18:50.255000.
        date_dernier_traitement_de_masse (Union[Unset, datetime.datetime]): Date (yyyy-MM-ddTHH:mm:ss.SSS) du dernier
            traitement de masse sur la collection. À cette date plusieurs centaines de milliers de documents ont pu être mis
            à jour. Il est conseillé de traiter cette date d'une manière spécifique Example: 2025-05-10 15:18:50.255000.
    """

    collection: Unset | DatesMiseAJourDonneesCollection = UNSET
    date_derniere_mise_a_disposition: Unset | datetime.datetime = UNSET
    date_dernier_traitement_maximum: Unset | datetime.datetime = UNSET
    date_dernier_traitement_de_masse: Unset | datetime.datetime = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection: Unset | str = UNSET
        if not isinstance(self.collection, Unset):
            collection = self.collection.value

        date_derniere_mise_a_disposition: Unset | str = UNSET
        if not isinstance(self.date_derniere_mise_a_disposition, Unset):
            date_derniere_mise_a_disposition = (
                self.date_derniere_mise_a_disposition.isoformat()
            )

        date_dernier_traitement_maximum: Unset | str = UNSET
        if not isinstance(self.date_dernier_traitement_maximum, Unset):
            date_dernier_traitement_maximum = (
                self.date_dernier_traitement_maximum.isoformat()
            )

        date_dernier_traitement_de_masse: Unset | str = UNSET
        if not isinstance(self.date_dernier_traitement_de_masse, Unset):
            date_dernier_traitement_de_masse = (
                self.date_dernier_traitement_de_masse.isoformat()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection is not UNSET:
            field_dict["collection"] = collection
        if date_derniere_mise_a_disposition is not UNSET:
            field_dict["dateDerniereMiseADisposition"] = (
                date_derniere_mise_a_disposition
            )
        if date_dernier_traitement_maximum is not UNSET:
            field_dict["dateDernierTraitementMaximum"] = date_dernier_traitement_maximum
        if date_dernier_traitement_de_masse is not UNSET:
            field_dict["dateDernierTraitementDeMasse"] = (
                date_dernier_traitement_de_masse
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _collection = d.pop("collection", UNSET)
        collection: Unset | DatesMiseAJourDonneesCollection
        if isinstance(_collection, Unset) or _collection is None:
            collection = UNSET
        else:
            collection = DatesMiseAJourDonneesCollection(_collection)

        _date_derniere_mise_a_disposition = d.pop("dateDerniereMiseADisposition", UNSET)
        date_derniere_mise_a_disposition: Unset | datetime.datetime
        if (
            isinstance(_date_derniere_mise_a_disposition, Unset)
            or _date_derniere_mise_a_disposition is None
        ):
            date_derniere_mise_a_disposition = UNSET
        else:
            date_derniere_mise_a_disposition = isoparse(
                _date_derniere_mise_a_disposition
            )

        _date_dernier_traitement_maximum = d.pop("dateDernierTraitementMaximum", UNSET)
        date_dernier_traitement_maximum: Unset | datetime.datetime
        if (
            isinstance(_date_dernier_traitement_maximum, Unset)
            or _date_dernier_traitement_maximum is None
        ):
            date_dernier_traitement_maximum = UNSET
        else:
            date_dernier_traitement_maximum = isoparse(_date_dernier_traitement_maximum)

        _date_dernier_traitement_de_masse = d.pop("dateDernierTraitementDeMasse", UNSET)
        date_dernier_traitement_de_masse: Unset | datetime.datetime
        if (
            isinstance(_date_dernier_traitement_de_masse, Unset)
            or _date_dernier_traitement_de_masse is None
        ):
            date_dernier_traitement_de_masse = UNSET
        else:
            date_dernier_traitement_de_masse = isoparse(
                _date_dernier_traitement_de_masse
            )

        dates_mise_a_jour_donnees = cls(
            collection=collection,
            date_derniere_mise_a_disposition=date_derniere_mise_a_disposition,
            date_dernier_traitement_maximum=date_dernier_traitement_maximum,
            date_dernier_traitement_de_masse=date_dernier_traitement_de_masse,
        )

        dates_mise_a_jour_donnees.additional_properties = d
        return dates_mise_a_jour_donnees

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
