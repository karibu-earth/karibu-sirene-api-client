from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sirene_api_client.api_types import UNSET, Unset

T = TypeVar("T", bound="EtablissementPostMultiCriteres")


@_attrs_define
class EtablissementPostMultiCriteres:
    """
    Attributes:
        q (Union[Unset, str]): Contenu de la requête multicritères, voir la documentation pour plus de précisions
            Default: ''.
        date (Union[Unset, str]): Date à laquelle on veut obtenir les valeurs des données historisées Default: ''.
        champs (Union[Unset, str]): Liste des champs demandés, séparés par des virgules Default: ''.
        nombre (Union[Unset, int]): Nombre d'éléments demandés dans la réponse, défaut 20 Default: 20.
        debut (Union[Unset, int]): Rang du premier élément demandé dans la réponse, défaut 0 Default: 0.
        masquer_valeurs_nulles (Union[Unset, bool]): Masque (true) ou affiche (false, par défaut) les attributs qui
            n'ont pas de valeur
        tri (Union[Unset, str]): Champs sur lesquels des tris seront effectués, séparés par des virgules. Tri sur siren
            par défaut Default: ''.
        curseur (Union[Unset, str]): Paramètre utilisé pour la pagination profonde, voir la documentation pour plus de
            précisions Default: ''.
        facette_champ (Union[Unset, str]): Liste des champs sur lesquels des comptages seront effectués, séparés par des
            virgules Default: ''.
    """

    q: Unset | str = ""
    date: Unset | str = ""
    champs: Unset | str = ""
    nombre: Unset | int = 20
    debut: Unset | int = 0
    masquer_valeurs_nulles: Unset | bool = UNSET
    tri: Unset | str = ""
    curseur: Unset | str = ""
    facette_champ: Unset | str = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        q = self.q

        date = self.date

        champs = self.champs

        nombre = self.nombre

        debut = self.debut

        masquer_valeurs_nulles = self.masquer_valeurs_nulles

        tri = self.tri

        curseur = self.curseur

        facette_champ = self.facette_champ

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if q is not UNSET and q != "":
            field_dict["q"] = q
        if date is not UNSET and date != "":
            field_dict["date"] = date
        if champs is not UNSET and champs != "":
            field_dict["champs"] = champs
        if nombre is not UNSET:
            field_dict["nombre"] = nombre
        if debut is not UNSET:
            field_dict["debut"] = debut
        if masquer_valeurs_nulles is not UNSET:
            field_dict["masquerValeursNulles"] = masquer_valeurs_nulles
        if tri is not UNSET and tri != "":
            field_dict["tri"] = tri
        if curseur is not UNSET and curseur != "":
            field_dict["curseur"] = curseur
        if facette_champ is not UNSET and facette_champ != "":
            field_dict["facette.champ"] = facette_champ

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        q = d.pop("q", UNSET)

        date = d.pop("date", UNSET)

        champs = d.pop("champs", UNSET)

        nombre = d.pop("nombre", UNSET)

        debut = d.pop("debut", UNSET)

        masquer_valeurs_nulles = d.pop("masquerValeursNulles", UNSET)

        tri = d.pop("tri", UNSET)

        curseur = d.pop("curseur", UNSET)

        facette_champ = d.pop("facette.champ", UNSET)

        etablissement_post_multi_criteres = cls(
            q=q,
            date=date,
            champs=champs,
            nombre=nombre,
            debut=debut,
            masquer_valeurs_nulles=masquer_valeurs_nulles,
            tri=tri,
            curseur=curseur,
            facette_champ=facette_champ,
        )

        etablissement_post_multi_criteres.additional_properties = d
        return etablissement_post_multi_criteres

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
