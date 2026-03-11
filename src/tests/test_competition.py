"""Tests pour la classe Competition."""

import re

import pytest

from ..msi_2024_bracket import MSI2024Bracket
from ..msi_2024_playin import MSI2024PlayIn


@pytest.mark.parametrize(
    "competition, resultat_attendu",
    [
        (MSI2024PlayIn(), {"KR #2", "CN #2", "EMEA #2", "NA #2", "APAC #1", "VN #1", "LAT #1", "BR #1"}),
        (
            MSI2024Bracket(),
            {"KR #1", "CN #1", "EMEA #1", "NA #1", "Play-In #1", "Play-In #2", "Play-In #3", "Play-In #4"},
        ),
    ],
)
def test_competition_places(competition, resultat_attendu):
    competition.renvoyer_places() == resultat_attendu


@pytest.mark.parametrize(
    "competition, equipes",
    [
        (
            MSI2024PlayIn(),
            (pytest.t1, pytest.tes, pytest.fnc, pytest.fly, pytest.psg, pytest.gam, pytest.est, pytest.lll),
        ),
        (
            MSI2024PlayIn(),
            {
                pytest.t1: "KR #2",
                pytest.tes: "CN #2",
                pytest.fnc: "EMEA #2",
                pytest.fly: "NA #2",
                pytest.psg: "APAC #1",
                pytest.gam: "VN #1",
                pytest.est: "LAT #1",
                pytest.lll: "BR #1",
            },
        ),
        (
            MSI2024PlayIn(),
            {
                "KR #2": pytest.t1,
                "CN #2": pytest.tes,
                "EMEA #2": pytest.fnc,
                "NA #2": pytest.fly,
                "APAC #1": pytest.psg,
                "VN #1": pytest.gam,
                "LAT #1": pytest.est,
            },
        ),
        (
            MSI2024PlayIn(),
            {
                "KR #2": "T1",
                "CN #2": "TES",
                "EMEA #2": "FNC",
                "NA #2": "FLY",
                "APAC #1": "PSG",
                "VN #1": "GAM",
                "LAT #1": "EST",
                "BR #1": "LLL",
            },
        ),
        (
            MSI2024Bracket(),
            {
                "KR #1": pytest.gen,
                "CN #1": pytest.blg,
                "EMEA #1": pytest.g2,
                "NA #1": pytest.tl,
                "Play-In #1": pytest.t1,
                "Play-In #2": pytest.tes,
                "Play-In #3": pytest.fnc,
                "Play-In #4": "PSG",
            },
        ),
    ],
)
def test_competition_ajouter_equipes_echec(competition, equipes):
    with pytest.raises(ValueError, match=re.escape("Les données fournies en argument sont mal formatées.")):
        competition.ajouter_equipes(equipes)


@pytest.mark.parametrize(
    "competition, equipes, chapeaux_equipes",
    [
        (
            MSI2024PlayIn(),
            {
                "KR #2": pytest.t1,
                "CN #2": pytest.tes,
                "EMEA #2": pytest.fnc,
                "NA #2": pytest.fly,
                "APAC #1": pytest.psg,
                "VN #1": pytest.gam,
                "LAT #1": pytest.est,
                "BR #1": pytest.lll,
            },
            {
                "Chapeau 1": [pytest.t1, pytest.tes],
                "Chapeau 2": [pytest.fly, pytest.fnc],
                "Chapeau 3": [pytest.gam, pytest.psg],
                "Chapeau 4": [pytest.est, pytest.lll],
            },
        ),
        (
            MSI2024PlayIn(),
            {
                "KR #2": pytest.gen,
                "CN #2": pytest.blg,
                "EMEA #2": pytest.g2,
                "NA #2": pytest.tl,
                "APAC #1": pytest.psg,
                "VN #1": pytest.gam,
                "LAT #1": pytest.est,
                "BR #1": pytest.lll,
            },
            {
                "Chapeau 1": [pytest.blg, pytest.gen],
                "Chapeau 2": [pytest.g2, pytest.tl],
                "Chapeau 3": [pytest.gam, pytest.psg],
                "Chapeau 4": [pytest.est, pytest.lll],
            },
        ),
        (
            MSI2024Bracket(),
            {
                "KR #1": pytest.gen,
                "CN #1": pytest.blg,
                "EMEA #1": pytest.g2,
                "NA #1": pytest.tl,
                "Play-In #1": pytest.t1,
                "Play-In #2": pytest.tes,
                "Play-In #3": pytest.fnc,
                "Play-In #4": pytest.psg,
            },
            {
                "Chapeau 1": [pytest.blg, pytest.gen],
                "Chapeau 2": [pytest.g2, pytest.tl],
                "Chapeau 3": [pytest.t1, pytest.tes],
                "Chapeau 4": [pytest.fnc, pytest.psg],
            },
        ),
        (
            MSI2024Bracket(),
            {
                "KR #1": pytest.t1,
                "CN #1": pytest.tes,
                "EMEA #1": pytest.fnc,
                "NA #1": pytest.fly,
                "Play-In #1": pytest.gen,
                "Play-In #2": pytest.blg,
                "Play-In #3": pytest.g2,
                "Play-In #4": pytest.tl,
            },
            {
                "Chapeau 1": [pytest.t1, pytest.tes],
                "Chapeau 2": [pytest.fly, pytest.fnc],
                "Chapeau 3": [pytest.blg, pytest.gen],
                "Chapeau 4": [pytest.g2, pytest.tl],
            },
        ),
    ],
)
def test_competition_ajouter_equipes_success(competition, equipes, chapeaux_equipes):
    competition.ajouter_equipes(equipes)
    assert competition._equipes == equipes
    assert competition._chapeaux_equipes == chapeaux_equipes
