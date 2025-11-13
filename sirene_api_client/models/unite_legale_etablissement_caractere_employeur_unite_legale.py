from enum import Enum


class UniteLegaleEtablissementCaractereEmployeurUniteLegale(str, Enum):
    OUI = "O"
    NON = "N"
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
