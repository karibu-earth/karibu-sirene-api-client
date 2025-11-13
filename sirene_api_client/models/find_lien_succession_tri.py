from enum import Enum


class FindLienSuccessionTri(str, Enum):
    SUCCESSEUR = "successeur"

    def __str__(self) -> str:
        return str(self.value)
