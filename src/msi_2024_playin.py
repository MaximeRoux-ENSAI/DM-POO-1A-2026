"""Implémentation de la classe MSI2024PlayIn."""

from .match import Match
from .phase import Phase


class MSI2024PlayIn(Phase):
    """Play-In (qualifications) du MSI 2024.

    Parameters
    ----------
    equipes = dict[str, Equipe]
        Équipes participant aux qualifications.
    """

    @property
    def _CHAPEAUX(self) -> dict[str, set[str]]:
        chapeaux = {
            "Chapeau 1": {"KR #2", "CN #2"},
            "Chapeau 2": {"EMEA #2", "NA #2"},
            "Chapeau 3": {"APAC #1", "VN #1"},
            "Chapeau 4": {"LAT #1", "BR #1"},
        }
        return chapeaux

    @property
    def _TABLEAU_VIDE(self) -> dict[str, dict[str, dict[str, Match]]]:
        tableau_vide = {
            "Groupe A": {
                "Tour 1": {
                    "Match 1": Match(best_of=3),
                    "Match 2": Match(best_of=3),
                    "Match 3": Match(best_of=3),
                },
                "Tour 2": {
                    "Match 1": Match(best_of=3),
                    "Match 2": Match(best_of=3),
                },
            },
            "Groupe B": {
                "Tour 1": {
                    "Match 1": Match(best_of=3),
                    "Match 2": Match(best_of=3),
                    "Match 3": Match(best_of=3),
                },
                "Tour 2": {
                    "Match 1": Match(best_of=3),
                    "Match 2": Match(best_of=3),
                },
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
            "=================                                        ",
            "PHASE 1 (PLAY-IN)                                        ",
            "=================                                        ",
            "                                                         ",
            " ——————————                    ——————————                ",
            "| GROUPE A |                  | GROUPE B |               ",
            " ——————————                    ——————————                ",
            "                                                         ",
            " —————————       —————————     —————————       ————————— ",
            "| TOUR 1  |     | TOUR 2  |   | TOUR 1  |     | TOUR 2  |",
            " —————————       —————————     —————————       ————————— ",
            "                                                         ",
            " —————————                     —————————                 ",
            "| {!s:<3} | {} |                   | {!s:<3} | {} |                ".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 1"].equipe_1,
                self._tableau["Groupe A"]["Tour 1"]["Match 1"].score_equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 1"].equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 1"].score_equipe_1,
            ),
            "|—————————|——                 |—————————|——              ",
            "| {!s:<3} | {} |  |   —————————    | {!s:<3} | {} |  |   ————————— ".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 1"].equipe_2,
                self._tableau["Groupe A"]["Tour 1"]["Match 1"].score_equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 1"].equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 1"].score_equipe_2,
            ),
            " —————————    ——| {!s:<3} | {} |    —————————    ——| {!s:<3} | {} |".format(
                self._tableau["Groupe A"]["Tour 2"]["Match 1"].equipe_1,
                self._tableau["Groupe A"]["Tour 2"]["Match 1"].score_equipe_1,
                self._tableau["Groupe B"]["Tour 2"]["Match 1"].equipe_1,
                self._tableau["Groupe B"]["Tour 2"]["Match 1"].score_equipe_1,
            ),
            "                |—————————|                   |—————————|",
            " —————————    ——| {!s:<3} | {} |    —————————    ——| {!s:<3} | {} |".format(
                self._tableau["Groupe A"]["Tour 2"]["Match 1"].equipe_2,
                self._tableau["Groupe A"]["Tour 2"]["Match 1"].score_equipe_2,
                self._tableau["Groupe B"]["Tour 2"]["Match 1"].equipe_2,
                self._tableau["Groupe B"]["Tour 2"]["Match 1"].score_equipe_2,
            ),
            "| {!s:<3} | {} |  |   —————————    | {!s:<3} | {} |  |   ————————— ".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 2"].equipe_1,
                self._tableau["Groupe A"]["Tour 1"]["Match 2"].score_equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 2"].equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 2"].score_equipe_1,
            ),
            "|—————————|——                 |—————————|——              ",
            "| {!s:<3} | {} |                   | {!s:<3} | {} |                ".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 2"].equipe_2,
                self._tableau["Groupe A"]["Tour 1"]["Match 2"].score_equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 2"].equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 2"].score_equipe_2,
            ),
            " —————————                     —————————                 ",
            "             |   —————————                 |   ————————— ",
            " —————————    ——| {!s:<3} | {} |    —————————    ——| {!s:<3} | {} |".format(
                self._tableau["Groupe A"]["Tour 2"]["Match 2"].equipe_1,
                self._tableau["Groupe A"]["Tour 2"]["Match 2"].score_equipe_1,
                self._tableau["Groupe B"]["Tour 2"]["Match 2"].equipe_1,
                self._tableau["Groupe B"]["Tour 2"]["Match 2"].score_equipe_1,
            ),
            "| {!s:<3} | {} |     |—————————|   | {!s:<3} | {} |     |—————————|".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 3"].equipe_1,
                self._tableau["Groupe A"]["Tour 1"]["Match 3"].score_equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 3"].equipe_1,
                self._tableau["Groupe B"]["Tour 1"]["Match 3"].score_equipe_1,
            ),
            "|—————————|—————| {!s:<3} | {} |   |—————————|—————| {!s:<3} | {} |".format(
                self._tableau["Groupe A"]["Tour 2"]["Match 2"].equipe_2,
                self._tableau["Groupe A"]["Tour 2"]["Match 2"].score_equipe_2,
                self._tableau["Groupe B"]["Tour 2"]["Match 2"].equipe_2,
                self._tableau["Groupe B"]["Tour 2"]["Match 2"].score_equipe_2,
            ),
            "| {!s:<3} | {} |      —————————    | {!s:<3} | {} |      ————————— ".format(
                self._tableau["Groupe A"]["Tour 1"]["Match 3"].equipe_2,
                self._tableau["Groupe A"]["Tour 1"]["Match 3"].score_equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 3"].equipe_2,
                self._tableau["Groupe B"]["Tour 1"]["Match 3"].score_equipe_2,
            ),
            " —————————                     —————————                 ",
        ]

        return "\n".join(string_list)
