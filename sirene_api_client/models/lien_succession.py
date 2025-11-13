from collections.abc import Mapping
import datetime
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sirene_api_client.api_types import UNSET, Unset

T = TypeVar("T", bound="LienSuccession")


@_attrs_define
class LienSuccession:
    """
    Attributes:
        siret_etablissement_predecesseur (Union[Unset, str]): Numéro Siret de l'établissement prédécesseur
        siret_etablissement_successeur (Union[Unset, str]): Numéro Siret de l'établissement successeur
        date_lien_succession (Union[Unset, datetime.date]): Date d'effet du lien de succession, au format AAAA-MM-JJ
        transfert_siege (Union[Unset, bool]): Indicatrice de transfert de siège
        continuite_economique (Union[Unset, bool]): Indicatrice de continuité économique entre les deux établissements
        date_dernier_traitement_lien_succession (Union[Unset, datetime.datetime]): Date de traitement du lien de
            succession, au format yyyy-MM-ddTHH:mm:ss.SSS Example: 2025-05-10 15:18:50.255000.
    """

    siret_etablissement_predecesseur: Unset | str = UNSET
    siret_etablissement_successeur: Unset | str = UNSET
    date_lien_succession: Unset | datetime.date = UNSET
    transfert_siege: Unset | bool = UNSET
    continuite_economique: Unset | bool = UNSET
    date_dernier_traitement_lien_succession: Unset | datetime.datetime = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        siret_etablissement_predecesseur = self.siret_etablissement_predecesseur

        siret_etablissement_successeur = self.siret_etablissement_successeur

        date_lien_succession: Unset | str = UNSET
        if not isinstance(self.date_lien_succession, Unset):
            date_lien_succession = self.date_lien_succession.isoformat()

        transfert_siege = self.transfert_siege

        continuite_economique = self.continuite_economique

        date_dernier_traitement_lien_succession: Unset | str = UNSET
        if not isinstance(self.date_dernier_traitement_lien_succession, Unset):
            date_dernier_traitement_lien_succession = (
                self.date_dernier_traitement_lien_succession.isoformat()
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if siret_etablissement_predecesseur is not UNSET:
            field_dict["siretEtablissementPredecesseur"] = (
                siret_etablissement_predecesseur
            )
        if siret_etablissement_successeur is not UNSET:
            field_dict["siretEtablissementSuccesseur"] = siret_etablissement_successeur
        if date_lien_succession is not UNSET:
            field_dict["dateLienSuccession"] = date_lien_succession
        if transfert_siege is not UNSET:
            field_dict["transfertSiege"] = transfert_siege
        if continuite_economique is not UNSET:
            field_dict["continuiteEconomique"] = continuite_economique
        if date_dernier_traitement_lien_succession is not UNSET:
            field_dict["dateDernierTraitementLienSuccession"] = (
                date_dernier_traitement_lien_succession
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        siret_etablissement_predecesseur = d.pop(
            "siretEtablissementPredecesseur", UNSET
        )

        siret_etablissement_successeur = d.pop("siretEtablissementSuccesseur", UNSET)

        _date_lien_succession = d.pop("dateLienSuccession", UNSET)
        date_lien_succession: Unset | datetime.date
        if isinstance(_date_lien_succession, Unset):
            date_lien_succession = UNSET
        else:
            date_lien_succession = isoparse(_date_lien_succession).date()

        transfert_siege = d.pop("transfertSiege", UNSET)

        continuite_economique = d.pop("continuiteEconomique", UNSET)

        _date_dernier_traitement_lien_succession = d.pop(
            "dateDernierTraitementLienSuccession", UNSET
        )
        date_dernier_traitement_lien_succession: Unset | datetime.datetime
        if isinstance(_date_dernier_traitement_lien_succession, Unset):
            date_dernier_traitement_lien_succession = UNSET
        else:
            date_dernier_traitement_lien_succession = isoparse(
                _date_dernier_traitement_lien_succession
            )

        lien_succession = cls(
            siret_etablissement_predecesseur=siret_etablissement_predecesseur,
            siret_etablissement_successeur=siret_etablissement_successeur,
            date_lien_succession=date_lien_succession,
            transfert_siege=transfert_siege,
            continuite_economique=continuite_economique,
            date_dernier_traitement_lien_succession=date_dernier_traitement_lien_succession,
        )

        lien_succession.additional_properties = d
        return lien_succession

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
