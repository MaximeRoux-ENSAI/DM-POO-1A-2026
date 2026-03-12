"""Implémentation de la classe abstraite Phase."""

from abc import abstractmethod
from copy import deepcopy

from src.competition import Competition


class Phase(Competition):
    """Modéliser une phase d'un tournoi."""

    def __init__(self) -> None:
        super().__init__()
        self._tableau = deepcopy(self._TABLEAU_VIDE)

    @property
    @abstractmethod
    def _CHAPEAUX(self):
        """Renvoyer les chapeaux de la phase."""

    @property
    @abstractmethod
    def _TABLEAU_VIDE(self):
        """Renvoyer le tableau vide de la phase."""

    @abstractmethod
    def _simuler_tirage(self) -> None:
        """Simuler le tirage de la phase."""

    @abstractmethod
    def _simuler_tours(self) -> None:
        """Simuler tous les tours de la phase."""

    def simuler(self) -> None:
        """Simuler toute la phase."""
        self._simuler_tirage()
        self._simuler_tours()
