from enum import Enum


class ReponseInformationsEtatService(str, Enum):
    """Service status values returned by the Sirene API."""

    UP = "UP"
    DOWN = "DOWN"

    def __str__(self) -> str:
        return str(self.value)
