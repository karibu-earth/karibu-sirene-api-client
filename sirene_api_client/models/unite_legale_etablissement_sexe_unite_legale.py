from enum import Enum


class UniteLegaleEtablissementSexeUniteLegale(str, Enum):
    M = "M"
    F = "F"
    ND = "[ND]"
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
