from enum import Enum


class UniteLegaleCategorieEntreprise(str, Enum):
    PME = "PME"
    ETI = "ETI"
    GE = "GE"
    NULL = "null"

    def __str__(self) -> str:
        return str(self.value)
