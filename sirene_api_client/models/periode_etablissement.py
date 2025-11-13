from collections.abc import Mapping
import datetime
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sirene_api_client.api_types import UNSET, Unset
from sirene_api_client.models.periode_etablissement_nomenclature_activite_principale_etablissement import (
    PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement,
)

T = TypeVar("T", bound="PeriodeEtablissement")


@_attrs_define
class PeriodeEtablissement:
    """Ensemble des variables historisées de l'établissement entre dateDebut et dateFin

    Attributes:
        date_fin (Union[Unset, datetime.date]): Date de fin de la période, null pour la dernière période, format AAAA-
            MM-DD
        date_debut (Union[Unset, datetime.date]): Date de début de la période, format AAAA-MM-DD
        etat_administratif_etablissement (Union[Unset, str]): État administratif de l'établissement pendant la période
            (A= établissement actif; F= établissement fermé)
        changement_etat_administratif_etablissement (Union[Unset, bool]): Indicatrice de changement de l'état
            administratif de l'établissement par rapport à la période précédente
        enseigne_1_etablissement (Union[Unset, str]): Première ligne d'enseigne
        enseigne_2_etablissement (Union[Unset, str]): Deuxième ligne d'enseigne
        enseigne_3_etablissement (Union[Unset, str]): Troisième ligne d'enseigne
        changement_enseigne_etablissement (Union[Unset, bool]): Indicatrice de changement de l'enseigne de
            l'établissement par rapport à la période précédente (un seul indicateur pour les trois variables Enseigne1,
            Enseigne2 et Enseigne3). Un seul indicateur pour les trois variables enseigne
        denomination_usuelle_etablissement (Union[Unset, str]): Nom sous lequel l'activité de l'établissement est connu
            du public
        changement_denomination_usuelle_etablissement (Union[Unset, bool]): Indicatrice de changement de la dénomination
            usuelle de l'établissement par rapport à la période précédente
        activite_principale_etablissement (Union[Unset, str]): Activité principale de l'établissement pendant la période
            (l'APE est codifiée selon la <a href='https://www.insee.fr/fr/information/2406147'>nomenclature d'Activités
            Française (NAF)</a>
        nomenclature_activite_principale_etablissement (Union[Unset,
            PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement]): Nomenclature de l'activité, permet de savoir
            à partir de quelle nomenclature est codifiée ActivitePrincipaleEtablissement
        changement_activite_principale_etablissement (Union[Unset, bool]): Indicatrice de changement de l'activité
            principale de l'établissement par rapport à la période précédente
        caractere_employeur_etablissement (Union[Unset, str]): Caractère employeur de l'établissement (O=oui, N=non,
            null=sans objet)
        changement_caractere_employeur_etablissement (Union[Unset, bool]): Indicatrice de changement du caractère
            employeur de l'établissement par rapport à la période précédente
    """

    date_fin: Unset | datetime.date = UNSET
    date_debut: Unset | datetime.date = UNSET
    etat_administratif_etablissement: Unset | str = UNSET
    changement_etat_administratif_etablissement: Unset | bool = UNSET
    enseigne_1_etablissement: Unset | str = UNSET
    enseigne_2_etablissement: Unset | str = UNSET
    enseigne_3_etablissement: Unset | str = UNSET
    changement_enseigne_etablissement: Unset | bool = UNSET
    denomination_usuelle_etablissement: Unset | str = UNSET
    changement_denomination_usuelle_etablissement: Unset | bool = UNSET
    activite_principale_etablissement: Unset | str = UNSET
    nomenclature_activite_principale_etablissement: (
        Unset | PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement
    ) = UNSET
    changement_activite_principale_etablissement: Unset | bool = UNSET
    caractere_employeur_etablissement: Unset | str = UNSET
    changement_caractere_employeur_etablissement: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_fin: Unset | str = UNSET
        if not isinstance(self.date_fin, Unset):
            date_fin = self.date_fin.isoformat()

        date_debut: Unset | str = UNSET
        if not isinstance(self.date_debut, Unset):
            date_debut = self.date_debut.isoformat()

        etat_administratif_etablissement = self.etat_administratif_etablissement

        changement_etat_administratif_etablissement = (
            self.changement_etat_administratif_etablissement
        )

        enseigne_1_etablissement = self.enseigne_1_etablissement

        enseigne_2_etablissement = self.enseigne_2_etablissement

        enseigne_3_etablissement = self.enseigne_3_etablissement

        changement_enseigne_etablissement = self.changement_enseigne_etablissement

        denomination_usuelle_etablissement = self.denomination_usuelle_etablissement

        changement_denomination_usuelle_etablissement = (
            self.changement_denomination_usuelle_etablissement
        )

        activite_principale_etablissement = self.activite_principale_etablissement

        nomenclature_activite_principale_etablissement: Unset | str = UNSET
        if not isinstance(self.nomenclature_activite_principale_etablissement, Unset):
            nomenclature_activite_principale_etablissement = (
                self.nomenclature_activite_principale_etablissement.value
            )

        changement_activite_principale_etablissement = (
            self.changement_activite_principale_etablissement
        )

        caractere_employeur_etablissement = self.caractere_employeur_etablissement

        changement_caractere_employeur_etablissement = (
            self.changement_caractere_employeur_etablissement
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_fin is not UNSET:
            field_dict["dateFin"] = date_fin
        if date_debut is not UNSET:
            field_dict["dateDebut"] = date_debut
        if etat_administratif_etablissement is not UNSET:
            field_dict["etatAdministratifEtablissement"] = (
                etat_administratif_etablissement
            )
        if changement_etat_administratif_etablissement is not UNSET:
            field_dict["changementEtatAdministratifEtablissement"] = (
                changement_etat_administratif_etablissement
            )
        if enseigne_1_etablissement is not UNSET:
            field_dict["enseigne1Etablissement"] = enseigne_1_etablissement
        if enseigne_2_etablissement is not UNSET:
            field_dict["enseigne2Etablissement"] = enseigne_2_etablissement
        if enseigne_3_etablissement is not UNSET:
            field_dict["enseigne3Etablissement"] = enseigne_3_etablissement
        if changement_enseigne_etablissement is not UNSET:
            field_dict["changementEnseigneEtablissement"] = (
                changement_enseigne_etablissement
            )
        if denomination_usuelle_etablissement is not UNSET:
            field_dict["denominationUsuelleEtablissement"] = (
                denomination_usuelle_etablissement
            )
        if changement_denomination_usuelle_etablissement is not UNSET:
            field_dict["changementDenominationUsuelleEtablissement"] = (
                changement_denomination_usuelle_etablissement
            )
        if activite_principale_etablissement is not UNSET:
            field_dict["activitePrincipaleEtablissement"] = (
                activite_principale_etablissement
            )
        if nomenclature_activite_principale_etablissement is not UNSET:
            field_dict["nomenclatureActivitePrincipaleEtablissement"] = (
                nomenclature_activite_principale_etablissement
            )
        if changement_activite_principale_etablissement is not UNSET:
            field_dict["changementActivitePrincipaleEtablissement"] = (
                changement_activite_principale_etablissement
            )
        if caractere_employeur_etablissement is not UNSET:
            field_dict["caractereEmployeurEtablissement"] = (
                caractere_employeur_etablissement
            )
        if changement_caractere_employeur_etablissement is not UNSET:
            field_dict["changementCaractereEmployeurEtablissement"] = (
                changement_caractere_employeur_etablissement
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date_fin = d.pop("dateFin", UNSET)
        date_fin: Unset | datetime.date
        date_fin = (
            UNSET
            if isinstance(_date_fin, Unset) or _date_fin is None
            else isoparse(_date_fin).date()
        )

        _date_debut = d.pop("dateDebut", UNSET)
        date_debut: Unset | datetime.date
        if isinstance(_date_debut, Unset) or _date_debut is None:
            date_debut = UNSET
        else:
            date_debut = isoparse(_date_debut).date()

        etat_administratif_etablissement = d.pop(
            "etatAdministratifEtablissement", UNSET
        )

        changement_etat_administratif_etablissement = d.pop(
            "changementEtatAdministratifEtablissement", UNSET
        )

        enseigne_1_etablissement = d.pop("enseigne1Etablissement", UNSET)

        enseigne_2_etablissement = d.pop("enseigne2Etablissement", UNSET)

        enseigne_3_etablissement = d.pop("enseigne3Etablissement", UNSET)

        changement_enseigne_etablissement = d.pop(
            "changementEnseigneEtablissement", UNSET
        )

        denomination_usuelle_etablissement = d.pop(
            "denominationUsuelleEtablissement", UNSET
        )

        changement_denomination_usuelle_etablissement = d.pop(
            "changementDenominationUsuelleEtablissement", UNSET
        )

        activite_principale_etablissement = d.pop(
            "activitePrincipaleEtablissement", UNSET
        )

        _nomenclature_activite_principale_etablissement = d.pop(
            "nomenclatureActivitePrincipaleEtablissement", UNSET
        )
        nomenclature_activite_principale_etablissement: (
            Unset | PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement
        )
        if (
            isinstance(_nomenclature_activite_principale_etablissement, Unset)
            or _nomenclature_activite_principale_etablissement is None
        ):
            nomenclature_activite_principale_etablissement = UNSET
        else:
            nomenclature_activite_principale_etablissement = (
                PeriodeEtablissementNomenclatureActivitePrincipaleEtablissement(
                    _nomenclature_activite_principale_etablissement
                )
            )

        changement_activite_principale_etablissement = d.pop(
            "changementActivitePrincipaleEtablissement", UNSET
        )

        caractere_employeur_etablissement = d.pop(
            "caractereEmployeurEtablissement", UNSET
        )

        changement_caractere_employeur_etablissement = d.pop(
            "changementCaractereEmployeurEtablissement", UNSET
        )

        periode_etablissement = cls(
            date_fin=date_fin,
            date_debut=date_debut,
            etat_administratif_etablissement=etat_administratif_etablissement,
            changement_etat_administratif_etablissement=changement_etat_administratif_etablissement,
            enseigne_1_etablissement=enseigne_1_etablissement,
            enseigne_2_etablissement=enseigne_2_etablissement,
            enseigne_3_etablissement=enseigne_3_etablissement,
            changement_enseigne_etablissement=changement_enseigne_etablissement,
            denomination_usuelle_etablissement=denomination_usuelle_etablissement,
            changement_denomination_usuelle_etablissement=changement_denomination_usuelle_etablissement,
            activite_principale_etablissement=activite_principale_etablissement,
            nomenclature_activite_principale_etablissement=nomenclature_activite_principale_etablissement,
            changement_activite_principale_etablissement=changement_activite_principale_etablissement,
            caractere_employeur_etablissement=caractere_employeur_etablissement,
            changement_caractere_employeur_etablissement=changement_caractere_employeur_etablissement,
        )

        periode_etablissement.additional_properties = d
        return periode_etablissement

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
