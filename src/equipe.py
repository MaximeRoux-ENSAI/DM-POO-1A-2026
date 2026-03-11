"""Implémentation de la classe Equipe."""

from src.coach import Coach
from src.joueur import Joueur


class Equipe:
    """Modéliser une équipe.

    Parameters
    ----------
    nom_officiel : str
        Le nom officiel de l'équipe.
    nom_abreviation : str
        Le nom abrégé de l'équipe de 2 à 3 caractères
        alphanumériques en majuscules.
    region : str
        La région dans laquelle évolue l'équipe.
    joueurs : tuple[Joueur]
        Un t-uplet de 5 joueurs uniques.
    coachs : tuple[Coach]
        Un t-uplet de 1 à 2 coachs uniques.
    """

    REGIONS = ("KR", "CN", "EMEA", "NA", "APAC", "VN", "BR", "LAT")

    def __init__(
        self,
        nom_officiel: str,
        nom_abreviation: str,
        region: str,
        joueurs: tuple[Joueur],
        coachs: tuple[Coach],
    ) -> None:
        if not isinstance(nom_officiel, str):
            raise TypeError(
                "Le nom officiel doit être une chaîne de caractères."
            )
        if not isinstance(nom_abreviation, str):
            raise TypeError(
                "Le nom abrégé doit être une chaîne de caractères."
            )
        if not 2 <= len(nom_abreviation) <= 3:
            raise ValueError(
                "Le nom abrégé doit contenir entre 2 et 3 caractères."
            )
        if not nom_abreviation.isalnum():
            raise ValueError(
                "Le nom abrégé doit être alphanumérique."
            )
        if not nom_abreviation.isupper():
            raise ValueError(
                "Le nom abrégé doit être en majuscules."
            )
        if not isinstance(region, str):
            raise TypeError("La région doit être une chaîne de caractères.")
        if region not in Equipe.REGIONS:
            raise ValueError(
                "La région doit être parmi "
                '"KR", "CN", "EMEA", "NA", "APAC", "VN", "BR", "LAT".'
            )
        if not isinstance(joueurs, tuple):
            raise TypeError("Les joueurs doivent être fournis dans un t-uplet.")
        if len(joueurs) != 5:
            raise ValueError(
                "Les joueurs doivent être fournis dans un t-uplet de 5 joueurs."
            )
        if len(set(joueurs)) != 5:
            raise ValueError("Les 5 joueurs doivent être uniques.")
        if not all(isinstance(joueur, Joueur) for joueur in joueurs):
            raise TypeError(
                "Tous les éléments de joueurs doivent être des joueurs."
            )
        if not isinstance(coachs, tuple):
            raise TypeError("Les coachs doivent être fournis dans un t-uplet.")
        if not 1 <= len(coachs) <= 2:
            raise ValueError(
                "Les coachs doivent être fournis dans un t-uplet de 1 à 2 coachs."
            )
        if len(set(coachs)) != len(coachs):
            raise ValueError("Les coachs doivent être uniques.")
        if not all(isinstance(coach, Coach) for coach in coachs):
            raise TypeError(
                "Tous les éléments de coachs doivent être des coachs."
            )

        self.__nom_officiel = nom_officiel
        self.__nom_abreviation = nom_abreviation
        self.__region = region
        self.__joueurs = joueurs
        self.__coachs = coachs

    @property
    def nom_officiel(self) -> str:
        """Renvoyer le nom officiel de l'équipe.

        Returns
        -------
        str
            Le nom officiel de l'équipe.
        """
        return self.__nom_officiel

    @property
    def nom_abreviation(self) -> str:
        """Renvoyer le nom abrégé de l'équipe.

        Returns
        -------
        str
            Le nom abrégé de l'équipe.
        """
        return self.__nom_abreviation

    @property
    def region(self) -> str:
        """Renvoyer la région de l'équipe.

        Returns
        -------
        str
            La région de l'équipe.
        """
        return self.__region

    def __str__(self) -> str:
        return self.nom_abreviation

    def __repr__(self) -> str:
        return (
            f"Equipe({self.__nom_officiel!r}, {self.__nom_abreviation!r}, "
            f"{self.__region!r}, {self.__joueurs!r}, {self.__coachs!r})"
        )

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Equipe):
            return self.nom_officiel == other.nom_officiel
        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Equipe):
            return self.nom_officiel < other.nom_officiel
        return NotImplemented

    def __hash__(self) -> int:
        return hash(repr(self))
