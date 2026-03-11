"""Tests de la classe Equipe."""

import pytest

from src.coach import Coach
from src.equipe import Equipe
from src.joueur import Joueur


@pytest.fixture
def joueurs_valides() -> tuple[Joueur, ...]:
    """Créer un t-uplet valide de joueurs."""
    return (
        Joueur("Faker"),
        Joueur("Oner"),
        Joueur("Gumayusi"),
        Joueur("Keria"),
        Joueur("Zeus"),
    )


@pytest.fixture
def coachs_valides() -> tuple[Coach, ...]:
    """Créer un t-uplet valide de coachs."""
    return (Coach("kkOma"),)


@pytest.fixture
def equipe_valide(
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> Equipe:
    """Créer une équipe valide."""
    return Equipe("T1 Esports", "T1", "KR", joueurs_valides, coachs_valides)


def test_init_avec_arguments_valides(
    equipe_valide: Equipe,
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester la création d'une équipe avec des arguments valides."""
    assert equipe_valide.nom_officiel == "T1 Esports"
    assert equipe_valide.nom_abreviation == "T1"
    assert equipe_valide.region == "KR"
    assert repr(equipe_valide) == (
        f"Equipe('T1 Esports', 'T1', 'KR', {joueurs_valides!r}, "
        f"{coachs_valides!r})"
    )


def test_init_leve_type_error_si_nom_officiel_non_str(
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une erreur est levée si le nom officiel n'est pas une chaîne."""
    with pytest.raises(TypeError):
        Equipe(12, "T1", "KR", joueurs_valides, coachs_valides)  # type: ignore[arg-type]


def test_init_leve_type_error_si_nom_abreviation_non_str(
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une erreur est levée si le nom abrégé n'est pas une chaîne."""
    with pytest.raises(TypeError):
        Equipe("T1 Esports", 12, "KR", joueurs_valides, coachs_valides)  # type: ignore[arg-type]


@pytest.mark.parametrize("nom_abreviation", ["T", "TEAM"])
def test_init_leve_value_error_si_longueur_nom_abreviation_invalide(
    nom_abreviation: str,
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une erreur est levée si la longueur du nom abrégé est invalide."""
    with pytest.raises(ValueError):
        Equipe(
            "T1 Esports",
            nom_abreviation,
            "KR",
            joueurs_valides,
            coachs_valides,
        )


def test_init_leve_value_error_si_nom_abreviation_non_alphanumerique(
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une erreur est levée si le nom abrégé n'est pas alphanumérique."""
    with pytest.raises(ValueError):
        Equipe("T1 Esports", "T!", "KR", joueurs_valides, coachs_valides)


def test_init_leve_value_error_si_nom_abreviation_non_majuscule(
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une erreur est levée si le nom abrégé n'est pas en majuscules."""
    with pytest.raises(ValueError):
        Equipe("T1 Esports", "Tk", "KR", joueurs_valides, coachs_valides)


def test_init_leve_type_error_si_region_non_str(
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une erreur est levée si la région n'est pas une chaîne."""
    with pytest.raises(TypeError):
        Equipe("T1 Esports", "T1", 12, joueurs_valides, coachs_valides)  # type: ignore[arg-type]


def test_init_leve_value_error_si_region_invalide(
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une erreur est levée si la région n'est pas valide."""
    with pytest.raises(ValueError):
        Equipe("T1 Esports", "T1", "EU", joueurs_valides, coachs_valides)


def test_init_leve_type_error_si_joueurs_non_tuple(
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une erreur est levée si joueurs n'est pas un t-uplet."""
    with pytest.raises(TypeError):
        Equipe(
            "T1 Esports",
            "T1",
            "KR",
            [Joueur("Faker")] * 5,  # type: ignore[arg-type]
            coachs_valides,
        )


def test_init_leve_value_error_si_nombre_joueurs_invalide(
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une erreur est levée si le nombre de joueurs est invalide."""
    joueurs = (
        Joueur("Faker"),
        Joueur("Oner"),
        Joueur("Keria"),
        Joueur("Zeus"),
    )

    with pytest.raises(ValueError):
        Equipe("T1 Esports", "T1", "KR", joueurs, coachs_valides)


def test_init_leve_value_error_si_joueurs_non_uniques(
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une erreur est levée si les joueurs ne sont pas uniques."""
    joueur = Joueur("Faker")
    joueurs = (joueur, joueur, joueur, joueur, joueur)

    with pytest.raises(ValueError):
        Equipe("T1 Esports", "T1", "KR", joueurs, coachs_valides)


def test_init_leve_type_error_si_elements_joueurs_non_joueur(
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une erreur est levée si un élément de joueurs n'est pas un Joueur."""
    joueurs = (
        Joueur("Faker"),
        Joueur("Oner"),
        Joueur("Keria"),
        Joueur("Zeus"),
        Coach("kkOma"),  # type: ignore[arg-type]
    )

    with pytest.raises(TypeError):
        Equipe("T1 Esports", "T1", "KR", joueurs, coachs_valides)


def test_init_leve_type_error_si_coachs_non_tuple(
    joueurs_valides: tuple[Joueur, ...],
) -> None:
    """Tester qu'une erreur est levée si coachs n'est pas un t-uplet."""
    with pytest.raises(TypeError):
        Equipe(
            "T1 Esports",
            "T1",
            "KR",
            joueurs_valides,
            [Coach("kkOma")],  # type: ignore[arg-type]
        )


@pytest.mark.parametrize("coachs", [(), (Coach("kkOma"), Coach("Tom"), Coach("Kim"))])
def test_init_leve_value_error_si_nombre_coachs_invalide(
    coachs: tuple[Coach, ...],
    joueurs_valides: tuple[Joueur, ...],
) -> None:
    """Tester qu'une erreur est levée si le nombre de coachs est invalide."""
    with pytest.raises(ValueError):
        Equipe("T1 Esports", "T1", "KR", joueurs_valides, coachs)


def test_init_leve_value_error_si_coachs_non_uniques(
    joueurs_valides: tuple[Joueur, ...],
) -> None:
    """Tester qu'une erreur est levée si les coachs ne sont pas uniques."""
    coach = Coach("kkOma")
    coachs = (coach, coach)

    with pytest.raises(ValueError):
        Equipe("T1 Esports", "T1", "KR", joueurs_valides, coachs)


def test_init_leve_type_error_si_elements_coachs_non_coach(
    joueurs_valides: tuple[Joueur, ...],
) -> None:
    """Tester qu'une erreur est levée si un élément de coachs n'est pas un Coach."""
    coachs = (Coach("kkOma"), Joueur("Faker"))  # type: ignore[arg-type]

    with pytest.raises(TypeError):
        Equipe("T1 Esports", "T1", "KR", joueurs_valides, coachs)


def test_nom_officiel_est_en_lecture_seule(equipe_valide: Equipe) -> None:
    """Tester que la propriété nom_officiel ne peut pas être modifiée."""
    with pytest.raises(AttributeError):
        equipe_valide.nom_officiel = "Gen.G"  # type: ignore[misc]


def test_nom_abreviation_est_en_lecture_seule(equipe_valide: Equipe) -> None:
    """Tester que la propriété nom_abreviation ne peut pas être modifiée."""
    with pytest.raises(AttributeError):
        equipe_valide.nom_abreviation = "GEN"  # type: ignore[misc]


def test_region_est_en_lecture_seule(equipe_valide: Equipe) -> None:
    """Tester que la propriété region ne peut pas être modifiée."""
    with pytest.raises(AttributeError):
        equipe_valide.region = "CN"  # type: ignore[misc]


def test_str(equipe_valide: Equipe) -> None:
    """Tester la représentation informelle d'une équipe."""
    assert str(equipe_valide) == "T1"


def test_repr(
    equipe_valide: Equipe,
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester la représentation officielle d'une équipe."""
    assert repr(equipe_valide) == (
        f"Equipe('T1 Esports', 'T1', 'KR', {joueurs_valides!r}, "
        f"{coachs_valides!r})"
    )


def test_eq_renvoie_true_si_meme_nom_officiel(
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester l'égalité de deux équipes ayant le même nom officiel."""
    equipe_1 = Equipe("T1 Esports", "T1", "KR", joueurs_valides, coachs_valides)
    equipe_2 = Equipe("T1 Esports", "SKT", "KR", joueurs_valides, coachs_valides)

    assert equipe_1 == equipe_2


def test_eq_renvoie_false_si_nom_officiel_different(
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester l'inégalité de deux équipes ayant un nom officiel différent."""
    equipe_1 = Equipe("T1 Esports", "T1", "KR", joueurs_valides, coachs_valides)
    equipe_2 = Equipe("Gen.G", "GEN", "KR", joueurs_valides, coachs_valides)

    assert equipe_1 != equipe_2


def test_eq_avec_objet_non_equipe(equipe_valide: Equipe) -> None:
    """Tester l'égalité avec un objet qui n'est pas une équipe."""
    assert equipe_valide.__eq__(42) is NotImplemented


def test_lt_renvoie_true_si_nom_officiel_strictement_inferieur(
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester l'ordre strict entre deux équipes."""
    equipe_1 = Equipe("Gen.G", "GEN", "KR", joueurs_valides, coachs_valides)
    equipe_2 = Equipe("T1 Esports", "T1", "KR", joueurs_valides, coachs_valides)

    assert equipe_1 < equipe_2


def test_lt_renvoie_false_si_nom_officiel_non_strictement_inferieur(
    joueurs_valides: tuple[Joueur, ...],
    coachs_valides: tuple[Coach, ...],
) -> None:
    """Tester qu'une équipe n'est pas strictement inférieure à elle-même."""
    equipe_1 = Equipe("T1 Esports", "T1", "KR", joueurs_valides, coachs_valides)
    equipe_2 = Equipe("T1 Esports", "SKT", "KR", joueurs_valides, coachs_valides)

    assert not equipe_1 < equipe_2


def test_lt_avec_objet_non_equipe(equipe_valide: Equipe) -> None:
    """Tester l'ordre avec un objet qui n'est pas une équipe."""
    assert equipe_valide.__lt__(42) is NotImplemented


def test_hash(equipe_valide: Equipe) -> None:
    """Tester le hachage d'une équipe."""
    assert hash(equipe_valide) == hash(repr(equipe_valide))
