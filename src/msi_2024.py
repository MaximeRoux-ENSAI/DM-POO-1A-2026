"""Implémentation de la classe MSI2024."""

from .equipe import Equipe
from .msi_2024_bracket import MSI2024Bracket
from .msi_2024_playin import MSI2024PlayIn
from .tournoi import Tournoi


class MSI2024(Tournoi):
    """Tournoi MSI 2024."""

    _CHAPEAUX = {
        "Chapeau Bracket": {"KR #1", "CN #1", "EMEA #1", "NA #1"},
        "Chapeau Play-In": {
            "KR #2",
            "CN #2",
            "EMEA #2",
            "NA #2",
            "APAC #1",
            "VN #1",
            "LAT #1",
            "BR #1",
        },
    }

    def simuler(self) -> None:
        """Simuler le tournoi complet.

        Returns
        -------
        None
        """
        play_in = MSI2024PlayIn()
        play_in.ajouter_equipes(
            {
                place: self._equipes[place]
                for place in self._CHAPEAUX["Chapeau Play-In"]
            }
        )
        play_in.simuler()
        self._phases["Play-In"] = play_in

        classement_play_in = play_in.renvoyer_classement()
        equipes_play_in = sorted(
            classement_play_in["1-2"] | classement_play_in["3-4"],
            key=lambda equipe: equipe.nom_officiel,
        )

        bracket = MSI2024Bracket()
        bracket.ajouter_equipes(
            {
                "KR #1": self._equipes["KR #1"],
                "CN #1": self._equipes["CN #1"],
                "EMEA #1": self._equipes["EMEA #1"],
                "NA #1": self._equipes["NA #1"],
                "Play-In #1": equipes_play_in[0],
                "Play-In #2": equipes_play_in[1],
                "Play-In #3": equipes_play_in[2],
                "Play-In #4": equipes_play_in[3],
            }
        )
        bracket.simuler()
        self._phases["Bracket"] = bracket

    def renvoyer_classement(self) -> dict[str, set[Equipe]]:
        """Renvoyer le classement final du tournoi.

        Returns
        -------
        dict[str, set[Equipe]]
            Dictionnaire associant chaque rang final aux équipes
            correspondantes.
        """
        classement_bracket = self._phases["Bracket"].renvoyer_classement()
        classement_play_in = self._phases["Play-In"].renvoyer_classement()

        return {
            "1": classement_bracket["1"],
            "2": classement_bracket["2"],
            "3": classement_bracket["3"],
            "4": classement_bracket["4"],
            "5-6": classement_bracket["5-6"],
            "7-8": classement_bracket["7-8"],
            "9-10": classement_play_in["5-6"],
            "11-12": classement_play_in["7-8"],
        }

    def renvoyer_classement_str(self) -> str:
        """Renvoie le classement sous la forme d'une chaîne de caractères.

        Returns
        -------
        str
            Chaîne de caractères présentant les résultats.
        """

        classement: dict[str, set[Equipe]] = self.renvoyer_classement()
        classement_sorted: dict[str, list[Equipe]] = {
            cle: sorted(valeur) for cle, valeur in classement.items()
        }

        cagnotte_str_dollar: dict[str, str] = {
            cle: f"${valeur:,}" for cle, valeur in self._cagnotte.items()
        }
        lar_prix: int = max(len(value) for value in cagnotte_str_dollar.values())
        lar_eq: int = max(len(equipe.nom_officiel) for equipe in self._equipes.values())

        string_list = [
            r"=========                            ",
            r"RESULTATS                            ",
            r"=========                            ",
            r"                                     ",
            r" ——————————————————————————————————— ",
            f'| Place | {"Prix":^{lar_prix}} | {"Équipe":<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|   1   | {cagnotte_str_dollar["1"]:^{lar_prix}} | {classement_sorted["1"].pop(0).nom_officiel:<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|   2   | {cagnotte_str_dollar["2"]:^{lar_prix}} | {classement_sorted["2"].pop(0).nom_officiel:<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|   3   | {cagnotte_str_dollar["3"]:^{lar_prix}} | {classement_sorted["3"].pop(0).nom_officiel:<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|   4   | {cagnotte_str_dollar["4"]:^{lar_prix}} | {classement_sorted["4"].pop(0).nom_officiel:<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|       |         | {classement_sorted["5-6"].pop(0).nom_officiel:<{lar_eq}} |',
            f'|  5—6  | {cagnotte_str_dollar["5-6"]:^{lar_prix}} |—————————————————|',
            f'|       |         | {classement_sorted["5-6"].pop(0).nom_officiel:<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|       |         | {classement_sorted["7-8"].pop(0).nom_officiel:<{lar_eq}} |',
            f'|  7—8  | {cagnotte_str_dollar["7-8"]:^{lar_prix}} |—————————————————|',
            f'|       |         | {classement_sorted["7-8"].pop(0).nom_officiel:<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|       |         | {classement_sorted["9-10"].pop(0).nom_officiel:<{lar_eq}} |',
            f'| 9—10  | {cagnotte_str_dollar["9-10"]:^{lar_prix}} |—————————————————|',
            f'|       |         | {classement_sorted["9-10"].pop(0).nom_officiel:<{lar_eq}} |',
            r"|———————|—————————|—————————————————|",
            f'|       |         | {classement_sorted["11-12"].pop(0).nom_officiel:<{lar_eq}} |',
            f'| 11—12 | {cagnotte_str_dollar["11-12"]:^{lar_prix}} |—————————————————|',
            f'|       |         | {classement_sorted["11-12"].pop(0).nom_officiel:<{lar_eq}} |',
            r" ——————————————————————————————————— ",
        ]

        return "\n".join(string_list)

    def renvoyer_resultats_str(self) -> str:
        """Renvoie les résultats sous la forme d'une chaîne de caractères.

        Returns
        -------
        str
            Chaîne de caractères présentant les résultats des deux phases
            et le classement final.
        """
        playin_str: str = self._phases["Play-In"].renvoyer_resultats_str()
        bracket_str: str = self._phases["Bracket"].renvoyer_resultats_str()
        classement_str: str = self.renvoyer_classement_str()

        largeur_max = max(
            max(
                max(len(string) for string in playin_str.split("\n")),
                max(len(string) for string in bracket_str.split("\n")),
            ),
            max(len(string) for string in classement_str.split("\n")),
        )

        trait = "-" * largeur_max
        ligne_vide = " " * largeur_max

        string = "\n".join(
            [
                ligne_vide,
                str(self),
                ligne_vide,
                trait,
                ligne_vide,
                playin_str,
                ligne_vide,
                trait,
                ligne_vide,
                bracket_str,
                ligne_vide,
                trait,
                ligne_vide,
                classement_str,
                ligne_vide,
                trait,
            ]
        )

        return string
