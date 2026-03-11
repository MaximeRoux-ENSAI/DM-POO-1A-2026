"""Tests pour la classe Tournoi."""

import datetime
import re
from unittest.mock import patch

import pytest

from ..tournoi import Tournoi


@pytest.fixture
def kwargs_default():
    return {
        "n_equipes": 12,
        "cagnotte": {
            "1": 50_000,
            "2": 40_000,
            "3": 30_000,
            "4": 25_000,
            "5-6": 20_000,
            "7-8": 15_000,
            "9-10": 10_000,
            "11-12": 7_500,
        },
        "date_debut": datetime.date(2024, 5, 1),
        "date_fin": datetime.date(2024, 5, 19),
    }


@patch.multiple(Tournoi, __abstractmethods__=set())
@pytest.mark.parametrize(
    "kwargs, erreur, message_erreur",
    [
        ({"n_equipes": "12"}, ValueError, "Le nombre d'équipes doit être un entier supérieur ou égal à 2."),
        ({"n_equipes": 1}, ValueError, "Le nombre d'équipes doit être un entier supérieur ou égal à 2."),
        ({"cagnotte": 1}, TypeError, "La cagnotte doit être un dictionnaire."),
        (
            {"cagnotte": {("1",): 50_000}},
            TypeError,
            "Les clés du dictionnaire 'cagnotte' doivent être des chaînes de caractères.",
        ),
        ({"cagnotte": {"Un": 50_000}}, ValueError, "La chaîne de caractères 'Un' n'est pas une clé valide."),
        ({"cagnotte": {"1-1": 50_000}}, ValueError, "La chaîne de caractères '1-1' n'est pas une clé valide."),
        (
            {"n_equipes": 10},
            ValueError,
            "La répartition de la cagnotte n'est pas compatible avec le nombre d'équipes participantes.",
        ),
        (
            {"cagnotte": {"13": 5_000}},
            ValueError,
            "La répartition de la cagnotte n'est pas compatible avec le nombre d'équipes participantes.",
        ),
        (
            {"cagnotte": {"11-12": "5_000"}},
            ValueError,
            "Les valeurs du dictionnaire 'cagnotte' doivent être des entiers positifs ou nuls.",
        ),
        (
            {"cagnotte": {"11-12": -50}},
            ValueError,
            "Les valeurs du dictionnaire 'cagnotte' doivent être des entiers positifs ou nuls.",
        ),
        (
            {"cagnotte": {"11-12": 12_000}},
            ValueError,
            "La répartition de la cagnotte n'est pas valide : une équipe moins bien classée qu'une autre a une "
            "cagnotte strictement plus élevée.",
        ),
        ({"date_debut": "2024/05/01"}, TypeError, "La date de début doit bien être une date."),
        ({"date_fin": "2024/05/19"}, TypeError, "La date de fin doit bien être une date."),
        (
            {"date_debut": datetime.date(2024, 5, 20)},
            ValueError,
            "La date de fin doit être postérieure à la date de début.",
        ),
    ],
)
def test_tournoi_init_echec(kwargs, erreur, message_erreur, kwargs_default):
    if "cagnotte" in kwargs and isinstance(kwargs["cagnotte"], dict):
        kwargs_default["cagnotte"].update(kwargs["cagnotte"])
    else:
        kwargs_default.update(**kwargs)
    with pytest.raises(erreur, match=re.escape(message_erreur)):
        Tournoi(**kwargs_default)


@patch.multiple(Tournoi, __abstractmethods__=set())
@pytest.mark.parametrize(
    "kwargs, resultat_attendu",
    [
        (
            {},
            "Un total de 12 équipes participent à ce tournoi ayant lieu du 2024-05-01 au 2024-05-19 avec une "
            "cagnotte totale de 250000 dollars en jeu.",
        ),
        (
            {"date_debut": datetime.date(2025, 3, 6), "date_fin": datetime.date(2025, 3, 28)},
            "Un total de 12 équipes participent à ce tournoi ayant lieu du 2025-03-06 au 2025-03-28 avec une "
            "cagnotte totale de 250000 dollars en jeu.",
        ),
        (
            {"cagnotte": {"1": 100_000, "2": 50_000}},
            "Un total de 12 équipes participent à ce tournoi ayant lieu du 2024-05-01 au 2024-05-19 avec une "
            "cagnotte totale de 310000 dollars en jeu.",
        ),
    ],
)
def test_tournoi_str(kwargs, resultat_attendu, kwargs_default):
    if "cagnotte" in kwargs and isinstance(kwargs["cagnotte"], dict):
        kwargs_default["cagnotte"].update(**kwargs["cagnotte"])
    else:
        kwargs_default.update(**kwargs)
    tournoi = Tournoi(**kwargs_default)
    assert str(tournoi) == resultat_attendu


@patch.multiple(Tournoi, __abstractmethods__=set())
@pytest.mark.parametrize(
    "cagnotte, resultat_attendu",
    [
        ({}, 250_000),
        ({"1": 100_000}, 300_000),
        ({"2": 45_000}, 255_000),
        ({"5-6": 17_500}, 245_000),
        ({"11-12": 0}, 235_000),
    ],
)
def test_tournoi_calculer_cagnotte_totale(cagnotte, resultat_attendu, kwargs_default):
    kwargs_default["cagnotte"].update(**cagnotte)
    tournoi = Tournoi(**kwargs_default)
    assert tournoi.calculer_cagnotte_totale() == resultat_attendu
