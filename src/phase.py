"""Implémentation de la classe abstraite Phase."""

from abc import abstractmethod
from copy import deepcopy

from src.competition import Competition


class Phase(Competition):
    """Modéliser une phase d'un tournoi."""

    TABLEAU_VIDE = None

    def __init__(self) -> None:
        self._tableau = deepcopy(self.TABLEAU_VIDE)

    @abstractmethod
    def simuler_tirage(self) -> None:
        """Simuler le tirage de la phase."""
        ... # Ou pass à la place de ..., les deux sont possibles.


    @abstractmethod
    def simuler_tours(self) -> None:
        """Simuler tous les tours de la phase."""
        ... # Ou pass à la place de ..., les deux sont possibles.

    def simuler(self) -> None:
        """Simuler toute la phase."""
        self.simuler_tirage()
        self.simuler_tours()
