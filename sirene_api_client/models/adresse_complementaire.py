from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset

T = TypeVar("T", bound="AdresseComplementaire")


@_attrs_define
class AdresseComplementaire:
    """Ensemble des variables d'adresse complémentaire d'un établissement

    Attributes:
        complement_adresse_2_etablissement (Union[Unset, str]): Complément d'adresse de l'établissement
        numero_voie_2_etablissement (Union[Unset, str]): Numéro dans la voie
        indice_repetition_2_etablissement (Union[Unset, str]): Indice de répétition dans la voie
        type_voie_2_etablissement (Union[Unset, str]): Type de la voie
        libelle_voie_2_etablissement (Union[Unset, str]): Libellé de la voie
        code_postal_2_etablissement (Union[Unset, str]): Code postal
        libelle_commune_2_etablissement (Union[Unset, str]): Libellé de la commune pour les adresses en France
        libelle_commune_etranger_2_etablissement (Union[Unset, str]): Libellé complémentaire pour une adresse à
            l'étranger
        distribution_speciale_2_etablissement (Union[Unset, str]): Distribution spéciale (BP par ex)
        code_commune_2_etablissement (Union[Unset, str]): Code commune de localisation de l'établissement hors
            établissements situés à l'étranger (Le code commune est défini dans le <a
            href='https://www.insee.fr/fr/information/2028028'>code officiel géographique (COG)</a>)
        code_cedex_2_etablissement (Union[Unset, str]): Numéro de Cedex
        libelle_cedex_2_etablissement (Union[Unset, str]): Libellé correspondant au numéro de Cedex (variable
            codeCedexEtablissement)
        code_pays_etranger_2_etablissement (Union[Unset, str]): Code pays pour les établissements situés à l'étranger
        libelle_pays_etranger_2_etablissement (Union[Unset, str]): Libellé du pays pour les adresses à l'étranger
    """

    complement_adresse_2_etablissement: Unset | str = UNSET
    numero_voie_2_etablissement: Unset | str = UNSET
    indice_repetition_2_etablissement: Unset | str = UNSET
    type_voie_2_etablissement: Unset | str = UNSET
    libelle_voie_2_etablissement: Unset | str = UNSET
    code_postal_2_etablissement: Unset | str = UNSET
    libelle_commune_2_etablissement: Unset | str = UNSET
    libelle_commune_etranger_2_etablissement: Unset | str = UNSET
    distribution_speciale_2_etablissement: Unset | str = UNSET
    code_commune_2_etablissement: Unset | str = UNSET
    code_cedex_2_etablissement: Unset | str = UNSET
    libelle_cedex_2_etablissement: Unset | str = UNSET
    code_pays_etranger_2_etablissement: Unset | str = UNSET
    libelle_pays_etranger_2_etablissement: Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        complement_adresse_2_etablissement = self.complement_adresse_2_etablissement

        numero_voie_2_etablissement = self.numero_voie_2_etablissement

        indice_repetition_2_etablissement = self.indice_repetition_2_etablissement

        type_voie_2_etablissement = self.type_voie_2_etablissement

        libelle_voie_2_etablissement = self.libelle_voie_2_etablissement

        code_postal_2_etablissement = self.code_postal_2_etablissement

        libelle_commune_2_etablissement = self.libelle_commune_2_etablissement

        libelle_commune_etranger_2_etablissement = (
            self.libelle_commune_etranger_2_etablissement
        )

        distribution_speciale_2_etablissement = (
            self.distribution_speciale_2_etablissement
        )

        code_commune_2_etablissement = self.code_commune_2_etablissement

        code_cedex_2_etablissement = self.code_cedex_2_etablissement

        libelle_cedex_2_etablissement = self.libelle_cedex_2_etablissement

        code_pays_etranger_2_etablissement = self.code_pays_etranger_2_etablissement

        libelle_pays_etranger_2_etablissement = (
            self.libelle_pays_etranger_2_etablissement
        )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if complement_adresse_2_etablissement is not UNSET:
            field_dict["complementAdresse2Etablissement"] = (
                complement_adresse_2_etablissement
            )
        if numero_voie_2_etablissement is not UNSET:
            field_dict["numeroVoie2Etablissement"] = numero_voie_2_etablissement
        if indice_repetition_2_etablissement is not UNSET:
            field_dict["indiceRepetition2Etablissement"] = (
                indice_repetition_2_etablissement
            )
        if type_voie_2_etablissement is not UNSET:
            field_dict["typeVoie2Etablissement"] = type_voie_2_etablissement
        if libelle_voie_2_etablissement is not UNSET:
            field_dict["libelleVoie2Etablissement"] = libelle_voie_2_etablissement
        if code_postal_2_etablissement is not UNSET:
            field_dict["codePostal2Etablissement"] = code_postal_2_etablissement
        if libelle_commune_2_etablissement is not UNSET:
            field_dict["libelleCommune2Etablissement"] = libelle_commune_2_etablissement
        if libelle_commune_etranger_2_etablissement is not UNSET:
            field_dict["libelleCommuneEtranger2Etablissement"] = (
                libelle_commune_etranger_2_etablissement
            )
        if distribution_speciale_2_etablissement is not UNSET:
            field_dict["distributionSpeciale2Etablissement"] = (
                distribution_speciale_2_etablissement
            )
        if code_commune_2_etablissement is not UNSET:
            field_dict["codeCommune2Etablissement"] = code_commune_2_etablissement
        if code_cedex_2_etablissement is not UNSET:
            field_dict["codeCedex2Etablissement"] = code_cedex_2_etablissement
        if libelle_cedex_2_etablissement is not UNSET:
            field_dict["libelleCedex2Etablissement"] = libelle_cedex_2_etablissement
        if code_pays_etranger_2_etablissement is not UNSET:
            field_dict["codePaysEtranger2Etablissement"] = (
                code_pays_etranger_2_etablissement
            )
        if libelle_pays_etranger_2_etablissement is not UNSET:
            field_dict["libellePaysEtranger2Etablissement"] = (
                libelle_pays_etranger_2_etablissement
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        complement_adresse_2_etablissement = d.pop(
            "complementAdresse2Etablissement", UNSET
        )

        numero_voie_2_etablissement = d.pop("numeroVoie2Etablissement", UNSET)

        indice_repetition_2_etablissement = d.pop(
            "indiceRepetition2Etablissement", UNSET
        )

        type_voie_2_etablissement = d.pop("typeVoie2Etablissement", UNSET)

        libelle_voie_2_etablissement = d.pop("libelleVoie2Etablissement", UNSET)

        code_postal_2_etablissement = d.pop("codePostal2Etablissement", UNSET)

        libelle_commune_2_etablissement = d.pop("libelleCommune2Etablissement", UNSET)

        libelle_commune_etranger_2_etablissement = d.pop(
            "libelleCommuneEtranger2Etablissement", UNSET
        )

        distribution_speciale_2_etablissement = d.pop(
            "distributionSpeciale2Etablissement", UNSET
        )

        code_commune_2_etablissement = d.pop("codeCommune2Etablissement", UNSET)

        code_cedex_2_etablissement = d.pop("codeCedex2Etablissement", UNSET)

        libelle_cedex_2_etablissement = d.pop("libelleCedex2Etablissement", UNSET)

        code_pays_etranger_2_etablissement = d.pop(
            "codePaysEtranger2Etablissement", UNSET
        )

        libelle_pays_etranger_2_etablissement = d.pop(
            "libellePaysEtranger2Etablissement", UNSET
        )

        adresse_complementaire = cls(
            complement_adresse_2_etablissement=complement_adresse_2_etablissement,
            numero_voie_2_etablissement=numero_voie_2_etablissement,
            indice_repetition_2_etablissement=indice_repetition_2_etablissement,
            type_voie_2_etablissement=type_voie_2_etablissement,
            libelle_voie_2_etablissement=libelle_voie_2_etablissement,
            code_postal_2_etablissement=code_postal_2_etablissement,
            libelle_commune_2_etablissement=libelle_commune_2_etablissement,
            libelle_commune_etranger_2_etablissement=libelle_commune_etranger_2_etablissement,
            distribution_speciale_2_etablissement=distribution_speciale_2_etablissement,
            code_commune_2_etablissement=code_commune_2_etablissement,
            code_cedex_2_etablissement=code_cedex_2_etablissement,
            libelle_cedex_2_etablissement=libelle_cedex_2_etablissement,
            code_pays_etranger_2_etablissement=code_pays_etranger_2_etablissement,
            libelle_pays_etranger_2_etablissement=libelle_pays_etranger_2_etablissement,
        )

        adresse_complementaire.additional_properties = d
        return adresse_complementaire

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
