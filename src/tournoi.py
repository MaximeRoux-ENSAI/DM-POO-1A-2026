"""Implémentation de la classe Tournoi."""

import datetime
import re
from abc import abstractmethod

from .competition import Competition


class Tournoi(Competition):
    """Classe de base abstraite pour un tournoi.

    Parameters
    ----------
    n_equipes : int
        Nombre d'équipes participant au tournoi.

    cagnotte : dict[str, int]
        Dictionnaire dont les clés sont les classements et les valeurs sont les prix.

    date_debut : datetime.date
        Date de début du tournoi.

    date_fin : datetime.date
        Date de fin du tournoi.
    """

    def __init__(
        self, n_equipes: int, cagnotte: dict[str, int], date_debut: datetime.date, date_fin: datetime.date
    ) -> None:
        if not (isinstance(n_equipes, int) and n_equipes >= 2):
            raise ValueError("Le nombre d'équipes doit être un entier supérieur ou égal à 2.")

        if not isinstance(cagnotte, dict):
            raise TypeError("La cagnotte doit être un dictionnaire.")
        self.__verifier_cles_cagnotte(cagnotte, n_equipes)
        self.__verifier_valeurs_cagnotte(cagnotte)

        if not isinstance(date_debut, datetime.date):
            raise TypeError("La date de début doit bien être une date.")
        if not isinstance(date_fin, datetime.date):
            raise TypeError("La date de fin doit bien être une date.")
        if not (date_debut <= date_fin):
            raise ValueError("La date de fin doit être postérieure à la date de début.")

        self.__n_equipes = n_equipes
        self._cagnotte = cagnotte
        self.__date_debut = date_debut
        self.__date_fin = date_fin
        self._phases: dict[str, Competition] = {}

    def __str__(self) -> str:
        string: str = (
            f"Un total de {self.__n_equipes} équipes participent à ce tournoi ayant lieu du {self.__date_debut} au "
            f"{self.__date_fin} avec une cagnotte totale de {self.calculer_cagnotte_totale()!s} dollars en jeu."
        )
        return string

    @abstractmethod
    def renvoyer_classement_str(self) -> str:
        """Renvoie le classement sous la forme d'une chaîne de caractères.

        Returns
        -------
        str
            Chaîne de caractères présentant les résultats.
        """
        ...

    @staticmethod
    def __verifier_nombre_str(string: str) -> list[int]:
        """Vérifie la validité d'une chaîne de caractères.

        La chaîne de caractères est valide si et seulement si l'une des conditions suivantes est vérifiée :
            - elle représente un nombre entier strictement positif (par exemple '1', '2', '6'), ou
            - elle représente une plage de nombres entiers strictement positifs (par exemple '1-2', '6-10').

        Parameters
        ----------
        string : str
            Chaîne de caractères.

        Returns
        -------
        list[int]
            Liste d'entiers correspondant à la chaîne de caractères.
        """
        if string.isdigit() and int(string) > 0:
            return [int(string)]
        else:
            if re.match(r"\d{1,}-\d{1,}", string):
                inf, sup = (int(x) for x in string.split("-"))
                if not (int(string.split("-")[0]) < int(string.split("-")[1])):
                    raise ValueError(f"La chaîne de caractères {string!r} n'est pas une clé valide.")
                return list(range(inf, sup + 1))
            else:
                raise ValueError(f"La chaîne de caractères {string!r} n'est pas une clé valide.")

    def __verifier_cles_cagnotte(self, cagnotte: dict[str, int], n_equipes: int) -> None:
        """Vérifie les clés du dictionnaire 'cagnotte'.

        Parameters
        ----------
        cagnotte : dict[str, int]
            Répartition de la cagnotte entre les équipes.

        n_equipes : int
            Nombre d'équipes participantes.
        """
        if not all(isinstance(cle, str) for cle in cagnotte.keys()):
            raise TypeError("Les clés du dictionnaire 'cagnotte' doivent être des chaînes de caractères.")

        # Génère puis trie la liste des rangs présents dans les clés
        liste_rangs = []
        for cle in cagnotte.keys():
            liste_rangs.extend(self.__verifier_nombre_str(cle))
        liste_rangs.sort()

        if liste_rangs != list(range(1, n_equipes + 1)):
            raise ValueError(
                "La répartition de la cagnotte n'est pas compatible avec le nombre d'équipes participantes."
            )

    def __verifier_valeurs_cagnotte(self, cagnotte: dict[str, int]) -> None:
        """Vérifie les valeurs du dictionnaire 'cagnotte'.

        Parameters
        ----------
        cagnotte : dict[str, int]
            Répartition de la cagnotte entre les équipes.
        """
        if not (
            all(isinstance(valeur, int) for valeur in cagnotte.values())
            and all(valeur >= 0 for valeur in cagnotte.values())
        ):
            raise ValueError("Les valeurs du dictionnaire 'cagnotte' doivent être des entiers positifs ou nuls.")

        prix_tries_par_rang: list[int] = list(
            dict(sorted(cagnotte.items(), key=lambda x: self.__verifier_nombre_str(x[0])[0])).values()
        )

        if prix_tries_par_rang != sorted(prix_tries_par_rang, reverse=True):
            raise ValueError(
                "La répartition de la cagnotte n'est pas valide : une équipe moins bien classée qu'une autre a une "
                "cagnotte strictement plus élevée."
            )

    def calculer_cagnotte_totale(self) -> int:
        """Calcule la cagnotte totale du tournoi.

        Returns
        -------
        int
            Cagnotte totale du tournoi.
        """
        cagnotte_totale: int = 0
        for cle, valeur in self._cagnotte.items():
            cagnotte_totale += len(self.__verifier_nombre_str(cle)) * valeur
        return cagnotte_totale
