"""Tests pour la classe MSI2024."""

import pytest


def test_msi_2024_simuler(msi_2024_avant_tirages_et_resultats):
    """Vérifie qu'on peut renvoyer le classement après une simulation."""
    msi_2024 = msi_2024_avant_tirages_et_resultats
    msi_2024.simuler()
    assert isinstance(msi_2024.renvoyer_classement(), dict)


def test_msi_2024_renvoyer_classement(msi_2024_apres_tirages_et_resultats):
    resultat_renvoye = msi_2024_apres_tirages_et_resultats.renvoyer_classement()
    resultat_attendu = {
        "1": {pytest.gen},
        "2": {pytest.blg},
        "3": {pytest.t1},
        "4": {pytest.g2},
        "5-6": {pytest.tes, pytest.tl},
        "7-8": {pytest.fnc, pytest.psg},
        "9-10": {pytest.fly, pytest.gam},
        "11-12": {pytest.est, pytest.lll},
    }
    assert resultat_renvoye == resultat_attendu


def test_msi_2024_renvoyer_classement_str(msi_2024_apres_tirages_et_resultats):
    resultat_renvoye = msi_2024_apres_tirages_et_resultats.renvoyer_classement_str()

    resultat_attendu = "\n".join(
        [
            "=========                            ",
            "RESULTATS                            ",
            "=========                            ",
            "                                     ",
            " ——————————————————————————————————— ",
            "| Place |  Prix   | Équipe          |",
            "|———————|—————————|—————————————————|",
            "|   1   | $50,000 | Gen.G           |",
            "|———————|—————————|—————————————————|",
            "|   2   | $40,000 | Bilibili Gaming |",
            "|———————|—————————|—————————————————|",
            "|   3   | $30,000 | T1              |",
            "|———————|—————————|—————————————————|",
            "|   4   | $25,000 | G2 Esports      |",
            "|———————|—————————|—————————————————|",
            "|       |         | Team Liquid     |",
            "|  5—6  | $20,000 |—————————————————|",
            "|       |         | Top Esports     |",
            "|———————|—————————|—————————————————|",
            "|       |         | Fnatic          |",
            "|  7—8  | $15,000 |—————————————————|",
            "|       |         | PSG Talon       |",
            "|———————|—————————|—————————————————|",
            "|       |         | FlyQuest        |",
            "| 9—10  | $10,000 |—————————————————|",
            "|       |         | GAM Esports     |",
            "|———————|—————————|—————————————————|",
            "|       |         | Estral Esports  |",
            "| 11—12 | $7,500  |—————————————————|",
            "|       |         | LOUD            |",
            " ——————————————————————————————————— ",
        ]
    )

    assert resultat_renvoye == resultat_attendu


def test_msi_2024_afficher_resultats(msi_2024_apres_tirages_et_resultats):
    """Vérifie qu'afficher les résultats ne lève pas d'erreurs."""
    msi_2024_apres_tirages_et_resultats.afficher_resultats()
