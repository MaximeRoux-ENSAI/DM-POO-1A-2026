"""Implémentation de la classe MSI2024Bracket."""

from .match import Match
from .phase import Phase


class MSI2024Bracket(Phase):
    """Phase finale du MSI 2024.

    Parameters
    ----------
    equipes = dict[str, Equipe]
        Équipes participant à la phase finale.
    """

    @property
    def _CHAPEAUX(self) -> dict[str, set[str]]:
        chapeaux = {
            "Chapeau 1": {"KR #1", "CN #1"},
            "Chapeau 2": {"EMEA #1", "NA #1"},
            "Chapeau 3": {"Play-In #1", "Play-In #2"},
            "Chapeau 4": {"Play-In #3", "Play-In #4"},
        }
        return chapeaux

    @property
    def _TABLEAU_VIDE(self) -> dict[str, dict[str, Match]]:
        tableau_vide = {
            "Tour 1": {
                "Match 1": Match(best_of=5),
                "Match 2": Match(best_of=5),
                "Match 3": Match(best_of=5),
                "Match 4": Match(best_of=5),
                "Match 5": Match(best_of=5),
                "Match 6": Match(best_of=5),
            },
            "Tour 2": {
                "Match 1": Match(best_of=5),
                "Match 2": Match(best_of=5),
                "Match 3": Match(best_of=5),
                "Match 4": Match(best_of=5),
            },
            "Tour 3": {
                "Match 1": Match(best_of=5),
            },
            "Tour 4": {
                "Match 1": Match(best_of=5),
                "Match 2": Match(best_of=5),
            },
            "Tour 5": {
                "Match 1": Match(best_of=5),
            },
        }
        return tableau_vide

    def renvoyer_resultats_str(self) -> str:
        """Renvoie les résultats sous la forme d'une chaîne de caractères.

        Returns
        -------
        str
            Chaîne de caractères présentant les résultats.
        """

        string_list = [
            "=================                                                          ",
            "PHASE 2 (BRACKET)                                                          ",
            "=================                                                          ",
            "                                                                           ",
            "                                                                           ",
            " —————————       —————————       —————————       —————————       ————————— ",
            "| TOUR 1  |     | TOUR 2  |     | TOUR 3  |     | TOUR 4  |     | TOUR 5  |",
            " —————————       —————————       —————————       —————————       ————————— ",
            "                                                                           ",
            " —————————                                                                 ",
            "| {!s:<3} | {} |                                                                ".format(
                self._tableau["Tour 1"]["Match 1"].equipe_1, self._tableau["Tour 1"]["Match 1"].score_equipe_1
            ),
            "|—————————|——                                                              ",
            "| {!s:<3} | {} |  |   —————————                                                 ".format(
                self._tableau["Tour 1"]["Match 1"].equipe_2, self._tableau["Tour 1"]["Match 1"].score_equipe_2
            ),
            " —————————    ——| {!s:<3} | {} |                                                ".format(
                self._tableau["Tour 2"]["Match 1"].equipe_1, self._tableau["Tour 2"]["Match 1"].score_equipe_1
            ),
            "                |—————————|                                                ",
            " —————————    ——| {!s:<3} | {} |——                                              ".format(
                self._tableau["Tour 2"]["Match 1"].equipe_2, self._tableau["Tour 2"]["Match 1"].score_equipe_2
            ),
            "| {!s:<3} | {} |  |   —————————   |                                             ".format(
                self._tableau["Tour 1"]["Match 2"].equipe_1, self._tableau["Tour 1"]["Match 2"].score_equipe_1
            ),
            "|—————————|——                |                                             ",
            "| {!s:<3} | {} |                  |                   —————————                 ".format(
                self._tableau["Tour 1"]["Match 2"].equipe_2, self._tableau["Tour 1"]["Match 2"].score_equipe_2
            ),
            " —————————                    ——————————————————| {!s:<3} | {} |                ".format(
                self._tableau["Tour 4"]["Match 1"].equipe_1, self._tableau["Tour 4"]["Match 1"].score_equipe_1
            ),
            "                                                |—————————|——              ",
            " —————————                    ——————————————————| {!s:<3} | {} |  |             ".format(
                self._tableau["Tour 4"]["Match 1"].equipe_2, self._tableau["Tour 4"]["Match 1"].score_equipe_2
            ),
            "| {!s:<3} | {} |                  |                   —————————   |             ".format(
                self._tableau["Tour 1"]["Match 3"].equipe_1, self._tableau["Tour 1"]["Match 3"].score_equipe_1
            ),
            "|—————————|——                |                               |             ",
            "| {!s:<3} | {} |  |   —————————   |                               |             ".format(
                self._tableau["Tour 1"]["Match 3"].equipe_2, self._tableau["Tour 1"]["Match 3"].score_equipe_2
            ),
            " —————————    ——| {!s:<3} | {} |  |                               |             ".format(
                self._tableau["Tour 2"]["Match 2"].equipe_1, self._tableau["Tour 2"]["Match 2"].score_equipe_1
            ),
            "                |—————————|——                                |   ————————— ",
            " —————————    ——| {!s:<3} | {} |                                   ——| {!s:<3} | {} |".format(
                self._tableau["Tour 2"]["Match 2"].equipe_2,
                self._tableau["Tour 2"]["Match 2"].score_equipe_2,
                self._tableau["Tour 5"]["Match 1"].equipe_1,
                self._tableau["Tour 5"]["Match 1"].score_equipe_1,
            ),
            "| {!s:<3} | {} |  |   —————————                                      |—————————|".format(
                self._tableau["Tour 1"]["Match 4"].equipe_1, self._tableau["Tour 1"]["Match 4"].score_equipe_1
            ),
            "|—————————|——                                                 ——| {!s:<3} | {} |".format(
                self._tableau["Tour 5"]["Match 1"].equipe_2, self._tableau["Tour 5"]["Match 1"].score_equipe_2
            ),
            "| {!s:<3} | {} |                                                  |   ————————— ".format(
                self._tableau["Tour 1"]["Match 4"].equipe_2, self._tableau["Tour 1"]["Match 4"].score_equipe_2
            ),
            " —————————                                                   |             ",
            "             |   —————————                                   |             ",
            " —————————    ——| {!s:<3} | {} |                                  |             ".format(
                self._tableau["Tour 2"]["Match 3"].equipe_1, self._tableau["Tour 2"]["Match 3"].score_equipe_1
            ),
            "| {!s:<3} | {} |     |—————————|——                |   —————————   |             ".format(
                self._tableau["Tour 1"]["Match 5"].equipe_1, self._tableau["Tour 1"]["Match 5"].score_equipe_1
            ),
            "|—————————|—————| {!s:<3} | {} |  |   —————————    ——| {!s:<3} | {} |  |             ".format(
                self._tableau["Tour 2"]["Match 3"].equipe_2,
                self._tableau["Tour 2"]["Match 3"].score_equipe_2,
                self._tableau["Tour 4"]["Match 2"].equipe_1,
                self._tableau["Tour 4"]["Match 2"].score_equipe_1,
            ),
            "| {!s:<3} | {} |      —————————    ——| {!s:<3} | {} |     |—————————|——              ".format(
                self._tableau["Tour 1"]["Match 5"].equipe_2,
                self._tableau["Tour 1"]["Match 5"].score_equipe_2,
                self._tableau["Tour 3"]["Match 1"].equipe_1,
                self._tableau["Tour 3"]["Match 1"].score_equipe_1,
            ),
            " —————————                      |—————————|—————| {!s:<3} | {} |                ".format(
                self._tableau["Tour 4"]["Match 2"].equipe_2, self._tableau["Tour 4"]["Match 2"].score_equipe_2
            ),
            "             |   —————————    ——| {!s:<3} | {} |      —————————                 ".format(
                self._tableau["Tour 3"]["Match 1"].equipe_2, self._tableau["Tour 3"]["Match 1"].score_equipe_2
            ),
            " —————————    ——| {!s:<3} | {} |  |   —————————                                 ".format(
                self._tableau["Tour 2"]["Match 4"].equipe_1, self._tableau["Tour 2"]["Match 4"].score_equipe_1
            ),
            "| {!s:<3} | {} |     |—————————|——                                              ".format(
                self._tableau["Tour 1"]["Match 6"].equipe_1, self._tableau["Tour 1"]["Match 6"].score_equipe_1
            ),
            "|—————————|—————| {!s:<3} | {} |                                                ".format(
                self._tableau["Tour 2"]["Match 4"].equipe_2, self._tableau["Tour 2"]["Match 4"].score_equipe_2
            ),
            "| {!s:<3} | {} |      —————————                                                 ".format(
                self._tableau["Tour 1"]["Match 6"].equipe_2, self._tableau["Tour 1"]["Match 6"].score_equipe_2
            ),
            " —————————                                                                 ",
        ]

        return "\n".join(string_list)
