from enum import Enum


class UniteLegaleEtablissementEtatAdministratifUniteLegale(str, Enum):
    A = "A"
    C = "C"

    def __str__(self) -> str:
        return str(self.value)
