"""Tests de la classe Match."""

import pytest

from src.coach import Coach
from src.equipe import Equipe
from src.joueur import Joueur
from src.match import Match


@pytest.fixture
def joueurs_t1() -> tuple[Joueur, ...]:
    """Créer les joueurs de T1."""
    return (
        Joueur("Faker"),
        Joueur("Oner"),
        Joueur("Gumayusi"),
        Joueur("Keria"),
        Joueur("Zeus"),
    )


@pytest.fixture
def joueurs_gen() -> tuple[Joueur, ...]:
    """Créer les joueurs de Gen.G."""
    return (
        Joueur("Chovy"),
        Joueur("Canyon"),
        Joueur("Ruler"),
        Joueur("Lehends"),
        Joueur("Kiin"),
    )


@pytest.fixture
def coachs_t1() -> tuple[Coach, ...]:
    """Créer les coachs de T1."""
    return (Coach("kkOma"),)


@pytest.fixture
def coachs_gen() -> tuple[Coach, ...]:
    """Créer les coachs de Gen.G."""
    return (Coach("Score"),)


@pytest.fixture
def equipe_t1(
    joueurs_t1: tuple[Joueur, ...],
    coachs_t1: tuple[Coach, ...],
) -> Equipe:
    """Créer l'équipe T1."""
    return Equipe("T1 Esports", "T1", "KR", joueurs_t1, coachs_t1)


@pytest.fixture
def equipe_gen(
    joueurs_gen: tuple[Joueur, ...],
    coachs_gen: tuple[Coach, ...],
) -> Equipe:
    """Créer l'équipe Gen.G."""
    return Equipe("Gen.G", "GEN", "KR", joueurs_gen, coachs_gen)


@pytest.fixture
def match_bo3() -> Match:
    """Créer un match en BO3."""
    return Match(3)


def test_init_valide() -> None:
    """Tester la création valide d'un match."""
    match = Match(3)

    assert match.best_of == 3
    assert match.equipe_1 is None
    assert match.equipe_2 is None
    assert match.score_equipe_1 is None
    assert match.score_equipe_2 is None


def test_init_leve_type_error_si_best_of_non_entier() -> None:
    """Tester qu'une erreur est levée si best_of n'est pas un entier."""
    with pytest.raises(TypeError):
        Match("3")  # type: ignore[arg-type]


@pytest.mark.parametrize("best_of", [0, 2, 4, 7])
def test_init_leve_value_error_si_best_of_invalide(best_of: int) -> None:
    """Tester qu'une erreur est levée si best_of est invalide."""
    with pytest.raises(ValueError):
        Match(best_of)


def test_str_match_vide(match_bo3: Match) -> None:
    """Tester la représentation d'un match sans équipes ni scores."""
    assert str(match_bo3) == "-----------\n|     |  |\n|     |  |\n-----------"


def test_str_match_avec_equipes_sans_scores(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester la représentation d'un match avec équipes mais sans scores."""
    match_bo3.ajouter_equipes(equipe_t1, equipe_gen)

    assert str(match_bo3) == "-----------\n| T1  |  |\n| GEN |  |\n-----------"


def test_str_match_complet(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester la représentation d'un match avec équipes et scores."""
    match_bo3.ajouter_equipes_et_scores(equipe_t1, equipe_gen, 2, 1)

    assert str(match_bo3) == "-----------\n| T1  | 2 |\n| GEN | 1 |\n-----------"


def test_ajouter_equipe_1_valide(match_bo3: Match, equipe_t1: Equipe) -> None:
    """Tester l'ajout valide de l'équipe 1."""
    match_bo3.ajouter_equipe_1(equipe_t1)

    assert match_bo3.equipe_1 == equipe_t1


def test_ajouter_equipe_1_leve_value_error_si_deja_ajoutee(
    match_bo3: Match,
    equipe_t1: Equipe,
) -> None:
    """Tester qu'une erreur est levée si l'équipe 1 a déjà été ajoutée."""
    match_bo3.ajouter_equipe_1(equipe_t1)

    with pytest.raises(ValueError):
        match_bo3.ajouter_equipe_1(equipe_t1)


def test_ajouter_equipe_1_leve_type_error_si_argument_non_equipe(
    match_bo3: Match,
) -> None:
    """Tester qu'une erreur est levée si l'argument n'est pas une équipe."""
    with pytest.raises(TypeError):
        match_bo3.ajouter_equipe_1("T1")  # type: ignore[arg-type]


def test_ajouter_equipe_1_leve_value_error_si_meme_equipe_que_equipe_2(
    match_bo3: Match,
    equipe_t1: Equipe,
) -> None:
    """Tester qu'une erreur est levée si les deux équipes sont identiques."""
    match_bo3.ajouter_equipe_2(equipe_t1)

    with pytest.raises(ValueError):
        match_bo3.ajouter_equipe_1(equipe_t1)


def test_ajouter_equipe_2_valide(match_bo3: Match, equipe_gen: Equipe) -> None:
    """Tester l'ajout valide de l'équipe 2."""
    match_bo3.ajouter_equipe_2(equipe_gen)

    assert match_bo3.equipe_2 == equipe_gen


def test_ajouter_equipe_2_leve_value_error_si_deja_ajoutee(
    match_bo3: Match,
    equipe_gen: Equipe,
) -> None:
    """Tester qu'une erreur est levée si l'équipe 2 a déjà été ajoutée."""
    match_bo3.ajouter_equipe_2(equipe_gen)

    with pytest.raises(ValueError):
        match_bo3.ajouter_equipe_2(equipe_gen)


def test_ajouter_equipe_2_leve_type_error_si_argument_non_equipe(
    match_bo3: Match,
) -> None:
    """Tester qu'une erreur est levée si l'argument n'est pas une équipe."""
    with pytest.raises(TypeError):
        match_bo3.ajouter_equipe_2("GEN")  # type: ignore[arg-type]


def test_ajouter_equipe_2_leve_value_error_si_meme_equipe_que_equipe_1(
    match_bo3: Match,
    equipe_t1: Equipe,
) -> None:
    """Tester qu'une erreur est levée si les deux équipes sont identiques."""
    match_bo3.ajouter_equipe_1(equipe_t1)

    with pytest.raises(ValueError):
        match_bo3.ajouter_equipe_2(equipe_t1)


def test_ajouter_equipes_valide(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester l'ajout valide des deux équipes."""
    match_bo3.ajouter_equipes(equipe_t1, equipe_gen)

    assert match_bo3.equipe_1 == equipe_t1
    assert match_bo3.equipe_2 == equipe_gen


def test_scores_valides_renvoie_false_si_score_negatif(match_bo3: Match) -> None:
    """Tester _scores_valides avec un score négatif."""
    assert not match_bo3._scores_valides(-1, 2)


def test_scores_valides_renvoie_false_si_scores_egaux(match_bo3: Match) -> None:
    """Tester _scores_valides avec deux scores égaux."""
    assert not match_bo3._scores_valides(1, 1)


def test_scores_valides_renvoie_false_si_personne_natteint_le_bon_score(
    match_bo3: Match,
) -> None:
    """Tester _scores_valides si le score gagnant est incorrect."""
    assert not match_bo3._scores_valides(1, 0)


def test_scores_valides_renvoie_false_si_les_deux_equipes_ont_trop(
    match_bo3: Match,
) -> None:
    """Tester _scores_valides si les deux équipes ont un score trop grand."""
    assert not match_bo3._scores_valides(2, 2)


def test_scores_valides_renvoie_false_si_total_depasse_best_of(
    match_bo3: Match,
) -> None:
    """Tester _scores_valides si le total dépasse le best-of."""
    assert not match_bo3._scores_valides(2, 2)


@pytest.mark.parametrize("score_1, score_2", [(2, 0), (2, 1), (0, 2), (1, 2)])
def test_scores_valides_renvoie_true_si_scores_valides_bo3(
    match_bo3: Match,
    score_1: int,
    score_2: int,
) -> None:
    """Tester _scores_valides avec des scores valides en BO3."""
    assert match_bo3._scores_valides(score_1, score_2)


def test_ajouter_scores_leve_value_error_si_equipes_non_ajoutees(
    match_bo3: Match,
) -> None:
    """Tester qu'une erreur est levée si les équipes ne sont pas ajoutées."""
    with pytest.raises(ValueError):
        match_bo3.ajouter_scores(2, 1)


def test_ajouter_scores_leve_value_error_si_scores_deja_ajoutes(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester qu'une erreur est levée si les scores sont déjà ajoutés."""
    match_bo3.ajouter_equipes(equipe_t1, equipe_gen)
    match_bo3.ajouter_scores(2, 1)

    with pytest.raises(ValueError):
        match_bo3.ajouter_scores(2, 0)


def test_ajouter_scores_leve_type_error_si_score_non_entier(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester qu'une erreur est levée si un score n'est pas un entier."""
    match_bo3.ajouter_equipes(equipe_t1, equipe_gen)

    with pytest.raises(TypeError):
        match_bo3.ajouter_scores("2", 1)  # type: ignore[arg-type]


def test_ajouter_scores_leve_value_error_si_score_negatif(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester qu'une erreur est levée si un score est négatif."""
    match_bo3.ajouter_equipes(equipe_t1, equipe_gen)

    with pytest.raises(ValueError):
        match_bo3.ajouter_scores(-1, 2)


def test_ajouter_scores_leve_value_error_si_scores_invalides(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester qu'une erreur est levée si les scores sont incompatibles."""
    match_bo3.ajouter_equipes(equipe_t1, equipe_gen)

    with pytest.raises(ValueError):
        match_bo3.ajouter_scores(1, 0)


def test_ajouter_scores_valide(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester l'ajout valide des scores."""
    match_bo3.ajouter_equipes(equipe_t1, equipe_gen)
    match_bo3.ajouter_scores(2, 1)

    assert match_bo3.score_equipe_1 == 2
    assert match_bo3.score_equipe_2 == 1


def test_ajouter_equipes_et_scores_valide(
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester l'ajout des équipes et des scores en une fois."""
    match = Match(1)

    match.ajouter_equipes_et_scores(equipe_t1, equipe_gen, 1, 0)

    assert match.equipe_1 == equipe_t1
    assert match.equipe_2 == equipe_gen
    assert match.score_equipe_1 == 1
    assert match.score_equipe_2 == 0


def test_renvoyer_equipe_gagnante_leve_value_error_si_scores_absents(
    match_bo3: Match,
) -> None:
    """Tester qu'une erreur est levée si les scores sont absents."""
    with pytest.raises(ValueError):
        match_bo3.renvoyer_equipe_gagnante()


def test_renvoyer_equipe_gagnante_equipe_1(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester que l'équipe 1 est renvoyée gagnante."""
    match_bo3.ajouter_equipes_et_scores(equipe_t1, equipe_gen, 2, 1)

    assert match_bo3.renvoyer_equipe_gagnante() == equipe_t1


def test_renvoyer_equipe_gagnante_equipe_2(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester que l'équipe 2 est renvoyée gagnante."""
    match_bo3.ajouter_equipes_et_scores(equipe_t1, equipe_gen, 0, 2)

    assert match_bo3.renvoyer_equipe_gagnante() == equipe_gen


def test_renvoyer_equipe_perdante_leve_value_error_si_scores_absents(
    match_bo3: Match,
) -> None:
    """Tester qu'une erreur est levée si les scores sont absents."""
    with pytest.raises(ValueError):
        match_bo3.renvoyer_equipe_perdante()


def test_renvoyer_equipe_perdante_equipe_1(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester que l'équipe 1 est renvoyée perdante."""
    match_bo3.ajouter_equipes_et_scores(equipe_t1, equipe_gen, 0, 2)

    assert match_bo3.renvoyer_equipe_perdante() == equipe_t1


def test_renvoyer_equipe_perdante_equipe_2(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester que l'équipe 2 est renvoyée perdante."""
    match_bo3.ajouter_equipes_et_scores(equipe_t1, equipe_gen, 2, 0)

    assert match_bo3.renvoyer_equipe_perdante() == equipe_gen


def test_renvoyer_regions_equipes_vide(match_bo3: Match) -> None:
    """Tester le renvoi des régions si aucune équipe n'est ajoutée."""
    assert match_bo3.renvoyer_regions_equipes() == set()


def test_renvoyer_regions_equipes_une_seule_equipe(
    match_bo3: Match,
    equipe_t1: Equipe,
) -> None:
    """Tester le renvoi des régions avec une seule équipe."""
    match_bo3.ajouter_equipe_1(equipe_t1)

    assert match_bo3.renvoyer_regions_equipes() == {"KR"}


def test_renvoyer_regions_equipes_deux_equipes_meme_region(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester le renvoi des régions avec deux équipes de même région."""
    match_bo3.ajouter_equipes(equipe_t1, equipe_gen)

    assert match_bo3.renvoyer_regions_equipes() == {"KR"}


def test_simuler_leve_value_error_si_equipes_absentes(match_bo3: Match) -> None:
    """Tester qu'une erreur est levée si les équipes sont absentes."""
    with pytest.raises(ValueError):
        match_bo3.simuler()


def test_simuler_leve_value_error_si_scores_deja_ajoutes(
    match_bo3: Match,
    equipe_t1: Equipe,
    equipe_gen: Equipe,
) -> None:
    """Tester qu'une erreur est levée si les scores sont déjà ajoutés."""
    match_bo3.ajouter_equipes_et_scores(equipe_t1, equipe_gen, 2, 1)

    with pytest.raises(ValueError):
        match_bo3.simuler()


def test_simuler_equipe_1_gagne(
    equipe_t1: Equipe,
    equipe_gen: Equipe,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Tester une simulation où l'équipe 1 gagne."""
    match = Match(3)
    match.ajouter_equipes(equipe_t1, equipe_gen)

    valeurs = iter([0.1, 0.2])
    monkeypatch.setattr("src.match.random.random", lambda: next(valeurs))

    match.simuler()

    assert match.score_equipe_1 == 2
    assert match.score_equipe_2 == 0


def test_simuler_equipe_2_gagne(
    equipe_t1: Equipe,
    equipe_gen: Equipe,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Tester une simulation où l'équipe 2 gagne."""
    match = Match(3)
    match.ajouter_equipes(equipe_t1, equipe_gen)

    valeurs = iter([0.9, 0.8])
    monkeypatch.setattr("src.match.random.random", lambda: next(valeurs))

    match.simuler()

    assert match.score_equipe_1 == 0
    assert match.score_equipe_2 == 2
