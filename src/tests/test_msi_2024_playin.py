"""Tests pour la classe MSI2024PlayIn."""

import random

import pytest


@pytest.mark.parametrize("_", range(100))
def test_msi_2024_playin_simuler_tirage(_, msi_2024_playin_avant_tirage):
    random.seed(None)
    playin = msi_2024_playin_avant_tirage
    playin._simuler_tirage()

    # Chapeau 1
    assert playin._tableau["Groupe A"]["Tour 1"]["Match 1"].equipe_1 in (pytest.t1, pytest.tes)
    assert playin._tableau["Groupe B"]["Tour 1"]["Match 1"].equipe_1 in (pytest.t1, pytest.tes)
    assert (
        playin._tableau["Groupe A"]["Tour 1"]["Match 1"].equipe_1
        != playin._tableau["Groupe B"]["Tour 1"]["Match 1"].equipe_1
    )

    # Chapeau 2
    assert playin._tableau["Groupe A"]["Tour 1"]["Match 2"].equipe_1 in (pytest.fnc, pytest.fly)
    assert playin._tableau["Groupe B"]["Tour 1"]["Match 2"].equipe_1 in (pytest.fnc, pytest.fly)
    assert (
        playin._tableau["Groupe A"]["Tour 1"]["Match 2"].equipe_1
        != playin._tableau["Groupe B"]["Tour 1"]["Match 2"].equipe_1
    )

    # Chapeau 3
    assert playin._tableau["Groupe A"]["Tour 1"]["Match 2"].equipe_2 in (pytest.psg, pytest.gam)
    assert playin._tableau["Groupe B"]["Tour 1"]["Match 2"].equipe_2 in (pytest.psg, pytest.gam)
    assert (
        playin._tableau["Groupe A"]["Tour 1"]["Match 2"].equipe_2
        != playin._tableau["Groupe B"]["Tour 1"]["Match 2"].equipe_2
    )

    # Chapeau 4
    assert playin._tableau["Groupe A"]["Tour 1"]["Match 1"].equipe_2 in (pytest.est, pytest.lll)
    assert playin._tableau["Groupe B"]["Tour 1"]["Match 1"].equipe_2 in (pytest.est, pytest.lll)
    assert (
        playin._tableau["Groupe A"]["Tour 1"]["Match 1"].equipe_2
        != playin._tableau["Groupe B"]["Tour 1"]["Match 1"].equipe_2
    )


def test_msi_2024_playin_simuler_tours(msi_2024_playin_apres_tirage):
    playin = msi_2024_playin_apres_tirage
    playin._simuler_tours()

    # Groupes A et B - Tour 2 - Matchs 1
    assert (
        playin._tableau["Groupe A"]["Tour 2"]["Match 1"].equipe_1
        == playin._tableau["Groupe A"]["Tour 1"]["Match 1"].renvoyer_equipe_gagnante()
    )
    assert (
        playin._tableau["Groupe A"]["Tour 2"]["Match 1"].equipe_2
        == playin._tableau["Groupe A"]["Tour 1"]["Match 2"].renvoyer_equipe_gagnante()
    )
    assert (
        playin._tableau["Groupe B"]["Tour 2"]["Match 1"].equipe_1
        == playin._tableau["Groupe B"]["Tour 1"]["Match 1"].renvoyer_equipe_gagnante()
    )
    assert (
        playin._tableau["Groupe B"]["Tour 2"]["Match 1"].equipe_2
        == playin._tableau["Groupe B"]["Tour 1"]["Match 2"].renvoyer_equipe_gagnante()
    )

    # Groupes A et B - Tour 1 - Matchs 3
    assert (
        playin._tableau["Groupe A"]["Tour 1"]["Match 3"].equipe_1
        == playin._tableau["Groupe A"]["Tour 1"]["Match 1"].renvoyer_equipe_perdante()
    )
    assert (
        playin._tableau["Groupe A"]["Tour 1"]["Match 3"].equipe_2
        == playin._tableau["Groupe A"]["Tour 1"]["Match 2"].renvoyer_equipe_perdante()
    )
    assert (
        playin._tableau["Groupe B"]["Tour 1"]["Match 3"].equipe_1
        == playin._tableau["Groupe B"]["Tour 1"]["Match 1"].renvoyer_equipe_perdante()
    )
    assert (
        playin._tableau["Groupe B"]["Tour 1"]["Match 3"].equipe_2
        == playin._tableau["Groupe B"]["Tour 1"]["Match 2"].renvoyer_equipe_perdante()
    )

    # Groupes A et B - Tour 2 - Matchs 2
    assert (
        playin._tableau["Groupe A"]["Tour 2"]["Match 2"].equipe_1
        == playin._tableau["Groupe A"]["Tour 2"]["Match 1"].renvoyer_equipe_perdante()
    )
    assert (
        playin._tableau["Groupe A"]["Tour 2"]["Match 2"].equipe_2
        == playin._tableau["Groupe A"]["Tour 1"]["Match 3"].renvoyer_equipe_gagnante()
    )
    assert (
        playin._tableau["Groupe B"]["Tour 2"]["Match 2"].equipe_1
        == playin._tableau["Groupe B"]["Tour 2"]["Match 1"].renvoyer_equipe_perdante()
    )
    assert (
        playin._tableau["Groupe B"]["Tour 2"]["Match 2"].equipe_2
        == playin._tableau["Groupe B"]["Tour 1"]["Match 3"].renvoyer_equipe_gagnante()
    )


def test_msi_2024_playin_renvoyer_classement(msi_2024_playin_apres_tirage_et_resultats):
    resultat_renvoye = msi_2024_playin_apres_tirage_et_resultats.renvoyer_classement()
    resultat_attendu = {
        "1-2": {pytest.t1, pytest.tes},
        "3-4": {pytest.psg, pytest.fnc},
        "5-6": {pytest.fly, pytest.gam},
        "7-8": {pytest.est, pytest.lll},
    }
    assert resultat_renvoye == resultat_attendu


def test_msi_2024_playin_renvoyer_resultats_str(msi_2024_playin_apres_tirage_et_resultats):
    resultat_renvoye = msi_2024_playin_apres_tirage_et_resultats.renvoyer_resultats_str()

    resultat_attendu = "\n".join(
        [
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
            "| T1  | 2 |                   | TES | 2 |                ",
            "|—————————|——                 |—————————|——              ",
            "| EST | 0 |  |   —————————    | LLL | 0 |  |   ————————— ",
            " —————————    ——| T1  | 2 |    —————————    ——| TES | 2 |",
            "                |—————————|                   |—————————|",
            " —————————    ——| FLY | 0 |    —————————    ——| FNC | 1 |",
            "| FLY | 2 |  |   —————————    | FNC | 2 |  |   ————————— ",
            "|—————————|——                 |—————————|——              ",
            "| PSG | 1 |                   | GAM | 0 |                ",
            " —————————                     —————————                 ",
            "             |   —————————                 |   ————————— ",
            " —————————    ——| FLY | 0 |    —————————    ——| FNC | 2 |",
            "| EST | 0 |     |—————————|   | LLL | 1 |     |—————————|",
            "|—————————|—————| PSG | 2 |   |—————————|—————| GAM | 0 |",
            "| PSG | 2 |      —————————    | GAM | 2 |      ————————— ",
            " —————————                     —————————                 ",
        ]
    )

    assert resultat_renvoye == resultat_attendu
