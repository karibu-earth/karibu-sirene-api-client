from enum import Enum


class PeriodeUniteLegaleEtatAdministratifUniteLegale(str, Enum):
    A = "A"
    C = "C"

    def __str__(self) -> str:
        return str(self.value)
