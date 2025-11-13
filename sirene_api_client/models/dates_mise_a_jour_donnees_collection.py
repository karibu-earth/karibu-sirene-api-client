from enum import Enum


class DatesMiseAJourDonneesCollection(str, Enum):
    """Collection names for data update dates returned by the Sirene API."""

    UNITÉS_LÉGALES = "Unités Légales"
    ÉTABLISSEMENTS = "Établissements"
    LIENS_DE_SUCCESSION = "Liens de succession"

    def __str__(self) -> str:
        return str(self.value)
