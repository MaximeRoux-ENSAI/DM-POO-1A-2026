"""Implémentation de la classe Match."""

import random

from src.equipe import Equipe


class Match:
    """Modéliser un match entre deux équipes.

    Parameters
    ----------
    best_of : int
        Le format du match.
        Il doit valoir 1, 3 ou 5.
    """

    BEST_OFS = (1, 3, 5)

    def __init__(self, best_of: int) -> None:
        if not isinstance(best_of, int):
            raise TypeError("Le best-of doit être un entier.")
        if best_of not in Match.BEST_OFS:
            raise ValueError("Le best-of doit valoir 1, 3 ou 5.")

        self.__best_of = best_of
        self.__equipe_1 = None
        self.__equipe_2 = None
        self.__score_equipe_1 = None
        self.__score_equipe_2 = None

    @property
    def best_of(self) -> int:
        """Renvoyer le format du match.

        Returns
        -------
        int
            La valeur du best-of.
        """
        return self.__best_of

    @property
    def equipe_1(self) -> Equipe | None:
        """Renvoyer l'équipe 1 du match.

        Returns
        -------
        Equipe | None
            L'équipe 1 si elle a été ajoutée, sinon None.
        """
        return self.__equipe_1

    @property
    def equipe_2(self) -> Equipe | None:
        """Renvoyer l'équipe 2 du match.

        Returns
        -------
        Equipe | None
            L'équipe 2 si elle a été ajoutée, sinon None.
        """
        return self.__equipe_2

    @property
    def score_equipe_1(self) -> int | None:
        """Renvoyer le score de l'équipe 1.

        Returns
        -------
        int | None
            Le score de l'équipe 1 s'il a été ajouté, sinon None.
        """
        return self.__score_equipe_1

    @property
    def score_equipe_2(self) -> int | None:
        """Renvoyer le score de l'équipe 2.

        Returns
        -------
        int | None
            Le score de l'équipe 2 s'il a été ajouté, sinon None.
        """
        return self.__score_equipe_2

    def __str__(self) -> str:
        equipe_1 = "" if self.equipe_1 is None else self.equipe_1.nom_abreviation
        equipe_2 = "" if self.equipe_2 is None else self.equipe_2.nom_abreviation
        score_1 = "" if self.score_equipe_1 is None else str(self.score_equipe_1)
        score_2 = "" if self.score_equipe_2 is None else str(self.score_equipe_2)

        ligne_horizontale = "-" * 11
        ligne_1 = f"| {equipe_1:<3} | {score_1} |"
        ligne_2 = f"| {equipe_2:<3} | {score_2} |"

        return "\n".join((ligne_horizontale, ligne_1, ligne_2, ligne_horizontale))

    def ajouter_equipe_1(self, equipe_1: Equipe) -> None:
        """Ajouter l'équipe 1 au match.

        Parameters
        ----------
        equipe : Equipe
            L'équipe à ajouter comme équipe 1.
        """
        if self.__equipe_1 is not None:
            raise ValueError("L'équipe 1 a déjà été ajoutée.")
        if not isinstance(equipe_1, Equipe):
            raise TypeError("L'équipe 1 doit être une équipe.")
        if self.__equipe_2 is not None and equipe_1 == self.__equipe_2:
            raise ValueError("Les deux équipes du match doivent être différentes.")

        self.__equipe_1 = equipe_1

    def ajouter_equipe_2(self, equipe_2: Equipe) -> None:
        """Ajouter l'équipe 2 au match.

        Parameters
        ----------
        equipe : Equipe
            L'équipe à ajouter comme équipe 2.
        """
        if self.__equipe_2 is not None:
            raise ValueError("L'équipe 2 a déjà été ajoutée.")
        if not isinstance(equipe_2, Equipe):
            raise TypeError("L'équipe 2 doit être une équipe.")
        if self.__equipe_1 is not None and equipe_2 == self.__equipe_1:
            raise ValueError("Les deux équipes du match doivent être différentes.")

        self.__equipe_2 = equipe_2

    def ajouter_equipes(self, equipe_1: Equipe, equipe_2: Equipe) -> None:
        """Ajouter les deux équipes du match.

        Parameters
        ----------
        equipe_1 : Equipe
            L'équipe 1.
        equipe_2 : Equipe
            L'équipe 2.
        """
        self.ajouter_equipe_1(equipe_1)
        self.ajouter_equipe_2(equipe_2)

    def _scores_valides(self, score_equipe_1: int, score_equipe_2: int) -> bool:
        """Vérifier si deux scores sont compatibles avec le best-of.

        Parameters
        ----------
        score_equipe_1 : int
            Le score de l'équipe 1.
        score_equipe_2 : int
            Le score de l'équipe 2.

        Returns
        -------
        bool
            True si les scores sont valides, sinon False.
        """
        manches_a_gagner = self.best_of // 2 + 1

        if score_equipe_1 < 0 or score_equipe_2 < 0:
            return False
        if score_equipe_1 == score_equipe_2:
            return False
        if max(score_equipe_1, score_equipe_2) != manches_a_gagner:
            return False
        if min(score_equipe_1, score_equipe_2) >= manches_a_gagner:
            return False
        if score_equipe_1 + score_equipe_2 > self.best_of:
            return False

        return True

    def ajouter_scores(self, score_equipe_1: int, score_equipe_2: int) -> None:
        """Ajouter les scores des deux équipes.

        Parameters
        ----------
        score_equipe_1 : int
            Le score de l'équipe 1.
        score_equipe_2 : int
            Le score de l'équipe 2.
        """
        if self.__equipe_1 is None or self.__equipe_2 is None:
            raise ValueError("Les équipes du match doivent être ajoutées avant les scores.")
        if self.__score_equipe_1 is not None or self.__score_equipe_2 is not None:
            raise ValueError("Les scores du match ont déjà été ajoutés.")
        if not isinstance(score_equipe_1, int) or not isinstance(score_equipe_2, int):
            raise TypeError("Les scores doivent être des entiers.")
        if score_equipe_1 < 0 or score_equipe_2 < 0:
            raise ValueError("Les scores doivent être positifs ou nuls.")
        if not self._scores_valides(score_equipe_1, score_equipe_2):
            raise ValueError("Les scores fournis ne sont pas compatibles avec le best-of.")

        self.__score_equipe_1 = score_equipe_1
        self.__score_equipe_2 = score_equipe_2

    def ajouter_equipes_et_scores(
        self,
        equipe_1: Equipe,
        equipe_2: Equipe,
        score_equipe_1: int,
        score_equipe_2: int,
    ) -> None:
        """Ajouter les équipes puis les scores du match.

        Parameters
        ----------
        equipe_1 : Equipe
            L'équipe 1.
        equipe_2 : Equipe
            L'équipe 2.
        score_equipe_1 : int
            Le score de l'équipe 1.
        score_equipe_2 : int
            Le score de l'équipe 2.
        """
        self.ajouter_equipes(equipe_1, equipe_2)
        self.ajouter_scores(score_equipe_1, score_equipe_2)

    def renvoyer_equipe_gagnante(self) -> Equipe:
        """Renvoyer l'équipe gagnante du match.

        Returns
        -------
        Equipe
            L'équipe gagnante du match.
        """
        if self.__score_equipe_1 is None or self.__score_equipe_2 is None:
            raise ValueError("Les scores du match n'ont pas encore été ajoutés.")

        if self.__score_equipe_1 > self.__score_equipe_2:
            return self.__equipe_1
        return self.__equipe_2

    def renvoyer_equipe_perdante(self) -> Equipe:
        """Renvoyer l'équipe perdante du match.

        Returns
        -------
        Equipe
            L'équipe perdante du match.
        """
        if self.__score_equipe_1 is None or self.__score_equipe_2 is None:
            raise ValueError("Les scores du match n'ont pas encore été ajoutés.")

        if self.__score_equipe_1 < self.__score_equipe_2:
            return self.__equipe_1
        return self.__equipe_2

    def renvoyer_regions_equipes(self) -> set[str]:
        """Renvoyer l'ensemble des régions des équipes du match.

        Returns
        -------
        set[str]
            L'ensemble des régions des équipes ajoutées.
        """
        regions = set()

        if self.__equipe_1 is not None:
            regions.add(self.__equipe_1.region)
        if self.__equipe_2 is not None:
            regions.add(self.__equipe_2.region)

        return regions

    def simuler(self) -> None:
        """Simuler le match."""
        if self.__equipe_1 is None or self.__equipe_2 is None:
            raise ValueError("Les équipes du match doivent être ajoutées avant simulation.")
        if self.__score_equipe_1 is not None or self.__score_equipe_2 is not None:
            raise ValueError("Les scores du match ont déjà été ajoutés.")

        manches_a_gagner = self.best_of // 2 + 1
        score_equipe_1 = 0
        score_equipe_2 = 0

        while (
            score_equipe_1 < manches_a_gagner
            and score_equipe_2 < manches_a_gagner
        ):
            if random.random() < 0.5:
                score_equipe_1 += 1
            else:
                score_equipe_2 += 1

        self.__score_equipe_1 = score_equipe_1
        self.__score_equipe_2 = score_equipe_2
