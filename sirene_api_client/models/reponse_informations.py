from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset
from sirene_api_client.models.reponse_informations_etat_service import (
    ReponseInformationsEtatService,
)

if TYPE_CHECKING:
    from sirene_api_client.models.dates_mise_a_jour_donnees import DatesMiseAJourDonnees
    from sirene_api_client.models.etat_collection import EtatCollection
    from sirene_api_client.models.header import Header


T = TypeVar("T", bound="ReponseInformations")


@_attrs_define
class ReponseInformations:
    """Objet renvoyé en cas de requête demandant les informations sur le service

    Attributes:
        header (Union[Unset, Header]): Informations générales sur le résultat de la requête
        etat_service (Union[Unset, ReponseInformationsEtatService]): État actuel du service
        etats_des_services (Union[Unset, list['EtatCollection']]): Etats des services
        version_service (Union[Unset, str]): Numéro de la version
        journal_des_modifications (Union[Unset, str]): Historique des versions de l'API Sirene
        dates_dernieres_mises_a_jour_des_donnees (Union[Unset, list['DatesMiseAJourDonnees']]): Dates des dernières
            mises à jour de chaque collection de données
    """

    header: Union[Unset, "Header"] = UNSET
    etat_service: Unset | ReponseInformationsEtatService = UNSET
    etats_des_services: Unset | list["EtatCollection"] = UNSET
    version_service: Unset | str = UNSET
    journal_des_modifications: Unset | str = UNSET
    dates_dernieres_mises_a_jour_des_donnees: Unset | list["DatesMiseAJourDonnees"] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        header: Unset | dict[str, Any] = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        etat_service: Unset | str = UNSET
        if not isinstance(self.etat_service, Unset):
            etat_service = self.etat_service.value

        etats_des_services: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.etats_des_services, Unset):
            etats_des_services = []
            for etats_des_services_item_data in self.etats_des_services:
                etats_des_services_item = etats_des_services_item_data.to_dict()
                etats_des_services.append(etats_des_services_item)

        version_service = self.version_service

        journal_des_modifications = self.journal_des_modifications

        dates_dernieres_mises_a_jour_des_donnees: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.dates_dernieres_mises_a_jour_des_donnees, Unset):
            dates_dernieres_mises_a_jour_des_donnees = []
            for (
                dates_dernieres_mises_a_jour_des_donnees_item_data
            ) in self.dates_dernieres_mises_a_jour_des_donnees:
                dates_dernieres_mises_a_jour_des_donnees_item = (
                    dates_dernieres_mises_a_jour_des_donnees_item_data.to_dict()
                )
                dates_dernieres_mises_a_jour_des_donnees.append(
                    dates_dernieres_mises_a_jour_des_donnees_item
                )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if header is not UNSET:
            field_dict["header"] = header
        if etat_service is not UNSET:
            field_dict["etatService"] = etat_service
        if etats_des_services is not UNSET:
            field_dict["etatsDesServices"] = etats_des_services
        if version_service is not UNSET:
            field_dict["versionService"] = version_service
        if journal_des_modifications is not UNSET:
            field_dict["journalDesModifications"] = journal_des_modifications
        if dates_dernieres_mises_a_jour_des_donnees is not UNSET:
            field_dict["datesDernieresMisesAJourDesDonnees"] = (
                dates_dernieres_mises_a_jour_des_donnees
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from sirene_api_client.models.dates_mise_a_jour_donnees import (
            DatesMiseAJourDonnees,
        )
        from sirene_api_client.models.etat_collection import EtatCollection
        from sirene_api_client.models.header import Header

        d = dict(src_dict)
        _header = d.pop("header", UNSET)
        header: Unset | Header
        header = UNSET if isinstance(_header, Unset) else Header.from_dict(_header)

        _etat_service = d.pop("etatService", UNSET)
        etat_service: Unset | ReponseInformationsEtatService
        if isinstance(_etat_service, Unset):
            etat_service = UNSET
        else:
            etat_service = ReponseInformationsEtatService(_etat_service)

        etats_des_services = []
        _etats_des_services = d.pop("etatsDesServices", UNSET)
        for etats_des_services_item_data in _etats_des_services or []:
            etats_des_services_item = EtatCollection.from_dict(
                etats_des_services_item_data
            )

            etats_des_services.append(etats_des_services_item)

        version_service = d.pop("versionService", UNSET)

        journal_des_modifications = d.pop("journalDesModifications", UNSET)

        dates_dernieres_mises_a_jour_des_donnees = []
        _dates_dernieres_mises_a_jour_des_donnees = d.pop(
            "datesDernieresMisesAJourDesDonnees", UNSET
        )
        for dates_dernieres_mises_a_jour_des_donnees_item_data in (
            _dates_dernieres_mises_a_jour_des_donnees or []
        ):
            dates_dernieres_mises_a_jour_des_donnees_item = (
                DatesMiseAJourDonnees.from_dict(
                    dates_dernieres_mises_a_jour_des_donnees_item_data
                )
            )

            dates_dernieres_mises_a_jour_des_donnees.append(
                dates_dernieres_mises_a_jour_des_donnees_item
            )

        reponse_informations = cls(
            header=header,
            etat_service=etat_service,
            etats_des_services=etats_des_services,
            version_service=version_service,
            journal_des_modifications=journal_des_modifications,
            dates_dernieres_mises_a_jour_des_donnees=dates_dernieres_mises_a_jour_des_donnees,
        )

        reponse_informations.additional_properties = d
        return reponse_informations

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
