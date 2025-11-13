from collections.abc import Mapping
import datetime
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sirene_api_client.api_types import UNSET, Unset
from sirene_api_client.models.unite_legale_categorie_entreprise import (
    UniteLegaleCategorieEntreprise,
)
from sirene_api_client.models.unite_legale_sexe_unite_legale import (
    UniteLegaleSexeUniteLegale,
)

if TYPE_CHECKING:
    from sirene_api_client.models.periode_unite_legale import PeriodeUniteLegale


T = TypeVar("T", bound="UniteLegale")


@_attrs_define
class UniteLegale:
    """
    Attributes:
        score (Union[Unset, float]): Score de l'élément parmi l'ensemble des éléments répondant à la requête, plus le
            score est élevé, plus l'élément est haut placé. Le score n'a pas de signification en dehors de la requête et
            n'est pas comparable aux score d'autres requêtes
        siren (Union[Unset, str]): Numéro Siren de l'entreprise, toujours renseigné Example: 005520135.
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
        nombre_periodes_unite_legale (Union[Unset, int]): Nombre de périodes dans la vie de l'unité légale
        categorie_entreprise (Union[Unset, UniteLegaleCategorieEntreprise]): Catégorie à laquelle appartient
            l'entreprise : Petite ou moyenne entreprise, Entreprise de taille intermédiaire, Grande entreprise
        annee_categorie_entreprise (Union[Unset, str]): Année de validité de la catégorie d'entreprise
        sigle_unite_legale (Union[Unset, str]): Sigle de l'unité légale
        sexe_unite_legale (Union[Unset, UniteLegaleSexeUniteLegale]): Sexe pour les personnes physiques sinon null
        prenom_1_unite_legale (Union[Unset, str]): Premier prénom déclaré pour une personne physique, peut être null
            dans le cas d'une unité purgée
        prenom_2_unite_legale (Union[Unset, str]): Deuxième prénom déclaré pour une personne physique
        prenom_3_unite_legale (Union[Unset, str]): Troisième prénom déclaré pour une personne physique
        prenom_4_unite_legale (Union[Unset, str]): Quatrième prénom déclaré pour une personne physique
        prenom_usuel_unite_legale (Union[Unset, str]): Prénom usuel pour les personne physiques, correspond généralement
            au Prenom1
        pseudonyme_unite_legale (Union[Unset, str]): Pseudonyme pour les personnes physiques
        periodes_unite_legale (Union[Unset, list['PeriodeUniteLegale']]):
    """

    score: Unset | float = UNSET
    siren: Unset | str = UNSET
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
    nombre_periodes_unite_legale: Unset | int = UNSET
    categorie_entreprise: Unset | UniteLegaleCategorieEntreprise = UNSET
    annee_categorie_entreprise: Unset | str = UNSET
    sigle_unite_legale: Unset | str = UNSET
    sexe_unite_legale: Unset | UniteLegaleSexeUniteLegale = UNSET
    prenom_1_unite_legale: Unset | str = UNSET
    prenom_2_unite_legale: Unset | str = UNSET
    prenom_3_unite_legale: Unset | str = UNSET
    prenom_4_unite_legale: Unset | str = UNSET
    prenom_usuel_unite_legale: Unset | str = UNSET
    pseudonyme_unite_legale: Unset | str = UNSET
    periodes_unite_legale: Unset | list["PeriodeUniteLegale"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        siren = self.siren

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

        nombre_periodes_unite_legale = self.nombre_periodes_unite_legale

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

        periodes_unite_legale: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.periodes_unite_legale, Unset):
            periodes_unite_legale = []
            for periodes_unite_legale_item_data in self.periodes_unite_legale:
                periodes_unite_legale_item = periodes_unite_legale_item_data.to_dict()
                periodes_unite_legale.append(periodes_unite_legale_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if siren is not UNSET:
            field_dict["siren"] = siren
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
        if nombre_periodes_unite_legale is not UNSET:
            field_dict["nombrePeriodesUniteLegale"] = nombre_periodes_unite_legale
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
        if periodes_unite_legale is not UNSET:
            field_dict["periodesUniteLegale"] = periodes_unite_legale

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from sirene_api_client.models.periode_unite_legale import PeriodeUniteLegale

        d = dict(src_dict)
        score = d.pop("score", UNSET)

        siren = d.pop("siren", UNSET)

        statut_diffusion_unite_legale = d.pop("statutDiffusionUniteLegale", UNSET)

        unite_purgee_unite_legale = d.pop("unitePurgeeUniteLegale", UNSET)

        _date_creation_unite_legale = d.pop("dateCreationUniteLegale", UNSET)
        date_creation_unite_legale: Unset | datetime.date
        if (
            isinstance(_date_creation_unite_legale, Unset)
            or _date_creation_unite_legale is None
        ):
            date_creation_unite_legale = UNSET
        else:
            date_creation_unite_legale = isoparse(_date_creation_unite_legale).date()

        date_naissance_unite_legale = d.pop("dateNaissanceUniteLegale", UNSET)
        if date_naissance_unite_legale is None:
            date_naissance_unite_legale = UNSET

        code_commune_naissance_unite_legale = d.pop(
            "codeCommuneNaissanceUniteLegale", UNSET
        )

        code_pays_naissance_unite_legale = d.pop("codePaysNaissanceUniteLegale", UNSET)

        libelle_nationalite_unite_legale = d.pop("libelleNationaliteUniteLegale", UNSET)

        identifiant_association_unite_legale = d.pop(
            "identifiantAssociationUniteLegale", UNSET
        )
        if identifiant_association_unite_legale is None:
            identifiant_association_unite_legale = UNSET

        tranche_effectifs_unite_legale = d.pop("trancheEffectifsUniteLegale", UNSET)

        annee_effectifs_unite_legale = d.pop("anneeEffectifsUniteLegale", UNSET)

        date_dernier_traitement_unite_legale = d.pop(
            "dateDernierTraitementUniteLegale", UNSET
        )

        nombre_periodes_unite_legale = d.pop("nombrePeriodesUniteLegale", UNSET)

        _categorie_entreprise = d.pop("categorieEntreprise", UNSET)
        categorie_entreprise: Unset | UniteLegaleCategorieEntreprise
        if isinstance(_categorie_entreprise, Unset) or _categorie_entreprise is None:
            categorie_entreprise = UNSET
        else:
            categorie_entreprise = UniteLegaleCategorieEntreprise(_categorie_entreprise)

        annee_categorie_entreprise = d.pop("anneeCategorieEntreprise", UNSET)

        sigle_unite_legale = d.pop("sigleUniteLegale", UNSET)

        _sexe_unite_legale = d.pop("sexeUniteLegale", UNSET)
        sexe_unite_legale: Unset | UniteLegaleSexeUniteLegale
        if isinstance(_sexe_unite_legale, Unset) or _sexe_unite_legale is None:
            sexe_unite_legale = UNSET
        else:
            sexe_unite_legale = UniteLegaleSexeUniteLegale(_sexe_unite_legale)

        prenom_1_unite_legale = d.pop("prenom1UniteLegale", UNSET)
        if prenom_1_unite_legale is None:
            prenom_1_unite_legale = UNSET

        prenom_2_unite_legale = d.pop("prenom2UniteLegale", UNSET)
        if prenom_2_unite_legale is None:
            prenom_2_unite_legale = UNSET

        prenom_3_unite_legale = d.pop("prenom3UniteLegale", UNSET)
        if prenom_3_unite_legale is None:
            prenom_3_unite_legale = UNSET

        prenom_4_unite_legale = d.pop("prenom4UniteLegale", UNSET)
        if prenom_4_unite_legale is None:
            prenom_4_unite_legale = UNSET

        prenom_usuel_unite_legale = d.pop("prenomUsuelUniteLegale", UNSET)
        if prenom_usuel_unite_legale is None:
            prenom_usuel_unite_legale = UNSET

        pseudonyme_unite_legale = d.pop("pseudonymeUniteLegale", UNSET)
        if pseudonyme_unite_legale is None:
            pseudonyme_unite_legale = UNSET

        periodes_unite_legale = []
        _periodes_unite_legale = d.pop("periodesUniteLegale", UNSET)
        for periodes_unite_legale_item_data in _periodes_unite_legale or []:
            periodes_unite_legale_item = PeriodeUniteLegale.from_dict(
                periodes_unite_legale_item_data
            )

            periodes_unite_legale.append(periodes_unite_legale_item)

        unite_legale = cls(
            score=score,
            siren=siren,
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
            nombre_periodes_unite_legale=nombre_periodes_unite_legale,
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
            periodes_unite_legale=periodes_unite_legale,
        )

        unite_legale.additional_properties = d
        return unite_legale

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
