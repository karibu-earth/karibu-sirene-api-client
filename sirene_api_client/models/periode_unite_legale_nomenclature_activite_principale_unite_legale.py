from enum import Enum


class PeriodeUniteLegaleNomenclatureActivitePrincipaleUniteLegale(str, Enum):
    NAP = "NAP"
    NAFREV1 = "NAFRev1"
    NAFREV2 = "NAFRev2"
    NAF1993 = "NAF1993"

    def __str__(self) -> str:
        return str(self.value)
