"""Fichier de configuration pour les tests."""

import datetime

import pytest

from ..coach import Coach
from ..equipe import Equipe
from ..joueur import Joueur
from ..match import Match
from ..msi_2024 import MSI2024
from ..msi_2024_bracket import MSI2024Bracket
from ..msi_2024_playin import MSI2024PlayIn


def pytest_configure():
    # Gen.G
    pytest.gen = Equipe(
        nom_officiel="Gen.G",
        nom_abreviation="GEN",
        region="KR",
        joueurs=(
            Joueur("Kiin"),
            Joueur("Canyon"),
            Joueur("Chovy"),
            Joueur("Peyz"),
            Joueur("Lehends"),
        ),
        coachs=(Coach("KIM"), Coach("Helper")),
    )

    # Bilibili Gaming
    pytest.blg = Equipe(
        nom_officiel="Bilibili Gaming",
        nom_abreviation="BLG",
        region="CN",
        joueurs=(
            Joueur("Bin"),
            Joueur("Xun"),
            Joueur("knight"),
            Joueur("Elk"),
            Joueur("ON"),
        ),
        coachs=(Coach("BigWei"), Coach("Xiasu")),
    )

    # G2 Esports
    pytest.g2 = Equipe(
        nom_officiel="G2 Esports",
        nom_abreviation="G2",
        region="EMEA",
        joueurs=(
            Joueur("BrokenBlade"),
            Joueur("Yike"),
            Joueur("Caps"),
            Joueur("HansSama"),
            Joueur("Mikyx"),
        ),
        coachs=(Coach("Dylan Falco"), Coach("Rodrigo")),
    )

    # Team Liquid
    pytest.tl = Equipe(
        nom_officiel="Team Liquid",
        nom_abreviation="TL",
        region="NA",
        joueurs=(
            Joueur("Impact"),
            Joueur("UmTi"),
            Joueur("APA"),
            Joueur("Yeon"),
            Joueur("CoreJJ"),
        ),
        coachs=(Coach("Spawn"), Coach("Reignover")),
    )

    # T1
    pytest.t1 = Equipe(
        nom_officiel="T1",
        nom_abreviation="T1",
        region="KR",
        joueurs=(
            Joueur("Zeus"),
            Joueur("Oner"),
            Joueur("Faker"),
            Joueur("Gumayusi"),
            Joueur("Keria"),
        ),
        coachs=(Coach("KkOma"), Coach("Tom")),
    )

    # Top Esports
    pytest.tes = Equipe(
        nom_officiel="Top Esports",
        nom_abreviation="TES",
        region="CN",
        joueurs=(
            Joueur("369"),
            Joueur("Tian"),
            Joueur("Creme"),
            Joueur("JackeyLove"),
            Joueur("Meiko"),
        ),
        coachs=(Coach("Despa1r"), Coach("River")),
    )

    # Fnatic
    pytest.fnc = Equipe(
        nom_officiel="Fnatic",
        nom_abreviation="FNC",
        region="EMEA",
        joueurs=(
            Joueur("Oscarinin"),
            Joueur("Razork"),
            Joueur("Humanoid"),
            Joueur("Noah"),
            Joueur("Jun"),
        ),
        coachs=(Coach("Nightshare"), Coach("Gaax")),
    )

    # FlyQuest
    pytest.fly = Equipe(
        nom_officiel="FlyQuest",
        nom_abreviation="FLY",
        region="NA",
        joueurs=(
            Joueur("Bwipo"),
            Joueur("Inspired"),
            Joueur("Jensen"),
            Joueur("Massu"),
            Joueur("Busio"),
        ),
        coachs=(Coach("Nukeduck"),),
    )

    # PSG Talon
    pytest.psg = Equipe(
        nom_officiel="PSG Talon",
        nom_abreviation="PSG",
        region="APAC",
        joueurs=(
            Joueur("Azhi"),
            Joueur("JunJia"),
            Joueur("Maple"),
            Joueur("Betty"),
            Joueur("Woody"),
        ),
        coachs=(Coach("CorGi"), Coach("Zero")),
    )

    # GAM Esports
    pytest.gam = Equipe(
        nom_officiel="GAM Esports",
        nom_abreviation="GAM",
        region="VN",
        joueurs=(
            Joueur("Kiaya"),
            Joueur("Levi"),
            Joueur("Emo"),
            Joueur("EasyLove"),
            Joueur("Elio"),
        ),
        coachs=(Coach("Archie"), Coach("Hype")),
    )

    # Estral Esports
    pytest.est = Equipe(
        nom_officiel="Estral Esports",
        nom_abreviation="EST",
        region="LAT",
        joueurs=(
            Joueur("Zothve"),
            Joueur("Josedeodo"),
            Joueur("Cody"),
            Joueur("Snaker"),
            Joueur("Ackerman"),
        ),
        coachs=(Coach("Snok"), Coach("PR1D3")),
    )

    # LOUD
    pytest.lll = Equipe(
        nom_officiel="LOUD",
        nom_abreviation="LLL",
        region="BR",
        joueurs=(
            Joueur("Robo"),
            Joueur("Croc"),
            Joueur("tinowns"),
            Joueur("Route"),
            Joueur("RedBert"),
        ),
        coachs=(Coach("Stardust"), Coach("SrVenancio")),
    )


@pytest.fixture
def equipe_kwargs():
    return {
        "nom_officiel": "Equipe",
        "nom_abreviation": "EQU",
        "region": "EMEA",
        "joueurs": (
            Joueur("TOP"),
            Joueur("JGL"),
            Joueur("MID"),
            Joueur("BOT"),
            Joueur("SUP"),
        ),
        "coachs": (Coach("Head Coach"), Coach("Assistant Coach")),
    }


@pytest.fixture
def match_sans_equipes():
    return Match(best_of=1)


@pytest.fixture
def match_avec_equipe_1():
    match = Match(best_of=3)
    match.ajouter_equipe_1(equipe_1=pytest.gen)
    return match


@pytest.fixture
def match_avec_equipe_2():
    match = Match(best_of=5)
    match.ajouter_equipe_2(equipe_2=pytest.blg)
    return match


@pytest.fixture(params=[5])
def match_avec_equipes(request):
    match = Match(best_of=request.param)
    match.ajouter_equipes(equipe_1=pytest.gen, equipe_2=pytest.blg)
    return match


@pytest.fixture
def msi_2024_playin_avant_tirage():
    equipes = {
        "KR #2": pytest.t1,
        "CN #2": pytest.tes,
        "EMEA #2": pytest.fnc,
        "NA #2": pytest.fly,
        "APAC #1": pytest.psg,
        "VN #1": pytest.gam,
        "LAT #1": pytest.est,
        "BR #1": pytest.lll,
    }
    playin = MSI2024PlayIn()
    playin.ajouter_equipes(equipes)
    return playin


@pytest.fixture
def msi_2024_playin_apres_tirage(msi_2024_playin_avant_tirage):
    # Initialisation de la phase finale
    playin = msi_2024_playin_avant_tirage

    # Ajout manuel du tirage
    playin._tableau["Groupe A"]["Tour 1"]["Match 1"].ajouter_equipes(equipe_1=pytest.t1, equipe_2=pytest.est)
    playin._tableau["Groupe A"]["Tour 1"]["Match 2"].ajouter_equipes(equipe_1=pytest.fly, equipe_2=pytest.psg)
    playin._tableau["Groupe B"]["Tour 1"]["Match 1"].ajouter_equipes(equipe_1=pytest.tes, equipe_2=pytest.lll)
    playin._tableau["Groupe B"]["Tour 1"]["Match 2"].ajouter_equipes(equipe_1=pytest.fnc, equipe_2=pytest.gam)

    return playin


@pytest.fixture
def msi_2024_playin_apres_tirage_et_resultats(msi_2024_playin_apres_tirage):
    # Initialisation de la phase finale
    playin = msi_2024_playin_apres_tirage

    # Ajout manuel des résultats du groupe A
    playin._tableau["Groupe A"]["Tour 1"]["Match 1"].ajouter_scores(score_equipe_1=2, score_equipe_2=0)
    playin._tableau["Groupe A"]["Tour 1"]["Match 2"].ajouter_scores(score_equipe_1=2, score_equipe_2=1)
    playin._tableau["Groupe A"]["Tour 2"]["Match 1"].ajouter_equipes_et_scores(
        equipe_1=pytest.t1, equipe_2=pytest.fly, score_equipe_1=2, score_equipe_2=0
    )
    playin._tableau["Groupe A"]["Tour 1"]["Match 3"].ajouter_equipes_et_scores(
        equipe_1=pytest.est, equipe_2=pytest.psg, score_equipe_1=0, score_equipe_2=2
    )
    playin._tableau["Groupe A"]["Tour 2"]["Match 2"].ajouter_equipes_et_scores(
        equipe_1=pytest.fly, equipe_2=pytest.psg, score_equipe_1=0, score_equipe_2=2
    )

    # Ajout manuel des résultats du groupe A
    playin._tableau["Groupe B"]["Tour 1"]["Match 1"].ajouter_scores(score_equipe_1=2, score_equipe_2=0)
    playin._tableau["Groupe B"]["Tour 1"]["Match 2"].ajouter_scores(score_equipe_1=2, score_equipe_2=0)
    playin._tableau["Groupe B"]["Tour 2"]["Match 1"].ajouter_equipes_et_scores(
        equipe_1=pytest.tes, equipe_2=pytest.fnc, score_equipe_1=2, score_equipe_2=1
    )
    playin._tableau["Groupe B"]["Tour 1"]["Match 3"].ajouter_equipes_et_scores(
        equipe_1=pytest.lll, equipe_2=pytest.gam, score_equipe_1=1, score_equipe_2=2
    )
    playin._tableau["Groupe B"]["Tour 2"]["Match 2"].ajouter_equipes_et_scores(
        equipe_1=pytest.fnc, equipe_2=pytest.gam, score_equipe_1=2, score_equipe_2=0
    )

    return playin


@pytest.fixture
def msi_2024_bracket_avant_tirage():
    equipes = {
        "KR #1": pytest.gen,
        "CN #1": pytest.blg,
        "EMEA #1": pytest.g2,
        "NA #1": pytest.tl,
        "Play-In #1": pytest.t1,
        "Play-In #2": pytest.tes,
        "Play-In #3": pytest.fnc,
        "Play-In #4": pytest.psg,
    }
    bracket = MSI2024Bracket()
    bracket.ajouter_equipes(equipes)
    return bracket


@pytest.fixture
def msi_2024_bracket_apres_tirage(msi_2024_bracket_avant_tirage):
    # Initialisation de la phase finale
    bracket = msi_2024_bracket_avant_tirage

    # Ajout manuel du tirage
    bracket._tableau["Tour 1"]["Match 1"].ajouter_equipes(equipe_1=pytest.gen, equipe_2=pytest.fnc)
    bracket._tableau["Tour 1"]["Match 2"].ajouter_equipes(equipe_1=pytest.tl, equipe_2=pytest.tes)
    bracket._tableau["Tour 1"]["Match 3"].ajouter_equipes(equipe_1=pytest.g2, equipe_2=pytest.t1)
    bracket._tableau["Tour 1"]["Match 4"].ajouter_equipes(equipe_1=pytest.blg, equipe_2=pytest.psg)

    return bracket


@pytest.fixture
def msi_2024_bracket_apres_tirage_et_resultats(msi_2024_bracket_apres_tirage):
    # Initialisation de la phase finale
    bracket = msi_2024_bracket_apres_tirage

    # Ajout manuel des résultats
    # Tour 1 - Matchs 1 à 4
    bracket._tableau["Tour 1"]["Match 1"].ajouter_scores(score_equipe_1=3, score_equipe_2=0)
    bracket._tableau["Tour 1"]["Match 2"].ajouter_scores(score_equipe_1=0, score_equipe_2=3)
    bracket._tableau["Tour 1"]["Match 3"].ajouter_scores(score_equipe_1=2, score_equipe_2=3)
    bracket._tableau["Tour 1"]["Match 4"].ajouter_scores(score_equipe_1=3, score_equipe_2=2)

    # Tour 2 - Matchs 1 et 2
    bracket._tableau["Tour 2"]["Match 1"].ajouter_equipes_et_scores(
        equipe_1=pytest.gen, equipe_2=pytest.tes, score_equipe_1=3, score_equipe_2=2
    )
    bracket._tableau["Tour 2"]["Match 2"].ajouter_equipes_et_scores(
        equipe_1=pytest.t1, equipe_2=pytest.blg, score_equipe_1=1, score_equipe_2=3
    )

    # Tour 1 - Matchs 5 et 6
    bracket._tableau["Tour 1"]["Match 5"].ajouter_equipes_et_scores(
        equipe_1=pytest.fnc, equipe_2=pytest.tl, score_equipe_1=1, score_equipe_2=3
    )
    bracket._tableau["Tour 1"]["Match 6"].ajouter_equipes_et_scores(
        equipe_1=pytest.g2, equipe_2=pytest.psg, score_equipe_1=3, score_equipe_2=0
    )

    # Tour 2 - Matchs 3 et 4
    bracket._tableau["Tour 2"]["Match 3"].ajouter_equipes_et_scores(
        equipe_1=pytest.t1, equipe_2=pytest.tl, score_equipe_1=3, score_equipe_2=1
    )
    bracket._tableau["Tour 2"]["Match 4"].ajouter_equipes_et_scores(
        equipe_1=pytest.tes, equipe_2=pytest.g2, score_equipe_1=0, score_equipe_2=3
    )

    # Tour 4 - Match 1
    bracket._tableau["Tour 4"]["Match 1"].ajouter_equipes_et_scores(
        equipe_1=pytest.gen, equipe_2=pytest.blg, score_equipe_1=3, score_equipe_2=1
    )

    # Tour 3 - Match 1
    bracket._tableau["Tour 3"]["Match 1"].ajouter_equipes_et_scores(
        equipe_1=pytest.t1, equipe_2=pytest.g2, score_equipe_1=3, score_equipe_2=0
    )

    # Tour 4 - Match 2
    bracket._tableau["Tour 4"]["Match 2"].ajouter_equipes_et_scores(
        equipe_1=pytest.blg, equipe_2=pytest.t1, score_equipe_1=3, score_equipe_2=2
    )

    # Tour 5 - Match 1
    bracket._tableau["Tour 5"]["Match 1"].ajouter_equipes_et_scores(
        equipe_1=pytest.gen, equipe_2=pytest.blg, score_equipe_1=3, score_equipe_2=1
    )

    return bracket


@pytest.fixture
def msi_2024_avant_tirages_et_resultats():
    equipes = {
        "KR #1": pytest.gen,
        "CN #1": pytest.blg,
        "EMEA #1": pytest.g2,
        "NA #1": pytest.tl,
        "KR #2": pytest.t1,
        "CN #2": pytest.tes,
        "EMEA #2": pytest.fnc,
        "NA #2": pytest.fly,
        "APAC #1": pytest.psg,
        "VN #1": pytest.gam,
        "LAT #1": pytest.est,
        "BR #1": pytest.lll,
    }
    cagnotte = {
        "1": 50_000,
        "2": 40_000,
        "3": 30_000,
        "4": 25_000,
        "5-6": 20_000,
        "7-8": 15_000,
        "9-10": 10_000,
        "11-12": 7_500,
    }
    msi_2024 = MSI2024(
        n_equipes=12,
        cagnotte=cagnotte,
        date_debut=datetime.date(2024, 5, 1),
        date_fin=datetime.date(2024, 5, 19),
    )
    msi_2024.ajouter_equipes(equipes)
    return msi_2024


@pytest.fixture
def msi_2024_apres_tirages_et_resultats(
    msi_2024_avant_tirages_et_resultats,
    msi_2024_playin_apres_tirage_et_resultats,
    msi_2024_bracket_apres_tirage_et_resultats,
):
    msi_2024 = msi_2024_avant_tirages_et_resultats
    msi_2024._phases["Play-In"] = msi_2024_playin_apres_tirage_et_resultats
    msi_2024._phases["Bracket"] = msi_2024_bracket_apres_tirage_et_resultats
    return msi_2024
