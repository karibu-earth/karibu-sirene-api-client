from collections.abc import Mapping
import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sirene_api_client.api_types import UNSET, Unset

if TYPE_CHECKING:
    from sirene_api_client.models.adresse import Adresse
    from sirene_api_client.models.adresse_complementaire import AdresseComplementaire
    from sirene_api_client.models.periode_etablissement import PeriodeEtablissement
    from sirene_api_client.models.unite_legale_etablissement import (
        UniteLegaleEtablissement,
    )


T = TypeVar("T", bound="Etablissement")


@_attrs_define
class Etablissement:
    """Objet représentant un établissement et son historique

    Attributes:
        score (Union[Unset, float]): Score de l'élément parmi l'ensemble des éléments répondant à la requête, plus le
            score est élevé, plus l'élément est haut placé. Le score n'a pas de signification en dehors de la requête et
            n'est pas comparable aux score d'autres requêtes
        siren (Union[Unset, str]): Numéro Siren de l'entreprise à laquelle appartient l'établissement
        nic (Union[Unset, str]): Numéro interne de classement de l'établissement
        siret (Union[Unset, str]): Numéro Siret de l'établissement (toujours renseigné)
        statut_diffusion_etablissement (Union[Unset, str]): Statut de diffusion de l'établissement
        date_creation_etablissement (Union[Unset, datetime.date]): Date de création de l'établissement, format AAAA-MM-
            JJ
        tranche_effectifs_etablissement (Union[Unset, str]): Tranche d'effectif salarié de l'établissement, valorisée
            uniquement si l'année correspondante est supérieure ou égale à l'année d'interrogation -3 (sinon, NN)
        annee_effectifs_etablissement (Union[Unset, str]): Année de la tranche d'effectif salarié de l'établissement,
            valorisée uniquement si l'année est supérieure ou égale à l'année d'interrogation -3 (sinon, null)
        activite_principale_registre_metiers_etablissement (Union[Unset, str]): Code de l'activité exercée par l'artisan
            inscrit au registre des métiers. L'APRM est codifiée selon la nomenclature d'Activités Française de l'Artisanat
            (NAFA)
        date_dernier_traitement_etablissement (Union[Unset, datetime.datetime]): Date de la dernière mise à jour
            effectuée au répertoire Sirene sur le Siret concerné (yyyy-MM-ddTHH:mm:ss.SSS) Example: 2025-05-10
            15:18:50.255000.
        etablissement_siege (Union[Unset, bool]): Indicatrice précisant si le Siret est celui de l'établissement siège
            ou non
        nombre_periodes_etablissement (Union[Unset, int]): Nombre de périodes dans la vie de l'établissement
        unite_legale (Union[Unset, UniteLegaleEtablissement]): Objet représentant les valeurs courante de l'unité légale
            de l'établissement
        adresse_etablissement (Union[Unset, Adresse]): Ensemble des variables d'adresse d'un établissement
        adresse_2_etablissement (Union[Unset, AdresseComplementaire]): Ensemble des variables d'adresse complémentaire
            d'un établissement
        periodes_etablissement (Union[Unset, list['PeriodeEtablissement']]):
    """

    score: Unset | float = UNSET
    siren: Unset | str = UNSET
    nic: Unset | str = UNSET
    siret: Unset | str = UNSET
    statut_diffusion_etablissement: Unset | str = UNSET
    date_creation_etablissement: Unset | datetime.date = UNSET
    tranche_effectifs_etablissement: Unset | str = UNSET
    annee_effectifs_etablissement: Unset | str = UNSET
    activite_principale_registre_metiers_etablissement: Unset | str = UNSET
    date_dernier_traitement_etablissement: Unset | datetime.datetime = UNSET
    etablissement_siege: Unset | bool = UNSET
    nombre_periodes_etablissement: Unset | int = UNSET
    unite_legale: Union[Unset, "UniteLegaleEtablissement"] = UNSET
    adresse_etablissement: Union[Unset, "Adresse"] = UNSET
    adresse_2_etablissement: Union[Unset, "AdresseComplementaire"] = UNSET
    periodes_etablissement: Unset | list["PeriodeEtablissement"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        score = self.score

        siren = self.siren

        nic = self.nic

        siret = self.siret

        statut_diffusion_etablissement = self.statut_diffusion_etablissement

        date_creation_etablissement: Unset | str = UNSET
        if not isinstance(self.date_creation_etablissement, Unset):
            date_creation_etablissement = self.date_creation_etablissement.isoformat()

        tranche_effectifs_etablissement = self.tranche_effectifs_etablissement

        annee_effectifs_etablissement = self.annee_effectifs_etablissement

        activite_principale_registre_metiers_etablissement = (
            self.activite_principale_registre_metiers_etablissement
        )

        date_dernier_traitement_etablissement: Unset | str = UNSET
        if not isinstance(self.date_dernier_traitement_etablissement, Unset):
            date_dernier_traitement_etablissement = (
                self.date_dernier_traitement_etablissement.isoformat()
            )

        etablissement_siege = self.etablissement_siege

        nombre_periodes_etablissement = self.nombre_periodes_etablissement

        unite_legale: Unset | dict[str, Any] = UNSET
        if not isinstance(self.unite_legale, Unset):
            unite_legale = self.unite_legale.to_dict()

        adresse_etablissement: Unset | dict[str, Any] = UNSET
        if not isinstance(self.adresse_etablissement, Unset):
            adresse_etablissement = self.adresse_etablissement.to_dict()

        adresse_2_etablissement: Unset | dict[str, Any] = UNSET
        if not isinstance(self.adresse_2_etablissement, Unset):
            adresse_2_etablissement = self.adresse_2_etablissement.to_dict()

        periodes_etablissement: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.periodes_etablissement, Unset):
            periodes_etablissement = []
            for periodes_etablissement_item_data in self.periodes_etablissement:
                periodes_etablissement_item = periodes_etablissement_item_data.to_dict()
                periodes_etablissement.append(periodes_etablissement_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if score is not UNSET:
            field_dict["score"] = score
        if siren is not UNSET:
            field_dict["siren"] = siren
        if nic is not UNSET:
            field_dict["nic"] = nic
        if siret is not UNSET:
            field_dict["siret"] = siret
        if statut_diffusion_etablissement is not UNSET:
            field_dict["statutDiffusionEtablissement"] = statut_diffusion_etablissement
        if date_creation_etablissement is not UNSET:
            field_dict["dateCreationEtablissement"] = date_creation_etablissement
        if tranche_effectifs_etablissement is not UNSET:
            field_dict["trancheEffectifsEtablissement"] = (
                tranche_effectifs_etablissement
            )
        if annee_effectifs_etablissement is not UNSET:
            field_dict["anneeEffectifsEtablissement"] = annee_effectifs_etablissement
        if activite_principale_registre_metiers_etablissement is not UNSET:
            field_dict["activitePrincipaleRegistreMetiersEtablissement"] = (
                activite_principale_registre_metiers_etablissement
            )
        if date_dernier_traitement_etablissement is not UNSET:
            field_dict["dateDernierTraitementEtablissement"] = (
                date_dernier_traitement_etablissement
            )
        if etablissement_siege is not UNSET:
            field_dict["etablissementSiege"] = etablissement_siege
        if nombre_periodes_etablissement is not UNSET:
            field_dict["nombrePeriodesEtablissement"] = nombre_periodes_etablissement
        if unite_legale is not UNSET:
            field_dict["uniteLegale"] = unite_legale
        if adresse_etablissement is not UNSET:
            field_dict["adresseEtablissement"] = adresse_etablissement
        if adresse_2_etablissement is not UNSET:
            field_dict["adresse2Etablissement"] = adresse_2_etablissement
        if periodes_etablissement is not UNSET:
            field_dict["periodesEtablissement"] = periodes_etablissement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from sirene_api_client.models.adresse import Adresse
        from sirene_api_client.models.adresse_complementaire import (
            AdresseComplementaire,
        )
        from sirene_api_client.models.periode_etablissement import PeriodeEtablissement
        from sirene_api_client.models.unite_legale_etablissement import (
            UniteLegaleEtablissement,
        )

        d = dict(src_dict)
        score = d.pop("score", UNSET)

        siren = d.pop("siren", UNSET)

        nic = d.pop("nic", UNSET)

        siret = d.pop("siret", UNSET)

        statut_diffusion_etablissement = d.pop("statutDiffusionEtablissement", UNSET)

        _date_creation_etablissement = d.pop("dateCreationEtablissement", UNSET)
        date_creation_etablissement: Unset | datetime.date
        if (
            isinstance(_date_creation_etablissement, Unset)
            or _date_creation_etablissement is None
        ):
            date_creation_etablissement = UNSET
        else:
            date_creation_etablissement = isoparse(_date_creation_etablissement).date()

        tranche_effectifs_etablissement = d.pop("trancheEffectifsEtablissement", UNSET)

        annee_effectifs_etablissement = d.pop("anneeEffectifsEtablissement", UNSET)

        activite_principale_registre_metiers_etablissement = d.pop(
            "activitePrincipaleRegistreMetiersEtablissement", UNSET
        )

        _date_dernier_traitement_etablissement = d.pop(
            "dateDernierTraitementEtablissement", UNSET
        )
        date_dernier_traitement_etablissement: Unset | datetime.datetime
        if (
            isinstance(_date_dernier_traitement_etablissement, Unset)
            or _date_dernier_traitement_etablissement is None
        ):
            date_dernier_traitement_etablissement = UNSET
        else:
            date_dernier_traitement_etablissement = isoparse(
                _date_dernier_traitement_etablissement
            )

        etablissement_siege = d.pop("etablissementSiege", UNSET)

        nombre_periodes_etablissement = d.pop("nombrePeriodesEtablissement", UNSET)

        _unite_legale = d.pop("uniteLegale", UNSET)
        unite_legale: Unset | UniteLegaleEtablissement
        if isinstance(_unite_legale, Unset):
            unite_legale = UNSET
        else:
            unite_legale = UniteLegaleEtablissement.from_dict(_unite_legale)

        _adresse_etablissement = d.pop("adresseEtablissement", UNSET)
        adresse_etablissement: Unset | Adresse
        if isinstance(_adresse_etablissement, Unset):
            adresse_etablissement = UNSET
        else:
            adresse_etablissement = Adresse.from_dict(_adresse_etablissement)

        _adresse_2_etablissement = d.pop("adresse2Etablissement", UNSET)
        adresse_2_etablissement: Unset | AdresseComplementaire
        if isinstance(_adresse_2_etablissement, Unset):
            adresse_2_etablissement = UNSET
        else:
            adresse_2_etablissement = AdresseComplementaire.from_dict(
                _adresse_2_etablissement
            )

        periodes_etablissement = []
        _periodes_etablissement = d.pop("periodesEtablissement", UNSET)
        for periodes_etablissement_item_data in _periodes_etablissement or []:
            periodes_etablissement_item = PeriodeEtablissement.from_dict(
                periodes_etablissement_item_data
            )

            periodes_etablissement.append(periodes_etablissement_item)

        etablissement = cls(
            score=score,
            siren=siren,
            nic=nic,
            siret=siret,
            statut_diffusion_etablissement=statut_diffusion_etablissement,
            date_creation_etablissement=date_creation_etablissement,
            tranche_effectifs_etablissement=tranche_effectifs_etablissement,
            annee_effectifs_etablissement=annee_effectifs_etablissement,
            activite_principale_registre_metiers_etablissement=activite_principale_registre_metiers_etablissement,
            date_dernier_traitement_etablissement=date_dernier_traitement_etablissement,
            etablissement_siege=etablissement_siege,
            nombre_periodes_etablissement=nombre_periodes_etablissement,
            unite_legale=unite_legale,
            adresse_etablissement=adresse_etablissement,
            adresse_2_etablissement=adresse_2_etablissement,
            periodes_etablissement=periodes_etablissement,
        )

        etablissement.additional_properties = d
        return etablissement

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
