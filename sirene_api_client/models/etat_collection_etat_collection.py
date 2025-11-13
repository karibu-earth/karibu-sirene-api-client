from enum import Enum


class EtatCollectionEtatCollection(str, Enum):
    """Collection status values returned by the Sirene API."""

    UP = "UP"
    DOWN = "DOWN"

    def __str__(self) -> str:
        return str(self.value)
