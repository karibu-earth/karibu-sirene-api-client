from collections.abc import Mapping
import datetime
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sirene_api_client.api_types import UNSET, Unset
from sirene_api_client.models.unite_legale_etablissement_caractere_employeur_unite_legale import (
    UniteLegaleEtablissementCaractereEmployeurUniteLegale,
)
from sirene_api_client.models.unite_legale_etablissement_categorie_entreprise import (
    UniteLegaleEtablissementCategorieEntreprise,
)
from sirene_api_client.models.unite_legale_etablissement_etat_administratif_unite_legale import (
    UniteLegaleEtablissementEtatAdministratifUniteLegale,
)
from sirene_api_client.models.unite_legale_etablissement_nomenclature_activite_principale_unite_legale import (
    UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale,
)
from sirene_api_client.models.unite_legale_etablissement_sexe_unite_legale import (
    UniteLegaleEtablissementSexeUniteLegale,
)

T = TypeVar("T", bound="UniteLegaleEtablissement")


@_attrs_define
class UniteLegaleEtablissement:
    """Objet représentant les valeurs courante de l'unité légale de l'établissement

    Attributes:
        statut_diffusion_unite_legale (Union[Unset, str]): Statut de diffusion de l'unité légale Example: O.
        unite_purgee_unite_legale (Union[Unset, bool]): True si l'unité est une unité purgée
        date_creation_unite_legale (Union[Unset, datetime.date]): Date de création de l'unité légale Example: AAAA-MM-
            JJ.
        date_naissance_unite_legale (Union[Unset, str]): L'accès à ces données est soumis à une démarche auprès de la
            Commission nationale de l'informatique et des libertés. Date de naissance pour la personne physique sinon null
        code_commune_naissance_unite_legale (Union[Unset, str]): L'accès à ces données est soumis à une démarche auprès
            de la Commission nationale de l'informatique et des libertés. Code commune de naissance pour les personnes
            physiques, null pour les personnes morales et les personnes physiques nées à l'étranger
        code_pays_naissance_unite_legale (Union[Unset, str]): L'accès à ces données est soumis à une démarche auprès de
            la Commission nationale de l'informatique et des libertés. Code pays de naissance pour les personnes physiques
            nées à l'étranger, null sinon
        libelle_nationalite_unite_legale (Union[Unset, str]): L'accès à ces données est soumis à une démarche auprès de
            la Commission nationale de l'informatique et des libertés. Nationalité pour les personnes physiques
        identifiant_association_unite_legale (Union[Unset, str]): Numéro au Répertoire National des Associations
        tranche_effectifs_unite_legale (Union[Unset, str]): Tranche d'effectif salarié de l'unité légale, valorisé
            uniquement si l'année correspondante est supérieure ou égale à l'année d'interrogation-3 (sinon, NN)
        annee_effectifs_unite_legale (Union[Unset, str]): Année de validité de la tranche d'effectif salarié de l'unité
            légale, valorisée uniquement si l'année est supérieure ou égale à l'année d'interrogation-3 (sinon, null)
        date_dernier_traitement_unite_legale (Union[Unset, str]): Date de la dernière mise à jour effectuée au
            répertoire Sirene sur le Siren concerné
        categorie_entreprise (Union[Unset, UniteLegaleEtablissementCategorieEntreprise]): Catégorie à laquelle
            appartient l'entreprise : Petite ou moyenne entreprise, Entreprise de taille intermédiaire, Grande entreprise
        annee_categorie_entreprise (Union[Unset, str]): Année de validité de la catégorie d'entreprise
        sigle_unite_legale (Union[Unset, str]): Sigle de l'unité légale
        sexe_unite_legale (Union[Unset, UniteLegaleEtablissementSexeUniteLegale]): Sexe pour les personnes physiques
            sinon null
        prenom_1_unite_legale (Union[Unset, str]): Premier prénom déclaré pour une personne physique, peut être null
            dans le cas d'une unité purgée
        prenom_2_unite_legale (Union[Unset, str]): Deuxième prénom déclaré pour une personne physique
        prenom_3_unite_legale (Union[Unset, str]): Troisième prénom déclaré pour une personne physique
        prenom_4_unite_legale (Union[Unset, str]): Quatrième prénom déclaré pour une personne physique
        prenom_usuel_unite_legale (Union[Unset, str]): Prénom usuel pour les personne physiques, correspond généralement
            au Prenom1
        pseudonyme_unite_legale (Union[Unset, str]): Pseudonyme pour les personnes physiques
        etat_administratif_unite_legale (Union[Unset, UniteLegaleEtablissementEtatAdministratifUniteLegale]): État de
            l'entreprise pendant la période (A= entreprise active, C= entreprise cessée)
        nom_unite_legale (Union[Unset, str]): Nom de naissance pour les personnes physiques pour la période (null pour
            les personnes morales)
        denomination_unite_legale (Union[Unset, str]): Raison sociale (personnes morales)
        denomination_usuelle_1_unite_legale (Union[Unset, str]): Premier nom sous lequel l'entreprise est connue du
            public
        denomination_usuelle_2_unite_legale (Union[Unset, str]): Deuxième nom sous lequel l'entreprise est connue du
            public
        denomination_usuelle_3_unite_legale (Union[Unset, str]): Troisième nom sous lequel l'entreprise est connue du
            public
        activite_principale_unite_legale (Union[Unset, str]): Activité principale de l'entreprise pendant la période
            (l'APE est codifiée selon la <a href='https://www.insee.fr/fr/information/2406147'>nomenclature d'Activités
            Française (NAF)</a>
        categorie_juridique_unite_legale (Union[Unset, str]): Catégorie juridique de l'entreprise (=1000 pour les
            personnes physiques)
        nic_siege_unite_legale (Union[Unset, str]): Identifiant du siège pour la période (le Siret du siège est obtenu
            en concaténant le numéro Siren et le NIC)
        nomenclature_activite_principale_unite_legale (Union[Unset,
            UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale]): Nomenclature de l'activité, permet de
            savoir à partir de quelle nomenclature est codifiée ActivitePrincipale
        nom_usage_unite_legale (Union[Unset, str]): Nom d'usage pour les personnes physiques sinon null
        economie_sociale_solidaire_unite_legale (Union[Unset, str]): Appartenance de l'unité légale au champ de
            l'économie sociale et solidaire (ESS)
        societe_mission_unite_legale (Union[Unset, str]): Appartenance de l'unité légale au champ societé à mission
        caractere_employeur_unite_legale (Union[Unset, UniteLegaleEtablissementCaractereEmployeurUniteLegale]):
            Caractère employeur de l'entreprise. Valeur courante=O si au moins l'un des établissements actifs de l'unité
            légale emploie des salariés
    """

    statut_diffusion_unite_legale: Unset | str = UNSET
    unite_purgee_unite_legale: Unset | bool = UNSET
    date_creation_unite_legale: Unset | datetime.date = UNSET
    date_naissance_unite_legale: Unset | str = UNSET
    code_commune_naissance_unite_legale: Unset | str = UNSET
    code_pays_naissance_unite_legale: Unset | str = UNSET
    libelle_nationalite_unite_legale: Unset | str = UNSET
    identifiant_association_unite_legale: Unset | str = UNSET
    tranche_effectifs_unite_legale: Unset | str = UNSET
    annee_effectifs_unite_legale: Unset | str = UNSET
    date_dernier_traitement_unite_legale: Unset | str = UNSET
    categorie_entreprise: Unset | UniteLegaleEtablissementCategorieEntreprise = UNSET
    annee_categorie_entreprise: Unset | str = UNSET
    sigle_unite_legale: Unset | str = UNSET
    sexe_unite_legale: Unset | UniteLegaleEtablissementSexeUniteLegale = UNSET
    prenom_1_unite_legale: Unset | str = UNSET
    prenom_2_unite_legale: Unset | str = UNSET
    prenom_3_unite_legale: Unset | str = UNSET
    prenom_4_unite_legale: Unset | str = UNSET
    prenom_usuel_unite_legale: Unset | str = UNSET
    pseudonyme_unite_legale: Unset | str = UNSET
    etat_administratif_unite_legale: (
        Unset | UniteLegaleEtablissementEtatAdministratifUniteLegale
    ) = UNSET
    nom_unite_legale: Unset | str = UNSET
    denomination_unite_legale: Unset | str = UNSET
    denomination_usuelle_1_unite_legale: Unset | str = UNSET
    denomination_usuelle_2_unite_legale: Unset | str = UNSET
    denomination_usuelle_3_unite_legale: Unset | str = UNSET
    activite_principale_unite_legale: Unset | str = UNSET
    categorie_juridique_unite_legale: Unset | str = UNSET
    nic_siege_unite_legale: Unset | str = UNSET
    nomenclature_activite_principale_unite_legale: (
        Unset | UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale
    ) = UNSET
    nom_usage_unite_legale: Unset | str = UNSET
    economie_sociale_solidaire_unite_legale: Unset | str = UNSET
    societe_mission_unite_legale: Unset | str = UNSET
    caractere_employeur_unite_legale: (
        Unset | UniteLegaleEtablissementCaractereEmployeurUniteLegale
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        statut_diffusion_unite_legale = self.statut_diffusion_unite_legale

        unite_purgee_unite_legale = self.unite_purgee_unite_legale

        date_creation_unite_legale: Unset | str = UNSET
        if not isinstance(self.date_creation_unite_legale, Unset):
            date_creation_unite_legale = self.date_creation_unite_legale.isoformat()

        date_naissance_unite_legale = self.date_naissance_unite_legale

        code_commune_naissance_unite_legale = self.code_commune_naissance_unite_legale

        code_pays_naissance_unite_legale = self.code_pays_naissance_unite_legale

        libelle_nationalite_unite_legale = self.libelle_nationalite_unite_legale

        identifiant_association_unite_legale = self.identifiant_association_unite_legale

        tranche_effectifs_unite_legale = self.tranche_effectifs_unite_legale

        annee_effectifs_unite_legale = self.annee_effectifs_unite_legale

        date_dernier_traitement_unite_legale = self.date_dernier_traitement_unite_legale

        categorie_entreprise: Unset | str = UNSET
        if not isinstance(self.categorie_entreprise, Unset):
            categorie_entreprise = self.categorie_entreprise.value

        annee_categorie_entreprise = self.annee_categorie_entreprise

        sigle_unite_legale = self.sigle_unite_legale

        sexe_unite_legale: Unset | str = UNSET
        if not isinstance(self.sexe_unite_legale, Unset):
            sexe_unite_legale = self.sexe_unite_legale.value

        prenom_1_unite_legale = self.prenom_1_unite_legale

        prenom_2_unite_legale = self.prenom_2_unite_legale

        prenom_3_unite_legale = self.prenom_3_unite_legale

        prenom_4_unite_legale = self.prenom_4_unite_legale

        prenom_usuel_unite_legale = self.prenom_usuel_unite_legale

        pseudonyme_unite_legale = self.pseudonyme_unite_legale

        etat_administratif_unite_legale: Unset | str = UNSET
        if not isinstance(self.etat_administratif_unite_legale, Unset):
            etat_administratif_unite_legale = self.etat_administratif_unite_legale.value

        nom_unite_legale = self.nom_unite_legale

        denomination_unite_legale = self.denomination_unite_legale

        denomination_usuelle_1_unite_legale = self.denomination_usuelle_1_unite_legale

        denomination_usuelle_2_unite_legale = self.denomination_usuelle_2_unite_legale

        denomination_usuelle_3_unite_legale = self.denomination_usuelle_3_unite_legale

        activite_principale_unite_legale = self.activite_principale_unite_legale

        categorie_juridique_unite_legale = self.categorie_juridique_unite_legale

        nic_siege_unite_legale = self.nic_siege_unite_legale

        nomenclature_activite_principale_unite_legale: Unset | str = UNSET
        if not isinstance(self.nomenclature_activite_principale_unite_legale, Unset):
            nomenclature_activite_principale_unite_legale = (
                self.nomenclature_activite_principale_unite_legale.value
            )

        nom_usage_unite_legale = self.nom_usage_unite_legale

        economie_sociale_solidaire_unite_legale = (
            self.economie_sociale_solidaire_unite_legale
        )

        societe_mission_unite_legale = self.societe_mission_unite_legale

        caractere_employeur_unite_legale: Unset | str = UNSET
        if not isinstance(self.caractere_employeur_unite_legale, Unset):
            caractere_employeur_unite_legale = (
                self.caractere_employeur_unite_legale.value
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if statut_diffusion_unite_legale is not UNSET:
            field_dict["statutDiffusionUniteLegale"] = statut_diffusion_unite_legale
        if unite_purgee_unite_legale is not UNSET:
            field_dict["unitePurgeeUniteLegale"] = unite_purgee_unite_legale
        if date_creation_unite_legale is not UNSET:
            field_dict["dateCreationUniteLegale"] = date_creation_unite_legale
        if date_naissance_unite_legale is not UNSET:
            field_dict["dateNaissanceUniteLegale"] = date_naissance_unite_legale
        if code_commune_naissance_unite_legale is not UNSET:
            field_dict["codeCommuneNaissanceUniteLegale"] = (
                code_commune_naissance_unite_legale
            )
        if code_pays_naissance_unite_legale is not UNSET:
            field_dict["codePaysNaissanceUniteLegale"] = (
                code_pays_naissance_unite_legale
            )
        if libelle_nationalite_unite_legale is not UNSET:
            field_dict["libelleNationaliteUniteLegale"] = (
                libelle_nationalite_unite_legale
            )
        if identifiant_association_unite_legale is not UNSET:
            field_dict["identifiantAssociationUniteLegale"] = (
                identifiant_association_unite_legale
            )
        if tranche_effectifs_unite_legale is not UNSET:
            field_dict["trancheEffectifsUniteLegale"] = tranche_effectifs_unite_legale
        if annee_effectifs_unite_legale is not UNSET:
            field_dict["anneeEffectifsUniteLegale"] = annee_effectifs_unite_legale
        if date_dernier_traitement_unite_legale is not UNSET:
            field_dict["dateDernierTraitementUniteLegale"] = (
                date_dernier_traitement_unite_legale
            )
        if categorie_entreprise is not UNSET:
            field_dict["categorieEntreprise"] = categorie_entreprise
        if annee_categorie_entreprise is not UNSET:
            field_dict["anneeCategorieEntreprise"] = annee_categorie_entreprise
        if sigle_unite_legale is not UNSET:
            field_dict["sigleUniteLegale"] = sigle_unite_legale
        if sexe_unite_legale is not UNSET:
            field_dict["sexeUniteLegale"] = sexe_unite_legale
        if prenom_1_unite_legale is not UNSET:
            field_dict["prenom1UniteLegale"] = prenom_1_unite_legale
        if prenom_2_unite_legale is not UNSET:
            field_dict["prenom2UniteLegale"] = prenom_2_unite_legale
        if prenom_3_unite_legale is not UNSET:
            field_dict["prenom3UniteLegale"] = prenom_3_unite_legale
        if prenom_4_unite_legale is not UNSET:
            field_dict["prenom4UniteLegale"] = prenom_4_unite_legale
        if prenom_usuel_unite_legale is not UNSET:
            field_dict["prenomUsuelUniteLegale"] = prenom_usuel_unite_legale
        if pseudonyme_unite_legale is not UNSET:
            field_dict["pseudonymeUniteLegale"] = pseudonyme_unite_legale
        if etat_administratif_unite_legale is not UNSET:
            field_dict["etatAdministratifUniteLegale"] = etat_administratif_unite_legale
        if nom_unite_legale is not UNSET:
            field_dict["nomUniteLegale"] = nom_unite_legale
        if denomination_unite_legale is not UNSET:
            field_dict["denominationUniteLegale"] = denomination_unite_legale
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
        if activite_principale_unite_legale is not UNSET:
            field_dict["activitePrincipaleUniteLegale"] = (
                activite_principale_unite_legale
            )
        if categorie_juridique_unite_legale is not UNSET:
            field_dict["categorieJuridiqueUniteLegale"] = (
                categorie_juridique_unite_legale
            )
        if nic_siege_unite_legale is not UNSET:
            field_dict["nicSiegeUniteLegale"] = nic_siege_unite_legale
        if nomenclature_activite_principale_unite_legale is not UNSET:
            field_dict["nomenclatureActivitePrincipaleUniteLegale"] = (
                nomenclature_activite_principale_unite_legale
            )
        if nom_usage_unite_legale is not UNSET:
            field_dict["nomUsageUniteLegale"] = nom_usage_unite_legale
        if economie_sociale_solidaire_unite_legale is not UNSET:
            field_dict["economieSocialeSolidaireUniteLegale"] = (
                economie_sociale_solidaire_unite_legale
            )
        if societe_mission_unite_legale is not UNSET:
            field_dict["societeMissionUniteLegale"] = societe_mission_unite_legale
        if caractere_employeur_unite_legale is not UNSET:
            field_dict["caractereEmployeurUniteLegale"] = (
                caractere_employeur_unite_legale
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        statut_diffusion_unite_legale = d.pop("statutDiffusionUniteLegale", UNSET)

        unite_purgee_unite_legale = d.pop("unitePurgeeUniteLegale", UNSET)

        _date_creation_unite_legale = d.pop("dateCreationUniteLegale", UNSET)
        date_creation_unite_legale: Unset | datetime.date
        if isinstance(_date_creation_unite_legale, Unset):
            date_creation_unite_legale = UNSET
        else:
            date_creation_unite_legale = isoparse(_date_creation_unite_legale).date()

        date_naissance_unite_legale = d.pop("dateNaissanceUniteLegale", UNSET)

        code_commune_naissance_unite_legale = d.pop(
            "codeCommuneNaissanceUniteLegale", UNSET
        )

        code_pays_naissance_unite_legale = d.pop("codePaysNaissanceUniteLegale", UNSET)

        libelle_nationalite_unite_legale = d.pop("libelleNationaliteUniteLegale", UNSET)

        identifiant_association_unite_legale = d.pop(
            "identifiantAssociationUniteLegale", UNSET
        )

        tranche_effectifs_unite_legale = d.pop("trancheEffectifsUniteLegale", UNSET)

        annee_effectifs_unite_legale = d.pop("anneeEffectifsUniteLegale", UNSET)

        date_dernier_traitement_unite_legale = d.pop(
            "dateDernierTraitementUniteLegale", UNSET
        )

        _categorie_entreprise = d.pop("categorieEntreprise", UNSET)
        categorie_entreprise: Unset | UniteLegaleEtablissementCategorieEntreprise
        if isinstance(_categorie_entreprise, Unset) or _categorie_entreprise is None:
            categorie_entreprise = UNSET
        else:
            categorie_entreprise = UniteLegaleEtablissementCategorieEntreprise(
                _categorie_entreprise
            )

        annee_categorie_entreprise = d.pop("anneeCategorieEntreprise", UNSET)

        sigle_unite_legale = d.pop("sigleUniteLegale", UNSET)

        _sexe_unite_legale = d.pop("sexeUniteLegale", UNSET)
        sexe_unite_legale: Unset | UniteLegaleEtablissementSexeUniteLegale
        if isinstance(_sexe_unite_legale, Unset) or _sexe_unite_legale is None:
            sexe_unite_legale = UNSET
        else:
            sexe_unite_legale = UniteLegaleEtablissementSexeUniteLegale(
                _sexe_unite_legale
            )

        prenom_1_unite_legale = d.pop("prenom1UniteLegale", UNSET)

        prenom_2_unite_legale = d.pop("prenom2UniteLegale", UNSET)

        prenom_3_unite_legale = d.pop("prenom3UniteLegale", UNSET)

        prenom_4_unite_legale = d.pop("prenom4UniteLegale", UNSET)

        prenom_usuel_unite_legale = d.pop("prenomUsuelUniteLegale", UNSET)

        pseudonyme_unite_legale = d.pop("pseudonymeUniteLegale", UNSET)

        _etat_administratif_unite_legale = d.pop("etatAdministratifUniteLegale", UNSET)
        etat_administratif_unite_legale: (
            Unset | UniteLegaleEtablissementEtatAdministratifUniteLegale
        )
        if (
            isinstance(_etat_administratif_unite_legale, Unset)
            or _etat_administratif_unite_legale is None
        ):
            etat_administratif_unite_legale = UNSET
        else:
            etat_administratif_unite_legale = (
                UniteLegaleEtablissementEtatAdministratifUniteLegale(
                    _etat_administratif_unite_legale
                )
            )

        nom_unite_legale = d.pop("nomUniteLegale", UNSET)

        denomination_unite_legale = d.pop("denominationUniteLegale", UNSET)

        denomination_usuelle_1_unite_legale = d.pop(
            "denominationUsuelle1UniteLegale", UNSET
        )

        denomination_usuelle_2_unite_legale = d.pop(
            "denominationUsuelle2UniteLegale", UNSET
        )

        denomination_usuelle_3_unite_legale = d.pop(
            "denominationUsuelle3UniteLegale", UNSET
        )

        activite_principale_unite_legale = d.pop("activitePrincipaleUniteLegale", UNSET)

        categorie_juridique_unite_legale = d.pop("categorieJuridiqueUniteLegale", UNSET)

        nic_siege_unite_legale = d.pop("nicSiegeUniteLegale", UNSET)

        _nomenclature_activite_principale_unite_legale = d.pop(
            "nomenclatureActivitePrincipaleUniteLegale", UNSET
        )
        nomenclature_activite_principale_unite_legale: (
            Unset | UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale
        )
        if (
            isinstance(_nomenclature_activite_principale_unite_legale, Unset)
            or _nomenclature_activite_principale_unite_legale is None
        ):
            nomenclature_activite_principale_unite_legale = UNSET
        else:
            nomenclature_activite_principale_unite_legale = (
                UniteLegaleEtablissementNomenclatureActivitePrincipaleUniteLegale(
                    _nomenclature_activite_principale_unite_legale
                )
            )

        nom_usage_unite_legale = d.pop("nomUsageUniteLegale", UNSET)

        economie_sociale_solidaire_unite_legale = d.pop(
            "economieSocialeSolidaireUniteLegale", UNSET
        )

        societe_mission_unite_legale = d.pop("societeMissionUniteLegale", UNSET)

        _caractere_employeur_unite_legale = d.pop(
            "caractereEmployeurUniteLegale", UNSET
        )
        caractere_employeur_unite_legale: (
            Unset | UniteLegaleEtablissementCaractereEmployeurUniteLegale
        )
        if (
            isinstance(_caractere_employeur_unite_legale, Unset)
            or _caractere_employeur_unite_legale is None
        ):
            caractere_employeur_unite_legale = UNSET
        else:
            caractere_employeur_unite_legale = (
                UniteLegaleEtablissementCaractereEmployeurUniteLegale(
                    _caractere_employeur_unite_legale
                )
            )

        unite_legale_etablissement = cls(
            statut_diffusion_unite_legale=statut_diffusion_unite_legale,
            unite_purgee_unite_legale=unite_purgee_unite_legale,
            date_creation_unite_legale=date_creation_unite_legale,
            date_naissance_unite_legale=date_naissance_unite_legale,
            code_commune_naissance_unite_legale=code_commune_naissance_unite_legale,
            code_pays_naissance_unite_legale=code_pays_naissance_unite_legale,
            libelle_nationalite_unite_legale=libelle_nationalite_unite_legale,
            identifiant_association_unite_legale=identifiant_association_unite_legale,
            tranche_effectifs_unite_legale=tranche_effectifs_unite_legale,
            annee_effectifs_unite_legale=annee_effectifs_unite_legale,
            date_dernier_traitement_unite_legale=date_dernier_traitement_unite_legale,
            categorie_entreprise=categorie_entreprise,
            annee_categorie_entreprise=annee_categorie_entreprise,
            sigle_unite_legale=sigle_unite_legale,
            sexe_unite_legale=sexe_unite_legale,
            prenom_1_unite_legale=prenom_1_unite_legale,
            prenom_2_unite_legale=prenom_2_unite_legale,
            prenom_3_unite_legale=prenom_3_unite_legale,
            prenom_4_unite_legale=prenom_4_unite_legale,
            prenom_usuel_unite_legale=prenom_usuel_unite_legale,
            pseudonyme_unite_legale=pseudonyme_unite_legale,
            etat_administratif_unite_legale=etat_administratif_unite_legale,
            nom_unite_legale=nom_unite_legale,
            denomination_unite_legale=denomination_unite_legale,
            denomination_usuelle_1_unite_legale=denomination_usuelle_1_unite_legale,
            denomination_usuelle_2_unite_legale=denomination_usuelle_2_unite_legale,
            denomination_usuelle_3_unite_legale=denomination_usuelle_3_unite_legale,
            activite_principale_unite_legale=activite_principale_unite_legale,
            categorie_juridique_unite_legale=categorie_juridique_unite_legale,
            nic_siege_unite_legale=nic_siege_unite_legale,
            nomenclature_activite_principale_unite_legale=nomenclature_activite_principale_unite_legale,
            nom_usage_unite_legale=nom_usage_unite_legale,
            economie_sociale_solidaire_unite_legale=economie_sociale_solidaire_unite_legale,
            societe_mission_unite_legale=societe_mission_unite_legale,
            caractere_employeur_unite_legale=caractere_employeur_unite_legale,
        )

        unite_legale_etablissement.additional_properties = d
        return unite_legale_etablissement

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
