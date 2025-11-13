from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset

T = TypeVar("T", bound="Adresse")


@_attrs_define
class Adresse:
    """Ensemble des variables d'adresse d'un établissement

    Attributes:
        complement_adresse_etablissement (Union[Unset, str]): Complément d'adresse de l'établissement
        numero_voie_etablissement (Union[Unset, str]): Numéro dans la voie
        indice_repetition_etablissement (Union[Unset, str]): Indice de répétition dans la voie
        dernier_numero_voie_etablissement (Union[Unset, str]): Numéro de la dernière adresse dans la voie
        indice_repetition_dernier_numero_voie_etablissement (Union[Unset, str]): Indice de répétition de la dernière
            adresse dans la voie
        type_voie_etablissement (Union[Unset, str]): Type de la voie
        libelle_voie_etablissement (Union[Unset, str]): Libellé de la voie
        code_postal_etablissement (Union[Unset, str]): Code postal
        libelle_commune_etablissement (Union[Unset, str]): Libellé de la commune pour les adresses en France
        libelle_commune_etranger_etablissement (Union[Unset, str]): Libellé complémentaire pour une adresse à l'étranger
        distribution_speciale_etablissement (Union[Unset, str]): Distribution spéciale (BP par ex)
        code_commune_etablissement (Union[Unset, str]): Code commune de localisation de l'établissement hors
            établissements situés à l'étranger (Le code commune est défini dans le <a
            href='https://www.insee.fr/fr/information/2028028'>code officiel géographique (COG)</a>)
        code_cedex_etablissement (Union[Unset, str]): Numéro de Cedex
        libelle_cedex_etablissement (Union[Unset, str]): Libellé correspondant au numéro de Cedex (variable
            codeCedexEtablissement)
        code_pays_etranger_etablissement (Union[Unset, str]): Code pays pour les établissements situés à l'étranger
        libelle_pays_etranger_etablissement (Union[Unset, str]): Libellé du pays pour les adresses à l'étranger
        identifiant_adresse_etablissement (Union[Unset, str]): IdentifiantAdresseEtablissement
        coordonnee_lambert_abscisse_etablissement (Union[Unset, str]): coordonneeLambertAbscisseEtablissement
        coordonnee_lambert_ordonnee_etablissement (Union[Unset, str]): coordonneeLambertOrdonneeEtablissement
    """

    complement_adresse_etablissement: Unset | str = UNSET
    numero_voie_etablissement: Unset | str = UNSET
    indice_repetition_etablissement: Unset | str = UNSET
    dernier_numero_voie_etablissement: Unset | str = UNSET
    indice_repetition_dernier_numero_voie_etablissement: Unset | str = UNSET
    type_voie_etablissement: Unset | str = UNSET
    libelle_voie_etablissement: Unset | str = UNSET
    code_postal_etablissement: Unset | str = UNSET
    libelle_commune_etablissement: Unset | str = UNSET
    libelle_commune_etranger_etablissement: Unset | str = UNSET
    distribution_speciale_etablissement: Unset | str = UNSET
    code_commune_etablissement: Unset | str = UNSET
    code_cedex_etablissement: Unset | str = UNSET
    libelle_cedex_etablissement: Unset | str = UNSET
    code_pays_etranger_etablissement: Unset | str = UNSET
    libelle_pays_etranger_etablissement: Unset | str = UNSET
    identifiant_adresse_etablissement: Unset | str = UNSET
    coordonnee_lambert_abscisse_etablissement: Unset | str = UNSET
    coordonnee_lambert_ordonnee_etablissement: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        complement_adresse_etablissement = self.complement_adresse_etablissement

        numero_voie_etablissement = self.numero_voie_etablissement

        indice_repetition_etablissement = self.indice_repetition_etablissement

        dernier_numero_voie_etablissement = self.dernier_numero_voie_etablissement

        indice_repetition_dernier_numero_voie_etablissement = (
            self.indice_repetition_dernier_numero_voie_etablissement
        )

        type_voie_etablissement = self.type_voie_etablissement

        libelle_voie_etablissement = self.libelle_voie_etablissement

        code_postal_etablissement = self.code_postal_etablissement

        libelle_commune_etablissement = self.libelle_commune_etablissement

        libelle_commune_etranger_etablissement = (
            self.libelle_commune_etranger_etablissement
        )

        distribution_speciale_etablissement = self.distribution_speciale_etablissement

        code_commune_etablissement = self.code_commune_etablissement

        code_cedex_etablissement = self.code_cedex_etablissement

        libelle_cedex_etablissement = self.libelle_cedex_etablissement

        code_pays_etranger_etablissement = self.code_pays_etranger_etablissement

        libelle_pays_etranger_etablissement = self.libelle_pays_etranger_etablissement

        identifiant_adresse_etablissement = self.identifiant_adresse_etablissement

        coordonnee_lambert_abscisse_etablissement = (
            self.coordonnee_lambert_abscisse_etablissement
        )

        coordonnee_lambert_ordonnee_etablissement = (
            self.coordonnee_lambert_ordonnee_etablissement
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if complement_adresse_etablissement is not UNSET:
            field_dict["complementAdresseEtablissement"] = (
                complement_adresse_etablissement
            )
        if numero_voie_etablissement is not UNSET:
            field_dict["numeroVoieEtablissement"] = numero_voie_etablissement
        if indice_repetition_etablissement is not UNSET:
            field_dict["indiceRepetitionEtablissement"] = (
                indice_repetition_etablissement
            )
        if dernier_numero_voie_etablissement is not UNSET:
            field_dict["dernierNumeroVoieEtablissement"] = (
                dernier_numero_voie_etablissement
            )
        if indice_repetition_dernier_numero_voie_etablissement is not UNSET:
            field_dict["indiceRepetitionDernierNumeroVoieEtablissement"] = (
                indice_repetition_dernier_numero_voie_etablissement
            )
        if type_voie_etablissement is not UNSET:
            field_dict["typeVoieEtablissement"] = type_voie_etablissement
        if libelle_voie_etablissement is not UNSET:
            field_dict["libelleVoieEtablissement"] = libelle_voie_etablissement
        if code_postal_etablissement is not UNSET:
            field_dict["codePostalEtablissement"] = code_postal_etablissement
        if libelle_commune_etablissement is not UNSET:
            field_dict["libelleCommuneEtablissement"] = libelle_commune_etablissement
        if libelle_commune_etranger_etablissement is not UNSET:
            field_dict["libelleCommuneEtrangerEtablissement"] = (
                libelle_commune_etranger_etablissement
            )
        if distribution_speciale_etablissement is not UNSET:
            field_dict["distributionSpecialeEtablissement"] = (
                distribution_speciale_etablissement
            )
        if code_commune_etablissement is not UNSET:
            field_dict["codeCommuneEtablissement"] = code_commune_etablissement
        if code_cedex_etablissement is not UNSET:
            field_dict["codeCedexEtablissement"] = code_cedex_etablissement
        if libelle_cedex_etablissement is not UNSET:
            field_dict["libelleCedexEtablissement"] = libelle_cedex_etablissement
        if code_pays_etranger_etablissement is not UNSET:
            field_dict["codePaysEtrangerEtablissement"] = (
                code_pays_etranger_etablissement
            )
        if libelle_pays_etranger_etablissement is not UNSET:
            field_dict["libellePaysEtrangerEtablissement"] = (
                libelle_pays_etranger_etablissement
            )
        if identifiant_adresse_etablissement is not UNSET:
            field_dict["identifiantAdresseEtablissement"] = (
                identifiant_adresse_etablissement
            )
        if coordonnee_lambert_abscisse_etablissement is not UNSET:
            field_dict["coordonneeLambertAbscisseEtablissement"] = (
                coordonnee_lambert_abscisse_etablissement
            )
        if coordonnee_lambert_ordonnee_etablissement is not UNSET:
            field_dict["coordonneeLambertOrdonneeEtablissement"] = (
                coordonnee_lambert_ordonnee_etablissement
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        complement_adresse_etablissement = d.pop(
            "complementAdresseEtablissement", UNSET
        )

        numero_voie_etablissement = d.pop("numeroVoieEtablissement", UNSET)

        indice_repetition_etablissement = d.pop("indiceRepetitionEtablissement", UNSET)

        dernier_numero_voie_etablissement = d.pop(
            "dernierNumeroVoieEtablissement", UNSET
        )

        indice_repetition_dernier_numero_voie_etablissement = d.pop(
            "indiceRepetitionDernierNumeroVoieEtablissement", UNSET
        )

        type_voie_etablissement = d.pop("typeVoieEtablissement", UNSET)

        libelle_voie_etablissement = d.pop("libelleVoieEtablissement", UNSET)

        code_postal_etablissement = d.pop("codePostalEtablissement", UNSET)

        libelle_commune_etablissement = d.pop("libelleCommuneEtablissement", UNSET)

        libelle_commune_etranger_etablissement = d.pop(
            "libelleCommuneEtrangerEtablissement", UNSET
        )

        distribution_speciale_etablissement = d.pop(
            "distributionSpecialeEtablissement", UNSET
        )

        code_commune_etablissement = d.pop("codeCommuneEtablissement", UNSET)

        code_cedex_etablissement = d.pop("codeCedexEtablissement", UNSET)

        libelle_cedex_etablissement = d.pop("libelleCedexEtablissement", UNSET)

        code_pays_etranger_etablissement = d.pop("codePaysEtrangerEtablissement", UNSET)

        libelle_pays_etranger_etablissement = d.pop(
            "libellePaysEtrangerEtablissement", UNSET
        )

        identifiant_adresse_etablissement = d.pop(
            "identifiantAdresseEtablissement", UNSET
        )

        coordonnee_lambert_abscisse_etablissement = d.pop(
            "coordonneeLambertAbscisseEtablissement", UNSET
        )

        coordonnee_lambert_ordonnee_etablissement = d.pop(
            "coordonneeLambertOrdonneeEtablissement", UNSET
        )

        adresse = cls(
            complement_adresse_etablissement=complement_adresse_etablissement,
            numero_voie_etablissement=numero_voie_etablissement,
            indice_repetition_etablissement=indice_repetition_etablissement,
            dernier_numero_voie_etablissement=dernier_numero_voie_etablissement,
            indice_repetition_dernier_numero_voie_etablissement=indice_repetition_dernier_numero_voie_etablissement,
            type_voie_etablissement=type_voie_etablissement,
            libelle_voie_etablissement=libelle_voie_etablissement,
            code_postal_etablissement=code_postal_etablissement,
            libelle_commune_etablissement=libelle_commune_etablissement,
            libelle_commune_etranger_etablissement=libelle_commune_etranger_etablissement,
            distribution_speciale_etablissement=distribution_speciale_etablissement,
            code_commune_etablissement=code_commune_etablissement,
            code_cedex_etablissement=code_cedex_etablissement,
            libelle_cedex_etablissement=libelle_cedex_etablissement,
            code_pays_etranger_etablissement=code_pays_etranger_etablissement,
            libelle_pays_etranger_etablissement=libelle_pays_etranger_etablissement,
            identifiant_adresse_etablissement=identifiant_adresse_etablissement,
            coordonnee_lambert_abscisse_etablissement=coordonnee_lambert_abscisse_etablissement,
            coordonnee_lambert_ordonnee_etablissement=coordonnee_lambert_ordonnee_etablissement,
        )

        adresse.additional_properties = d
        return adresse

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
