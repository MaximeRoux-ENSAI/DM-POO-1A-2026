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

    def simuler_tirage(self) -> None:
        """Simuler le tirage du bracket."""
        chapeau_1 = list(self._chapeaux_equipes["Chapeau 1"])
        chapeau_2 = list(self._chapeaux_equipes["Chapeau 2"])
        chapeau_3 = list(self._chapeaux_equipes["Chapeau 3"])
        chapeau_4 = list(self._chapeaux_equipes["Chapeau 4"])

        self._tableau["Tour 1"]["Match 1"].ajouter_equipes(chapeau_1[0], chapeau_4[0])
        self._tableau["Tour 1"]["Match 2"].ajouter_equipes(chapeau_2[0], chapeau_3[0])
        self._tableau["Tour 1"]["Match 3"].ajouter_equipes(chapeau_1[1], chapeau_4[1])
        self._tableau["Tour 1"]["Match 4"].ajouter_equipes(chapeau_2[1], chapeau_3[1])

    def simuler_tours(self) -> None:
        """Simuler tous les tours du bracket."""
        for tour in self._tableau.values():
            for match in tour.values():
                if match.equipe_1 is not None and match.equipe_2 is not None:
                    match.simuler()

    def simuler(self) -> None:
        """Simuler la totalité du tournoi.

        Cette méthode simule successivement la phase de qualifications
        (Play-In) puis la phase finale (Bracket). Les phases simulées sont
        sauvegardées dans l'attribut protégé ``_phases``.
        """

        # Phase 1 : Play-In
        playin = MSI2024PlayIn()

        places_playin = playin.renvoyer_places()
        equipes_playin = {
            seed: equipe
            for seed, equipe in self._equipes.items()
            if seed in places_playin
        }

        playin.ajouter_equipes(equipes_playin)
        playin.simuler()

        # équipes qualifiées pour la phase finale
        classement_playin = playin.renvoyer_classement()

        qualifies_playin = (
            classement_playin["1-2"]
            | classement_playin["3-4"]
        )

        # Phase 2 : Bracket
        bracket = MSI2024Bracket()

        places_bracket = bracket.renvoyer_places()

        equipes_bracket = {
            seed: equipe
            for seed, equipe in self._equipes.items()
            if seed in places_bracket
        }

        # remplacer les seeds Play-In par les équipes qualifiées
        seeds_playin = sorted(
            [s for s in places_bracket if "Play-In" in s]
        )

        for seed, equipe in zip(seeds_playin, sorted(qualifies_playin)):
            equipes_bracket[seed] = equipe

        bracket.ajouter_equipes(equipes_bracket)
        bracket.simuler()

        self._phases = [playin, bracket]

    def renvoyer_classement(self) -> dict[str, set]:
        """Renvoyer le classement final du tournoi.

        Returns
        -------
        dict[str, set]
            Dictionnaire contenant le classement du tournoi.
            Les clés correspondent aux positions finales
            ("1", "2", "3", "4", "5-6", "7-8", "9-10", "11-12")
            et les valeurs sont les ensembles d'équipes
            correspondantes.
        """

        playin = self._phases[0]
        bracket = self._phases[1]

        classement_playin = playin.renvoyer_classement()

        finale = bracket._tableau["Tour 5"]["Match 1"]

        classement = {
            "1": {finale.renvoyer_equipe_gagnante()},
            "2": {finale.renvoyer_equipe_perdante()},
            "3": {
                bracket._tableau["Tour 4"]["Match 1"].renvoyer_equipe_perdante(),
                bracket._tableau["Tour 4"]["Match 2"].renvoyer_equipe_perdante(),
            },
            "4": set(),
            "5-6": set(),
            "7-8": set(),
            "9-10": classement_playin["5-6"],
            "11-12": classement_playin["7-8"],
        }

        return classement

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
