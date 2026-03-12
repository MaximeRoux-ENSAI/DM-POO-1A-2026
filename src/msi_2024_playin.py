"""Implémentation de la classe MSI2024PlayIn."""

import random

from .match import Match
from .phase import Phase
from .equipe import Equipe


class MSI2024PlayIn(Phase):
    """Play-In (qualifications) du MSI 2024.

    Parameters
    ----------
    equipes = dict[str, Equipe]
        Équipes participant aux qualifications.
    """

    @property
    def _CHAPEAUX(self) -> dict[str, set[str]]:
        """Renvoyer la structure des chapeaux."""
        chapeaux = {
            "Chapeau 1": {"KR #2", "CN #2"},
            "Chapeau 2": {"EMEA #2", "NA #2"},
            "Chapeau 3": {"APAC #1", "VN #1"},
            "Chapeau 4": {"LAT #1", "BR #1"},
        }
        return chapeaux

    @property
    def _TABLEAU_VIDE(self) -> dict[str, dict[str, dict[str, Match]]]:
        """Renvoyer la structure vide du tableau de la phase."""
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

    # ------------------------------------------------------------------
    # Tirage
    # ------------------------------------------------------------------

    # Version rapide utilisant zip (non demandée mais conservée pour référence)
    #
    # def simuler_tirage_rapide(self) -> None:
    #     chapeaux = self._chapeaux_equipes
    #
    #     for groupe, equipe_c1, equipe_c2, equipe_c3, equipe_c4 in zip(
    #         ("Groupe A", "Groupe B"),
    #         random.sample(list(chapeaux["Chapeau 1"]), 2),
    #         random.sample(list(chapeaux["Chapeau 2"]), 2),
    #         random.sample(list(chapeaux["Chapeau 3"]), 2),
    #         random.sample(list(chapeaux["Chapeau 4"]), 2),
    #     ):
    #         self._tableau[groupe]["Tour 1"]["Match 1"].ajouter_equipes(
    #             equipe_c1,
    #             equipe_c4,
    #         )
    #
    #         self._tableau[groupe]["Tour 1"]["Match 2"].ajouter_equipes(
    #             equipe_c2,
    #             equipe_c3,
    #         )

    def simuler_tirage(self) -> None:
        """Simuler le tirage des groupes.

        Cette méthode répartit aléatoirement les équipes des quatre
        chapeaux dans les groupes A et B. Chaque groupe contient
        exactement une équipe de chaque chapeau.

        Les matchs du tour 1 sont ensuite initialisés selon les règles
        suivantes :

        - le match 1 oppose une équipe du chapeau 1 à une équipe du
        chapeau 4 ;
        - le match 2 oppose une équipe du chapeau 2 à une équipe du
        chapeau 3.
        """
        chapeau_1 = random.sample(list(self._chapeaux_equipes["Chapeau 1"]), 2)
        chapeau_2 = random.sample(list(self._chapeaux_equipes["Chapeau 2"]), 2)
        chapeau_3 = random.sample(list(self._chapeaux_equipes["Chapeau 3"]), 2)
        chapeau_4 = random.sample(list(self._chapeaux_equipes["Chapeau 4"]), 2)

        self._tableau["Groupe A"]["Tour 1"]["Match 1"].ajouter_equipes(
            chapeau_1[0],
            chapeau_4[0],
        )
        self._tableau["Groupe A"]["Tour 1"]["Match 2"].ajouter_equipes(
            chapeau_2[0],
            chapeau_3[0],
        )

        self._tableau["Groupe B"]["Tour 1"]["Match 1"].ajouter_equipes(
            chapeau_1[1],
            chapeau_4[1],
        )
        self._tableau["Groupe B"]["Tour 1"]["Match 2"].ajouter_equipes(
            chapeau_2[1],
            chapeau_3[1],
        )

    # ------------------------------------------------------------------
    # Simulation des tours
    # ------------------------------------------------------------------

    def __simuler_tour_1_matchs_1_2(self) -> None:
        """Simuler les matchs 1 et 2 du tour 1 de chaque groupe."""
        for groupe in ("Groupe A", "Groupe B"):

            m1 = self._tableau[groupe]["Tour 1"]["Match 1"]
            m2 = self._tableau[groupe]["Tour 1"]["Match 2"]

            m1.simuler()
            m2.simuler()

            self._tableau[groupe]["Tour 2"]["Match 1"].ajouter_equipes(
                m1.renvoyer_equipe_gagnante(),
                m2.renvoyer_equipe_gagnante(),
            )

            self._tableau[groupe]["Tour 1"]["Match 3"].ajouter_equipes(
                m1.renvoyer_equipe_perdante(),
                m2.renvoyer_equipe_perdante(),
            )

    def __simuler_tour_2_matchs_1(self) -> None:
        """Simuler le match 1 du tour 2 de chaque groupe."""
        for groupe in ("Groupe A", "Groupe B"):

            m = self._tableau[groupe]["Tour 2"]["Match 1"]
            m.simuler()

            self._tableau[groupe]["Tour 2"]["Match 2"].ajouter_equipe_1(
                m.renvoyer_equipe_perdante()
            )

    def __simuler_tour_1_matchs_3(self) -> None:
        """Simuler le match 3 du tour 1 de chaque groupe."""
        for groupe in ("Groupe A", "Groupe B"):

            m = self._tableau[groupe]["Tour 1"]["Match 3"]
            m.simuler()

            self._tableau[groupe]["Tour 2"]["Match 2"].ajouter_equipe_2(
                m.renvoyer_equipe_gagnante()
            )

    def __simuler_tour_2_matchs_2(self) -> None:
        """Simuler le match 2 du tour 2 de chaque groupe."""
        for groupe in ("Groupe A", "Groupe B"):

            m = self._tableau[groupe]["Tour 2"]["Match 2"]
            m.simuler()

    def simuler_tours(self) -> None:
        """Simuler l'ensemble des tours de la phase.

        Les tours sont simulés dans l'ordre suivant :

        1. matchs 1 et 2 du tour 1,
        2. matchs 1 du tour 2,
        3. matchs 3 du tour 1,
        4. matchs 2 du tour 2.
        """
        self.__simuler_tour_1_matchs_1_2()
        self.__simuler_tour_2_matchs_1()
        self.__simuler_tour_1_matchs_3()
        self.__simuler_tour_2_matchs_2()

    # ------------------------------------------------------------------
    # Classement
    # ------------------------------------------------------------------

    def renvoyer_classement(self) -> dict[str, set[Equipe]]:
        """Renvoyer le classement final de la phase.

        Returns
        -------
        dict[str, set[Equipe]]
            Dictionnaire représentant le classement de la phase.
            Les clés correspondent aux positions finales
            ("1-2", "3-4", "5-6", "7-8") et les valeurs sont les
            ensembles d'équipes associées.
        """
        classement = {
            "1-2": set(),
            "3-4": set(),
            "5-6": set(),
            "7-8": set(),
        }

        for groupe in ("Groupe A", "Groupe B"):

            classement["1-2"].add(
                self._tableau[groupe]["Tour 2"]["Match 1"].renvoyer_equipe_gagnante()
            )

            classement["3-4"].add(
                self._tableau[groupe]["Tour 2"]["Match 2"].renvoyer_equipe_gagnante()
            )

            classement["5-6"].add(
                self._tableau[groupe]["Tour 2"]["Match 2"].renvoyer_equipe_perdante()
            )

            classement["7-8"].add(
                self._tableau[groupe]["Tour 1"]["Match 3"].renvoyer_equipe_perdante()
            )

        return classement

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
