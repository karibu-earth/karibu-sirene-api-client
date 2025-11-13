from collections.abc import Mapping
import datetime
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sirene_api_client.api_types import UNSET, Unset
from sirene_api_client.models.periode_unite_legale_caractere_employeur_unite_legale import (
    PeriodeUniteLegaleCaractereEmployeurUniteLegale,
)
from sirene_api_client.models.periode_unite_legale_etat_administratif_unite_legale import (
    PeriodeUniteLegaleEtatAdministratifUniteLegale,
)
from sirene_api_client.models.periode_unite_legale_nomenclature_activite_principale_unite_legale import (
    PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale,
)

T = TypeVar("T", bound="PeriodeUniteLegale")


@_attrs_define
class PeriodeUniteLegale:
    """
    Attributes:
        date_fin (Union[Unset, datetime.date]): Date de fin de la période, null pour la dernière période, format AAAA-
            MM-DD
        date_debut (Union[Unset, datetime.date]): Date de début de la période, format AAAA-MM-DD
        etat_administratif_unite_legale (Union[Unset, PeriodeUniteLegaleEtatAdministratifUniteLegale]): État de
            l'entreprise pendant la période (A= entreprise active, C= entreprise cessée)
        changement_etat_administratif_unite_legale (Union[Unset, bool]): Indicatrice de changement d'état par rapport à
            la période précédente
        nom_unite_legale (Union[Unset, str]): Nom de naissance pour les personnes physiques pour la période (null pour
            les personnes morales)
        changement_nom_unite_legale (Union[Unset, bool]): Indicatrice de changement du nom par rapport à la période
            précédente
        nom_usage_unite_legale (Union[Unset, str]): Nom d'usage pour les personnes physiques si celui-ci existe, null
            pour les personnes morales
        changement_nom_usage_unite_legale (Union[Unset, bool]): Indicatrice de changement du nom d'usage par rapport à
            la période précédente
        denomination_unite_legale (Union[Unset, str]): Raison sociale (personnes morales)
        changement_denomination_unite_legale (Union[Unset, bool]): Indicatrice de changement de la dénomination par
            rapport à la période précédente
        denomination_usuelle_1_unite_legale (Union[Unset, str]): Premier nom sous lequel l'entreprise est connue du
            public
        denomination_usuelle_2_unite_legale (Union[Unset, str]): Deuxième nom sous lequel l'entreprise est connue du
            public
        denomination_usuelle_3_unite_legale (Union[Unset, str]): Troisième nom sous lequel l'entreprise est connue du
            public
        categorie_juridique_unite_legale (Union[Unset, str]): Catégorie juridique de l'entreprise (variable Null pour
            les personnes physiques. (<a href='https://www.insee.fr/fr/information/2028129'>la nomenclature sur
            insee.fr</a>))
        changement_categorie_juridique_unite_legale (Union[Unset, bool]): Indicatrice de changement de la catégorie
            juridique par rapport à la période précédente
        activite_principale_unite_legale (Union[Unset, str]): Activité principale de l'entreprise pendant la période
            (l'APE est codifiée selon la <a href='https://www.insee.fr/fr/information/2406147'>nomenclature d'Activités
            Française (NAF)</a>
        nomenclature_activite_principale_unite_legale (Union[Unset,
            PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale]): Nomenclature de l'activité, permet de savoir à
            partir de quelle nomenclature est codifiée ActivitePrincipale
        changement_activite_principale_unite_legale (Union[Unset, bool]): Indicatrice de changement de l'activité
            principale par rapport à la période précédente
        nic_siege_unite_legale (Union[Unset, str]): Identifiant du siège pour la période (le Siret du siège est obtenu
            en concaténant le numéro Siren et le Nic)
        changement_nic_siege_unite_legale (Union[Unset, bool]): Indicatrice de changement du NIC du siège par rapport à
            la période précédente
        economie_sociale_solidaire_unite_legale (Union[Unset, str]): Appartenance de l'unité légale au champ de
            l'économie sociale et solidaire (ESS)
        changement_economie_sociale_solidaire_unite_legale (Union[Unset, bool]): Indicatrice de changement de l'ESS par
            rapport à la période précédente
        societe_mission_unite_legale (Union[Unset, str]): Appartenance de l'unité légale au champ société à mission (SM)
        changement_societe_mission_unite_legale (Union[Unset, bool]): Indicatrice de changement du champ société à
            mission par rapport à la période précédente
        caractere_employeur_unite_legale (Union[Unset, PeriodeUniteLegaleCaractereEmployeurUniteLegale]): Caractère
            employeur de l'entreprise. Valeur courante=O si au moins l'un des établissements actifs de l'unité légale
            emploie des salariés
        changement_caractere_employeur_unite_legale (Union[Unset, bool]): Indicatrice de changement du caractère
            employeur par rapport à la période précédente
        changement_denomination_usuelle_unite_legale (Union[Unset, bool]): Indicatrice de changement de la dénomination
            par rapport à la période précédente
    """

    date_fin: Unset | datetime.date = UNSET
    date_debut: Unset | datetime.date = UNSET
    etat_administratif_unite_legale: (
        Unset | PeriodeUniteLegaleEtatAdministratifUniteLegale
    ) = UNSET
    changement_etat_administratif_unite_legale: Unset | bool = UNSET
    nom_unite_legale: Unset | str = UNSET
    changement_nom_unite_legale: Unset | bool = UNSET
    nom_usage_unite_legale: Unset | str = UNSET
    changement_nom_usage_unite_legale: Unset | bool = UNSET
    denomination_unite_legale: Unset | str = UNSET
    changement_denomination_unite_legale: Unset | bool = UNSET
    denomination_usuelle_1_unite_legale: Unset | str = UNSET
    denomination_usuelle_2_unite_legale: Unset | str = UNSET
    denomination_usuelle_3_unite_legale: Unset | str = UNSET
    categorie_juridique_unite_legale: Unset | str = UNSET
    changement_categorie_juridique_unite_legale: Unset | bool = UNSET
    activite_principale_unite_legale: Unset | str = UNSET
    nomenclature_activite_principale_unite_legale: (
        Unset | PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale
    ) = UNSET
    changement_activite_principale_unite_legale: Unset | bool = UNSET
    nic_siege_unite_legale: Unset | str = UNSET
    changement_nic_siege_unite_legale: Unset | bool = UNSET
    economie_sociale_solidaire_unite_legale: Unset | str = UNSET
    changement_economie_sociale_solidaire_unite_legale: Unset | bool = UNSET
    societe_mission_unite_legale: Unset | str = UNSET
    changement_societe_mission_unite_legale: Unset | bool = UNSET
    caractere_employeur_unite_legale: (
        Unset | PeriodeUniteLegaleCaractereEmployeurUniteLegale
    ) = UNSET
    changement_caractere_employeur_unite_legale: Unset | bool = UNSET
    changement_denomination_usuelle_unite_legale: Unset | bool = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_fin: Unset | str = UNSET
        if not isinstance(self.date_fin, Unset):
            date_fin = self.date_fin.isoformat()

        date_debut: Unset | str = UNSET
        if not isinstance(self.date_debut, Unset):
            date_debut = self.date_debut.isoformat()

        etat_administratif_unite_legale: Unset | str = UNSET
        if not isinstance(self.etat_administratif_unite_legale, Unset):
            etat_administratif_unite_legale = self.etat_administratif_unite_legale.value

        changement_etat_administratif_unite_legale = (
            self.changement_etat_administratif_unite_legale
        )

        nom_unite_legale = self.nom_unite_legale

        changement_nom_unite_legale = self.changement_nom_unite_legale

        nom_usage_unite_legale = self.nom_usage_unite_legale

        changement_nom_usage_unite_legale = self.changement_nom_usage_unite_legale

        denomination_unite_legale = self.denomination_unite_legale

        changement_denomination_unite_legale = self.changement_denomination_unite_legale

        denomination_usuelle_1_unite_legale = self.denomination_usuelle_1_unite_legale

        denomination_usuelle_2_unite_legale = self.denomination_usuelle_2_unite_legale

        denomination_usuelle_3_unite_legale = self.denomination_usuelle_3_unite_legale

        categorie_juridique_unite_legale = self.categorie_juridique_unite_legale

        changement_categorie_juridique_unite_legale = (
            self.changement_categorie_juridique_unite_legale
        )

        activite_principale_unite_legale = self.activite_principale_unite_legale

        nomenclature_activite_principale_unite_legale: Unset | str = UNSET
        if not isinstance(self.nomenclature_activite_principale_unite_legale, Unset):
            nomenclature_activite_principale_unite_legale = (
                self.nomenclature_activite_principale_unite_legale.value
            )

        changement_activite_principale_unite_legale = (
            self.changement_activite_principale_unite_legale
        )

        nic_siege_unite_legale = self.nic_siege_unite_legale

        changement_nic_siege_unite_legale = self.changement_nic_siege_unite_legale

        economie_sociale_solidaire_unite_legale = (
            self.economie_sociale_solidaire_unite_legale
        )

        changement_economie_sociale_solidaire_unite_legale = (
            self.changement_economie_sociale_solidaire_unite_legale
        )

        societe_mission_unite_legale = self.societe_mission_unite_legale

        changement_societe_mission_unite_legale = (
            self.changement_societe_mission_unite_legale
        )

        caractere_employeur_unite_legale: Unset | str = UNSET
        if not isinstance(self.caractere_employeur_unite_legale, Unset):
            caractere_employeur_unite_legale = (
                self.caractere_employeur_unite_legale.value
            )

        changement_caractere_employeur_unite_legale = (
            self.changement_caractere_employeur_unite_legale
        )

        changement_denomination_usuelle_unite_legale = (
            self.changement_denomination_usuelle_unite_legale
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_fin is not UNSET:
            field_dict["dateFin"] = date_fin
        if date_debut is not UNSET:
            field_dict["dateDebut"] = date_debut
        if etat_administratif_unite_legale is not UNSET:
            field_dict["etatAdministratifUniteLegale"] = etat_administratif_unite_legale
        if changement_etat_administratif_unite_legale is not UNSET:
            field_dict["changementEtatAdministratifUniteLegale"] = (
                changement_etat_administratif_unite_legale
            )
        if nom_unite_legale is not UNSET:
            field_dict["nomUniteLegale"] = nom_unite_legale
        if changement_nom_unite_legale is not UNSET:
            field_dict["changementNomUniteLegale"] = changement_nom_unite_legale
        if nom_usage_unite_legale is not UNSET:
            field_dict["nomUsageUniteLegale"] = nom_usage_unite_legale
        if changement_nom_usage_unite_legale is not UNSET:
            field_dict["changementNomUsageUniteLegale"] = (
                changement_nom_usage_unite_legale
            )
        if denomination_unite_legale is not UNSET:
            field_dict["denominationUniteLegale"] = denomination_unite_legale
        if changement_denomination_unite_legale is not UNSET:
            field_dict["changementDenominationUniteLegale"] = (
                changement_denomination_unite_legale
            )
        if denomination_usuelle_1_unite_legale is not UNSET:
            field_dict["denominationUsuelle1UniteLegale"] = (
                denomination_usuelle_1_unite_legale
            )
        if denomination_usuelle_2_unite_legale is not UNSET:
            field_dict["denominationUsuelle2UniteLegale"] = (
                denomination_usuelle_2_unite_legale
            )
        if denomination_usuelle_3_unite_legale is not UNSET:
            field_dict["denominationUsuelle3UniteLegale"] = (
                denomination_usuelle_3_unite_legale
            )
        if categorie_juridique_unite_legale is not UNSET:
            field_dict["categorieJuridiqueUniteLegale"] = (
                categorie_juridique_unite_legale
            )
        if changement_categorie_juridique_unite_legale is not UNSET:
            field_dict["changementCategorieJuridiqueUniteLegale"] = (
                changement_categorie_juridique_unite_legale
            )
        if activite_principale_unite_legale is not UNSET:
            field_dict["activitePrincipaleUniteLegale"] = (
                activite_principale_unite_legale
            )
        if nomenclature_activite_principale_unite_legale is not UNSET:
            field_dict["nomenclatureActivitePrincipaleUniteLegale"] = (
                nomenclature_activite_principale_unite_legale
            )
        if changement_activite_principale_unite_legale is not UNSET:
            field_dict["changementActivitePrincipaleUniteLegale"] = (
                changement_activite_principale_unite_legale
            )
        if nic_siege_unite_legale is not UNSET:
            field_dict["nicSiegeUniteLegale"] = nic_siege_unite_legale
        if changement_nic_siege_unite_legale is not UNSET:
            field_dict["changementNicSiegeUniteLegale"] = (
                changement_nic_siege_unite_legale
            )
        if economie_sociale_solidaire_unite_legale is not UNSET:
            field_dict["economieSocialeSolidaireUniteLegale"] = (
                economie_sociale_solidaire_unite_legale
            )
        if changement_economie_sociale_solidaire_unite_legale is not UNSET:
            field_dict["changementEconomieSocialeSolidaireUniteLegale"] = (
                changement_economie_sociale_solidaire_unite_legale
            )
        if societe_mission_unite_legale is not UNSET:
            field_dict["societeMissionUniteLegale"] = societe_mission_unite_legale
        if changement_societe_mission_unite_legale is not UNSET:
            field_dict["changementSocieteMissionUniteLegale"] = (
                changement_societe_mission_unite_legale
            )
        if caractere_employeur_unite_legale is not UNSET:
            field_dict["caractereEmployeurUniteLegale"] = (
                caractere_employeur_unite_legale
            )
        if changement_caractere_employeur_unite_legale is not UNSET:
            field_dict["changementCaractereEmployeurUniteLegale"] = (
                changement_caractere_employeur_unite_legale
            )
        if changement_denomination_usuelle_unite_legale is not UNSET:
            field_dict["changementDenominationUsuelleUniteLegale"] = (
                changement_denomination_usuelle_unite_legale
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date_fin = d.pop("dateFin", UNSET)
        date_fin: Unset | datetime.date
        if isinstance(_date_fin, Unset) or _date_fin is None:
            date_fin = UNSET
        else:
            date_fin = isoparse(_date_fin).date()

        _date_debut = d.pop("dateDebut", UNSET)
        date_debut: Unset | datetime.date
        if isinstance(_date_debut, Unset) or _date_debut is None:
            date_debut = UNSET
        else:
            date_debut = isoparse(_date_debut).date()

        _etat_administratif_unite_legale = d.pop("etatAdministratifUniteLegale", UNSET)
        etat_administratif_unite_legale: (
            Unset | PeriodeUniteLegaleEtatAdministratifUniteLegale
        )
        if (
            isinstance(_etat_administratif_unite_legale, Unset)
            or _etat_administratif_unite_legale is None
        ):
            etat_administratif_unite_legale = UNSET
        else:
            etat_administratif_unite_legale = (
                PeriodeUniteLegaleEtatAdministratifUniteLegale(
                    _etat_administratif_unite_legale
                )
            )

        changement_etat_administratif_unite_legale = d.pop(
            "changementEtatAdministratifUniteLegale", UNSET
        )

        nom_unite_legale = d.pop("nomUniteLegale", UNSET)

        changement_nom_unite_legale = d.pop("changementNomUniteLegale", UNSET)

        nom_usage_unite_legale = d.pop("nomUsageUniteLegale", UNSET)

        changement_nom_usage_unite_legale = d.pop(
            "changementNomUsageUniteLegale", UNSET
        )

        denomination_unite_legale = d.pop("denominationUniteLegale", UNSET)

        changement_denomination_unite_legale = d.pop(
            "changementDenominationUniteLegale", UNSET
        )

        denomination_usuelle_1_unite_legale = d.pop(
            "denominationUsuelle1UniteLegale", UNSET
        )

        denomination_usuelle_2_unite_legale = d.pop(
            "denominationUsuelle2UniteLegale", UNSET
        )

        denomination_usuelle_3_unite_legale = d.pop(
            "denominationUsuelle3UniteLegale", UNSET
        )

        categorie_juridique_unite_legale = d.pop("categorieJuridiqueUniteLegale", UNSET)

        changement_categorie_juridique_unite_legale = d.pop(
            "changementCategorieJuridiqueUniteLegale", UNSET
        )

        activite_principale_unite_legale = d.pop("activitePrincipaleUniteLegale", UNSET)

        _nomenclature_activite_principale_unite_legale = d.pop(
            "nomenclatureActivitePrincipaleUniteLegale", UNSET
        )
        nomenclature_activite_principale_unite_legale: (
            Unset | PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale
        )
        if (
            isinstance(_nomenclature_activite_principale_unite_legale, Unset)
            or _nomenclature_activite_principale_unite_legale is None
        ):
            nomenclature_activite_principale_unite_legale = UNSET
        else:
            nomenclature_activite_principale_unite_legale = (
                PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale(
                    _nomenclature_activite_principale_unite_legale
                )
            )

        changement_activite_principale_unite_legale = d.pop(
            "changementActivitePrincipaleUniteLegale", UNSET
        )

        nic_siege_unite_legale = d.pop("nicSiegeUniteLegale", UNSET)

        changement_nic_siege_unite_legale = d.pop(
            "changementNicSiegeUniteLegale", UNSET
        )

        economie_sociale_solidaire_unite_legale = d.pop(
            "economieSocialeSolidaireUniteLegale", UNSET
        )

        changement_economie_sociale_solidaire_unite_legale = d.pop(
            "changementEconomieSocialeSolidaireUniteLegale", UNSET
        )

        societe_mission_unite_legale = d.pop("societeMissionUniteLegale", UNSET)

        changement_societe_mission_unite_legale = d.pop(
            "changementSocieteMissionUniteLegale", UNSET
        )

        _caractere_employeur_unite_legale = d.pop(
            "caractereEmployeurUniteLegale", UNSET
        )
        caractere_employeur_unite_legale: (
            Unset | PeriodeUniteLegaleCaractereEmployeurUniteLegale
        )
        if (
            isinstance(_caractere_employeur_unite_legale, Unset)
            or _caractere_employeur_unite_legale is None
        ):
            caractere_employeur_unite_legale = UNSET
        else:
            caractere_employeur_unite_legale = (
                PeriodeUniteLegaleCaractereEmployeurUniteLegale(
                    _caractere_employeur_unite_legale
                )
            )

        changement_caractere_employeur_unite_legale = d.pop(
            "changementCaractereEmployeurUniteLegale", UNSET
        )

        changement_denomination_usuelle_unite_legale = d.pop(
            "changementDenominationUsuelleUniteLegale", UNSET
        )

        periode_unite_legale = cls(
            date_fin=date_fin,
            date_debut=date_debut,
            etat_administratif_unite_legale=etat_administratif_unite_legale,
            changement_etat_administratif_unite_legale=changement_etat_administratif_unite_legale,
            nom_unite_legale=nom_unite_legale,
            changement_nom_unite_legale=changement_nom_unite_legale,
            nom_usage_unite_legale=nom_usage_unite_legale,
            changement_nom_usage_unite_legale=changement_nom_usage_unite_legale,
            denomination_unite_legale=denomination_unite_legale,
            changement_denomination_unite_legale=changement_denomination_unite_legale,
            denomination_usuelle_1_unite_legale=denomination_usuelle_1_unite_legale,
            denomination_usuelle_2_unite_legale=denomination_usuelle_2_unite_legale,
            denomination_usuelle_3_unite_legale=denomination_usuelle_3_unite_legale,
            categorie_juridique_unite_legale=categorie_juridique_unite_legale,
            changement_categorie_juridique_unite_legale=changement_categorie_juridique_unite_legale,
            activite_principale_unite_legale=activite_principale_unite_legale,
            nomenclature_activite_principale_unite_legale=nomenclature_activite_principale_unite_legale,
            changement_activite_principale_unite_legale=changement_activite_principale_unite_legale,
            nic_siege_unite_legale=nic_siege_unite_legale,
            changement_nic_siege_unite_legale=changement_nic_siege_unite_legale,
            economie_sociale_solidaire_unite_legale=economie_sociale_solidaire_unite_legale,
            changement_economie_sociale_solidaire_unite_legale=changement_economie_sociale_solidaire_unite_legale,
            societe_mission_unite_legale=societe_mission_unite_legale,
            changement_societe_mission_unite_legale=changement_societe_mission_unite_legale,
            caractere_employeur_unite_legale=caractere_employeur_unite_legale,
            changement_caractere_employeur_unite_legale=changement_caractere_employeur_unite_legale,
            changement_denomination_usuelle_unite_legale=changement_denomination_usuelle_unite_legale,
        )

        periode_unite_legale.additional_properties = d
        return periode_unite_legale

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
