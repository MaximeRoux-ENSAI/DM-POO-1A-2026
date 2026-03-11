"""Tests pour la classe MSI2024Bracket."""

import random

import pytest


@pytest.mark.parametrize("_", range(100))
def test_msi_2024_bracket_simuler_tirage(_, msi_2024_bracket_avant_tirage):
    random.seed(None)
    bracket = msi_2024_bracket_avant_tirage
    bracket._simuler_tirage()

    # Chapeau 1
    assert bracket._tableau["Tour 1"]["Match 1"].equipe_1 in (pytest.gen, pytest.blg)
    assert bracket._tableau["Tour 1"]["Match 4"].equipe_1 in (pytest.gen, pytest.blg)
    assert bracket._tableau["Tour 1"]["Match 1"].equipe_1 != bracket._tableau["Tour 1"]["Match 4"].equipe_1

    # Chapeau 2
    assert bracket._tableau["Tour 1"]["Match 2"].equipe_1 in (pytest.g2, pytest.tl)
    assert bracket._tableau["Tour 1"]["Match 3"].equipe_1 in (pytest.g2, pytest.tl)
    assert bracket._tableau["Tour 1"]["Match 2"].equipe_1 != bracket._tableau["Tour 1"]["Match 3"].equipe_1

    # Chapeau 3
    assert bracket._tableau["Tour 1"]["Match 2"].equipe_2 in (pytest.t1, pytest.tes)
    assert bracket._tableau["Tour 1"]["Match 3"].equipe_2 in (pytest.t1, pytest.tes)
    assert bracket._tableau["Tour 1"]["Match 2"].equipe_2 != bracket._tableau["Tour 1"]["Match 3"].equipe_2

    # Chapeau 4
    assert bracket._tableau["Tour 1"]["Match 1"].equipe_2 in (pytest.fnc, pytest.psg)
    assert bracket._tableau["Tour 1"]["Match 4"].equipe_2 in (pytest.fnc, pytest.psg)
    assert bracket._tableau["Tour 1"]["Match 1"].equipe_2 != bracket._tableau["Tour 1"]["Match 4"].equipe_2

    # Une seule équipe par région dans chaque partie du tableau
    assert (
        len(
            bracket._tableau["Tour 1"]["Match 1"].renvoyer_regions_equipes()
            | bracket._tableau["Tour 1"]["Match 2"].renvoyer_regions_equipes()
        )
        == 4
    )
    assert (
        len(
            bracket._tableau["Tour 1"]["Match 3"].renvoyer_regions_equipes()
            | bracket._tableau["Tour 1"]["Match 4"].renvoyer_regions_equipes()
        )
        == 4
    )


def test_msi_2024_bracket_simuler_tours(msi_2024_bracket_apres_tirage):
    bracket = msi_2024_bracket_apres_tirage
    bracket._simuler_tours()

    # Tour 2 - Matchs 1 et 2
    assert (
        bracket._tableau["Tour 2"]["Match 1"].equipe_1
        == bracket._tableau["Tour 1"]["Match 1"].renvoyer_equipe_gagnante()
    )
    assert (
        bracket._tableau["Tour 2"]["Match 1"].equipe_2
        == bracket._tableau["Tour 1"]["Match 2"].renvoyer_equipe_gagnante()
    )
    assert (
        bracket._tableau["Tour 2"]["Match 2"].equipe_1
        == bracket._tableau["Tour 1"]["Match 3"].renvoyer_equipe_gagnante()
    )
    assert (
        bracket._tableau["Tour 2"]["Match 2"].equipe_2
        == bracket._tableau["Tour 1"]["Match 4"].renvoyer_equipe_gagnante()
    )

    # Tour 1 - Matchs 5 et 6
    assert (
        bracket._tableau["Tour 1"]["Match 5"].equipe_1
        == bracket._tableau["Tour 1"]["Match 1"].renvoyer_equipe_perdante()
    )
    assert (
        bracket._tableau["Tour 1"]["Match 5"].equipe_2
        == bracket._tableau["Tour 1"]["Match 2"].renvoyer_equipe_perdante()
    )
    assert (
        bracket._tableau["Tour 1"]["Match 6"].equipe_1
        == bracket._tableau["Tour 1"]["Match 3"].renvoyer_equipe_perdante()
    )
    assert (
        bracket._tableau["Tour 1"]["Match 6"].equipe_2
        == bracket._tableau["Tour 1"]["Match 4"].renvoyer_equipe_perdante()
    )

    # Tour 2 - Matchs 3 et 4
    assert (
        bracket._tableau["Tour 2"]["Match 3"].equipe_1
        == bracket._tableau["Tour 2"]["Match 2"].renvoyer_equipe_perdante()
    )
    assert (
        bracket._tableau["Tour 2"]["Match 3"].equipe_2
        == bracket._tableau["Tour 1"]["Match 5"].renvoyer_equipe_gagnante()
    )
    assert (
        bracket._tableau["Tour 2"]["Match 4"].equipe_1
        == bracket._tableau["Tour 2"]["Match 1"].renvoyer_equipe_perdante()
    )
    assert (
        bracket._tableau["Tour 2"]["Match 4"].equipe_2
        == bracket._tableau["Tour 1"]["Match 6"].renvoyer_equipe_gagnante()
    )

    # Tour 4 - Match 1
    assert (
        bracket._tableau["Tour 4"]["Match 1"].equipe_1
        == bracket._tableau["Tour 2"]["Match 1"].renvoyer_equipe_gagnante()
    )
    assert (
        bracket._tableau["Tour 4"]["Match 1"].equipe_2
        == bracket._tableau["Tour 2"]["Match 2"].renvoyer_equipe_gagnante()
    )

    # Tour 3
    assert (
        bracket._tableau["Tour 3"]["Match 1"].equipe_1
        == bracket._tableau["Tour 2"]["Match 3"].renvoyer_equipe_gagnante()
    )
    assert (
        bracket._tableau["Tour 3"]["Match 1"].equipe_2
        == bracket._tableau["Tour 2"]["Match 4"].renvoyer_equipe_gagnante()
    )

    # Tour 4 - Match 2
    assert (
        bracket._tableau["Tour 4"]["Match 2"].equipe_1
        == bracket._tableau["Tour 4"]["Match 1"].renvoyer_equipe_perdante()
    )
    assert (
        bracket._tableau["Tour 4"]["Match 2"].equipe_2
        == bracket._tableau["Tour 3"]["Match 1"].renvoyer_equipe_gagnante()
    )

    # Tour 5
    assert (
        bracket._tableau["Tour 5"]["Match 1"].equipe_1
        == bracket._tableau["Tour 4"]["Match 1"].renvoyer_equipe_gagnante()
    )
    assert (
        bracket._tableau["Tour 5"]["Match 1"].equipe_2
        == bracket._tableau["Tour 4"]["Match 2"].renvoyer_equipe_gagnante()
    )


def test_msi_2024_bracket_renvoyer_classement(msi_2024_bracket_apres_tirage_et_resultats):
    resultat_renvoye = msi_2024_bracket_apres_tirage_et_resultats.renvoyer_classement()
    resultat_attendu = {
        "1": {pytest.gen},
        "2": {pytest.blg},
        "3": {pytest.t1},
        "4": {pytest.g2},
        "5-6": {pytest.tl, pytest.tes},
        "7-8": {pytest.fnc, pytest.psg},
    }
    assert resultat_renvoye == resultat_attendu


def test_msi_2024_playin_renvoyer_resultats_str(msi_2024_bracket_apres_tirage_et_resultats):
    resultat_renvoye = msi_2024_bracket_apres_tirage_et_resultats.renvoyer_resultats_str()

    resultat_attendu = "\n".join(
        [
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
            "| GEN | 3 |                                                                ",
            "|—————————|——                                                              ",
            "| FNC | 0 |  |   —————————                                                 ",
            " —————————    ——| GEN | 3 |                                                ",
            "                |—————————|                                                ",
            " —————————    ——| TES | 2 |——                                              ",
            "| TL  | 0 |  |   —————————   |                                             ",
            "|—————————|——                |                                             ",
            "| TES | 3 |                  |                   —————————                 ",
            " —————————                    ——————————————————| GEN | 3 |                ",
            "                                                |—————————|——              ",
            " —————————                    ——————————————————| BLG | 1 |  |             ",
            "| G2  | 2 |                  |                   —————————   |             ",
            "|—————————|——                |                               |             ",
            "| T1  | 3 |  |   —————————   |                               |             ",
            " —————————    ——| T1  | 1 |  |                               |             ",
            "                |—————————|——                                |   ————————— ",
            " —————————    ——| BLG | 3 |                                   ——| GEN | 3 |",
            "| BLG | 3 |  |   —————————                                      |—————————|",
            "|—————————|——                                                 ——| BLG | 1 |",
            "| PSG | 2 |                                                  |   ————————— ",
            " —————————                                                   |             ",
            "             |   —————————                                   |             ",
            " —————————    ——| T1  | 3 |                                  |             ",
            "| FNC | 1 |     |—————————|——                |   —————————   |             ",
            "|—————————|—————| TL  | 1 |  |   —————————    ——| BLG | 3 |  |             ",
            "| TL  | 3 |      —————————    ——| T1  | 3 |     |—————————|——              ",
            " —————————                      |—————————|—————| T1  | 2 |                ",
            "             |   —————————    ——| G2  | 0 |      —————————                 ",
            " —————————    ——| TES | 0 |  |   —————————                                 ",
            "| G2  | 3 |     |—————————|——                                              ",
            "|—————————|—————| G2  | 3 |                                                ",
            "| PSG | 0 |      —————————                                                 ",
            " —————————                                                                 ",
        ]
    )

    assert resultat_renvoye == resultat_attendu
