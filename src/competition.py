"""Implémentation de la classe Competition."""

from abc import ABC, abstractmethod

from .equipe import Equipe


class Competition(ABC):
    """Classe modélisant une compétition.

    Un tournoi et une phase d'un tournoi étant des compétitions, les caractéristiques et fonctionnalités communes sont
    regroupées dans cette classe mère.
    """

    @property
    @abstractmethod
    def _CHAPEAUX(self) -> dict[str, set[str]]: ...

    def renvoyer_places(self) -> set[str]:
        res: set[str] = set()
        for value in self._CHAPEAUX.values():
            res |= value
        return res

    def ajouter_equipes(self, equipes: dict[str, Equipe]) -> None:
        """Ajoute les équipes participant à la compétition.

        Parameters
        ----------
        equipes : dict[str, Equipe]
            Dictionnaire indiquant les têtes de séries et chaque équipe associée.
        """
        if not (
            isinstance(equipes, dict)
            and all(isinstance(key, str) for key in equipes.keys())
            and set(equipes.keys()) == self.renvoyer_places()
            and all(isinstance(value, Equipe) for value in equipes.values())
        ):
            raise ValueError("Les données fournies en argument sont mal formatées.")

        self._equipes: dict[str, Equipe] = equipes

        # Remplacement des têtes de série par les équipes
        chapeaux = self._CHAPEAUX
        self._chapeaux_equipes: dict[str, list[Equipe]] = {
            chapeau: sorted([self._equipes[seed] for seed in chapeaux[chapeau]]) for chapeau in chapeaux
        }

    @abstractmethod
    def simuler(self) -> None:
        """Simule la compétition."""
        ...

    @abstractmethod
    def renvoyer_classement(self) -> dict[str, set[Equipe]]:
        """Renvoie le classement de la phase de qualifications.

        Returns
        -------
        dict[str, set[Equipe]]
            Classement des équipes participantes.
        """
        ...

    @abstractmethod
    def renvoyer_resultats_str(self) -> str:
        """Renvoie les résultats sous la forme d'une chaîne de caractères.

        Returns
        -------
        str
            Chaîne de caractères présentant les résultats.
        """
        ...

    def afficher_resultats(self) -> None:
        """Affiche les résultats dans la sortie standard."""
        print(self.renvoyer_resultats_str())
