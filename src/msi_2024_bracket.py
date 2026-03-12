"""Implémentation de la classe MSI2024Bracket."""

import random

from .equipe import Equipe
from .match import Match
from .phase import Phase


class MSI2024Bracket(Phase):
    """Phase finale du MSI 2024."""

    _CHAPEAUX = {
        "Chapeau 1": {"KR #1", "CN #1"},
        "Chapeau 2": {"EMEA #1", "NA #1"},
        "Chapeau 3": {"Play-In #1", "Play-In #2"},
        "Chapeau 4": {"Play-In #3", "Play-In #4"},
    }

    _TABLEAU_VIDE = {
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

    def _simuler_tirage(self) -> None:
        """Simuler le tirage du bracket.

        Returns
        -------
        None
        """
        chapeau_1 = random.sample(list(self._chapeaux_equipes["Chapeau 1"]), 2)
        chapeau_2 = random.sample(list(self._chapeaux_equipes["Chapeau 2"]), 2)
        chapeau_3 = random.sample(list(self._chapeaux_equipes["Chapeau 3"]), 2)
        chapeau_4 = random.sample(list(self._chapeaux_equipes["Chapeau 4"]), 2)

        for gauche_3, droite_3 in ((chapeau_3[0], chapeau_3[1]), (chapeau_3[1], chapeau_3[0])):
            for gauche_4, droite_4 in ((chapeau_4[0], chapeau_4[1]), (chapeau_4[1], chapeau_4[0])):
                regions_gauche = {
                    chapeau_1[0].region,
                    gauche_4.region,
                    chapeau_2[0].region,
                    gauche_3.region,
                }
                regions_droite = {
                    chapeau_2[1].region,
                    droite_3.region,
                    chapeau_1[1].region,
                    droite_4.region,
                }

                if len(regions_gauche) == 4 and len(regions_droite) == 4:
                    self._tableau["Tour 1"]["Match 1"].ajouter_equipes(
                        equipe_1=chapeau_1[0],
                        equipe_2=gauche_4,
                    )
                    self._tableau["Tour 1"]["Match 2"].ajouter_equipes(
                        equipe_1=chapeau_2[0],
                        equipe_2=gauche_3,
                    )
                    self._tableau["Tour 1"]["Match 3"].ajouter_equipes(
                        equipe_1=chapeau_2[1],
                        equipe_2=droite_3,
                    )
                    self._tableau["Tour 1"]["Match 4"].ajouter_equipes(
                        equipe_1=chapeau_1[1],
                        equipe_2=droite_4,
                    )
                    return

        raise ValueError("Aucun tirage valide n'a pu être trouvé.")

    def __simuler_tour_1_matchs_1_a_4(self) -> None:
        """Simuler les matchs 1 à 4 du tour 1.

        Returns
        -------
        None
        """
        match_1 = self._tableau["Tour 1"]["Match 1"]
        match_2 = self._tableau["Tour 1"]["Match 2"]
        match_3 = self._tableau["Tour 1"]["Match 3"]
        match_4 = self._tableau["Tour 1"]["Match 4"]

        match_1.simuler()
        match_2.simuler()
        match_3.simuler()
        match_4.simuler()

        self._tableau["Tour 2"]["Match 1"].ajouter_equipes(
            equipe_1=match_1.renvoyer_equipe_gagnante(),
            equipe_2=match_2.renvoyer_equipe_gagnante(),
        )
        self._tableau["Tour 2"]["Match 2"].ajouter_equipes(
            equipe_1=match_3.renvoyer_equipe_gagnante(),
            equipe_2=match_4.renvoyer_equipe_gagnante(),
        )
        self._tableau["Tour 1"]["Match 5"].ajouter_equipes(
            equipe_1=match_1.renvoyer_equipe_perdante(),
            equipe_2=match_2.renvoyer_equipe_perdante(),
        )
        self._tableau["Tour 1"]["Match 6"].ajouter_equipes(
            equipe_1=match_3.renvoyer_equipe_perdante(),
            equipe_2=match_4.renvoyer_equipe_perdante(),
        )

    def __simuler_tour_2_matchs_1_2(self) -> None:
        """Simuler les matchs 1 et 2 du tour 2.

        Returns
        -------
        None
        """
        match_1 = self._tableau["Tour 2"]["Match 1"]
        match_2 = self._tableau["Tour 2"]["Match 2"]

        match_1.simuler()
        match_2.simuler()

        self._tableau["Tour 4"]["Match 1"].ajouter_equipes(
            equipe_1=match_1.renvoyer_equipe_gagnante(),
            equipe_2=match_2.renvoyer_equipe_gagnante(),
        )

    def __simuler_tour_1_matchs_5_6(self) -> None:
        """Simuler les matchs 5 et 6 du tour 1.

        Returns
        -------
        None
        """
        match_5 = self._tableau["Tour 1"]["Match 5"]
        match_6 = self._tableau["Tour 1"]["Match 6"]
        match_1 = self._tableau["Tour 2"]["Match 1"]
        match_2 = self._tableau["Tour 2"]["Match 2"]

        match_5.simuler()
        match_6.simuler()

        self._tableau["Tour 2"]["Match 3"].ajouter_equipes(
            equipe_1=match_2.renvoyer_equipe_perdante(),
            equipe_2=match_5.renvoyer_equipe_gagnante(),
        )
        self._tableau["Tour 2"]["Match 4"].ajouter_equipes(
            equipe_1=match_1.renvoyer_equipe_perdante(),
            equipe_2=match_6.renvoyer_equipe_gagnante(),
        )

    def __simuler_tour_2_matchs_3_4(self) -> None:
        """Simuler les matchs 3 et 4 du tour 2.

        Returns
        -------
        None
        """
        match_3 = self._tableau["Tour 2"]["Match 3"]
        match_4 = self._tableau["Tour 2"]["Match 4"]

        match_3.simuler()
        match_4.simuler()

        self._tableau["Tour 3"]["Match 1"].ajouter_equipes(
            equipe_1=match_3.renvoyer_equipe_gagnante(),
            equipe_2=match_4.renvoyer_equipe_gagnante(),
        )

    def __simuler_tour_4_match_1(self) -> None:
        """Simuler le match 1 du tour 4.

        Returns
        -------
        None
        """
        self._tableau["Tour 4"]["Match 1"].simuler()

    def __simuler_tour_3(self) -> None:
        """Simuler le tour 3.

        Returns
        -------
        None
        """
        self._tableau["Tour 3"]["Match 1"].simuler()

    def __simuler_tour_4_match_2(self) -> None:
        """Simuler le match 2 du tour 4.

        Returns
        -------
        None
        """
        match_3 = self._tableau["Tour 3"]["Match 1"]
        match_4_1 = self._tableau["Tour 4"]["Match 1"]

        self._tableau["Tour 4"]["Match 2"].ajouter_equipes(
            equipe_1=match_4_1.renvoyer_equipe_perdante(),
            equipe_2=match_3.renvoyer_equipe_gagnante(),
        )
        self._tableau["Tour 4"]["Match 2"].simuler()

    def __simuler_tour_5(self) -> None:
        """Simuler le tour 5.

        Returns
        -------
        None
        """
        match_4_1 = self._tableau["Tour 4"]["Match 1"]
        match_4_2 = self._tableau["Tour 4"]["Match 2"]

        self._tableau["Tour 5"]["Match 1"].ajouter_equipes(
            equipe_1=match_4_1.renvoyer_equipe_gagnante(),
            equipe_2=match_4_2.renvoyer_equipe_gagnante(),
        )
        self._tableau["Tour 5"]["Match 1"].simuler()

    def _simuler_tours(self) -> None:
        """Simuler tous les tours de la phase.

        Returns
        -------
        None
        """
        self.__simuler_tour_1_matchs_1_a_4()
        self.__simuler_tour_2_matchs_1_2()
        self.__simuler_tour_1_matchs_5_6()
        self.__simuler_tour_2_matchs_3_4()
        self.__simuler_tour_4_match_1()
        self.__simuler_tour_3()
        self.__simuler_tour_4_match_2()
        self.__simuler_tour_5()

    def renvoyer_classement(self) -> dict[str, set[Equipe]]:
        """Renvoyer le classement final de la phase.

        Returns
        -------
        dict[str, set[Equipe]]
            Classement final du bracket.
        """
        return {
            "1": {self._tableau["Tour 5"]["Match 1"].renvoyer_equipe_gagnante()},
            "2": {self._tableau["Tour 5"]["Match 1"].renvoyer_equipe_perdante()},
            "3": {self._tableau["Tour 4"]["Match 2"].renvoyer_equipe_perdante()},
            "4": {self._tableau["Tour 3"]["Match 1"].renvoyer_equipe_perdante()},
            "5-6": {
                self._tableau["Tour 2"]["Match 3"].renvoyer_equipe_perdante(),
                self._tableau["Tour 2"]["Match 4"].renvoyer_equipe_perdante(),
            },
            "7-8": {
                self._tableau["Tour 1"]["Match 5"].renvoyer_equipe_perdante(),
                self._tableau["Tour 1"]["Match 6"].renvoyer_equipe_perdante(),
            },
        }

    def renvoyer_resultats_str(self) -> str:
        """Renvoyer les résultats sous forme de chaîne de caractères.

        Returns
        -------
        str
            Chaîne de caractères présentant le bracket.
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
                self._tableau["Tour 1"]["Match 1"].equipe_1,
                self._tableau["Tour 1"]["Match 1"].score_equipe_1,
            ),
            "|—————————|——                                                              ",
            "| {!s:<3} | {} |  |   —————————                                                 ".format(
                self._tableau["Tour 1"]["Match 1"].equipe_2,
                self._tableau["Tour 1"]["Match 1"].score_equipe_2,
            ),
            " —————————    ——| {!s:<3} | {} |                                                ".format(
                self._tableau["Tour 2"]["Match 1"].equipe_1,
                self._tableau["Tour 2"]["Match 1"].score_equipe_1,
            ),
            "                |—————————|                                                ",
            " —————————    ——| {!s:<3} | {} |——                                              ".format(
                self._tableau["Tour 2"]["Match 1"].equipe_2,
                self._tableau["Tour 2"]["Match 1"].score_equipe_2,
            ),
            "| {!s:<3} | {} |  |   —————————   |                                             ".format(
                self._tableau["Tour 1"]["Match 2"].equipe_1,
                self._tableau["Tour 1"]["Match 2"].score_equipe_1,
            ),
            "|—————————|——                |                                             ",
            "| {!s:<3} | {} |                  |                   —————————                 ".format(
                self._tableau["Tour 1"]["Match 2"].equipe_2,
                self._tableau["Tour 1"]["Match 2"].score_equipe_2,
            ),
            " —————————                    ——————————————————| {!s:<3} | {} |                ".format(
                self._tableau["Tour 4"]["Match 1"].equipe_1,
                self._tableau["Tour 4"]["Match 1"].score_equipe_1,
            ),
            "                                                |—————————|——              ",
            " —————————                    ——————————————————| {!s:<3} | {} |  |             ".format(
                self._tableau["Tour 4"]["Match 1"].equipe_2,
                self._tableau["Tour 4"]["Match 1"].score_equipe_2,
            ),
            "| {!s:<3} | {} |                  |                   —————————   |             ".format(
                self._tableau["Tour 1"]["Match 3"].equipe_1,
                self._tableau["Tour 1"]["Match 3"].score_equipe_1,
            ),
            "|—————————|——                |                               |             ",
            "| {!s:<3} | {} |  |   —————————   |                               |             ".format(
                self._tableau["Tour 1"]["Match 3"].equipe_2,
                self._tableau["Tour 1"]["Match 3"].score_equipe_2,
            ),
            " —————————    ——| {!s:<3} | {} |  |                               |             ".format(
                self._tableau["Tour 2"]["Match 2"].equipe_1,
                self._tableau["Tour 2"]["Match 2"].score_equipe_1,
            ),
            "                |—————————|——                                |   ————————— ",
            " —————————    ——| {!s:<3} | {} |                                   ——| {!s:<3} | {} |".format(
                self._tableau["Tour 2"]["Match 2"].equipe_2,
                self._tableau["Tour 2"]["Match 2"].score_equipe_2,
                self._tableau["Tour 5"]["Match 1"].equipe_1,
                self._tableau["Tour 5"]["Match 1"].score_equipe_1,
            ),
            "| {!s:<3} | {} |  |   —————————                                      |—————————|".format(
                self._tableau["Tour 1"]["Match 4"].equipe_1,
                self._tableau["Tour 1"]["Match 4"].score_equipe_1,
            ),
            "|—————————|——                                                 ——| {!s:<3} | {} |".format(
                self._tableau["Tour 5"]["Match 1"].equipe_2,
                self._tableau["Tour 5"]["Match 1"].score_equipe_2,
            ),
            "| {!s:<3} | {} |                                                  |   ————————— ".format(
                self._tableau["Tour 1"]["Match 4"].equipe_2,
                self._tableau["Tour 1"]["Match 4"].score_equipe_2,
            ),
            " —————————                                                   |             ",
            "             |   —————————                                   |             ",
            " —————————    ——| {!s:<3} | {} |                                  |             ".format(
                self._tableau["Tour 2"]["Match 3"].equipe_1,
                self._tableau["Tour 2"]["Match 3"].score_equipe_1,
            ),
            "| {!s:<3} | {} |     |—————————|——                |   —————————   |             ".format(
                self._tableau["Tour 1"]["Match 5"].equipe_1,
                self._tableau["Tour 1"]["Match 5"].score_equipe_1,
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
                self._tableau["Tour 4"]["Match 2"].equipe_2,
                self._tableau["Tour 4"]["Match 2"].score_equipe_2,
            ),
            "             |   —————————    ——| {!s:<3} | {} |      —————————                 ".format(
                self._tableau["Tour 3"]["Match 1"].equipe_2,
                self._tableau["Tour 3"]["Match 1"].score_equipe_2,
            ),
            " —————————    ——| {!s:<3} | {} |  |   —————————                                 ".format(
                self._tableau["Tour 2"]["Match 4"].equipe_1,
                self._tableau["Tour 2"]["Match 4"].score_equipe_1,
            ),
            "| {!s:<3} | {} |     |—————————|——                                              ".format(
                self._tableau["Tour 1"]["Match 6"].equipe_1,
                self._tableau["Tour 1"]["Match 6"].score_equipe_1,
            ),
            "|—————————|—————| {!s:<3} | {} |                                                ".format(
                self._tableau["Tour 2"]["Match 4"].equipe_2,
                self._tableau["Tour 2"]["Match 4"].score_equipe_2,
            ),
            "| {!s:<3} | {} |      —————————                                                 ".format(
                self._tableau["Tour 1"]["Match 6"].equipe_2,
                self._tableau["Tour 1"]["Match 6"].score_equipe_2,
            ),
            " —————————                                                                 ",
        ]

        return "\n".join(string_list)
