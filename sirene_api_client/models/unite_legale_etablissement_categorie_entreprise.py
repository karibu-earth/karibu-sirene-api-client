from enum import Enum


class UniteLegaleEtablissementCategorieEntreprise(str, Enum):
    PME = "PME"
    ETI = "ETI"
    GE = "GE"
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
