"""Tests de la classe _Personne."""

import pytest

from src.personne import _Personne


def test_init_avec_pseudo_valide() -> None:
    """Tester la création d'une personne avec un pseudo valide."""
    personne = _Personne("Faker")

    assert personne.pseudo == "Faker"


def test_init_leve_type_error_si_pseudo_non_str() -> None:
    """Tester qu'une erreur est levée si le pseudo n'est pas une chaîne."""
    with pytest.raises(TypeError):
        _Personne(12)  # type: ignore[arg-type]


@pytest.mark.parametrize("pseudo", ["", "A", "a" * 17])
def test_init_leve_value_error_si_longueur_pseudo_invalide(
    pseudo: str,
) -> None:
    """Tester qu'une erreur est levée si la longueur du pseudo est invalide."""
    with pytest.raises(ValueError):
        _Personne(pseudo)


def test_property_pseudo_est_en_lecture_seule() -> None:
    """Tester que la propriété pseudo ne peut pas être modifiée."""
    personne = _Personne("Faker")

    with pytest.raises(AttributeError):
        personne.pseudo = "Chovy"  # type: ignore[misc]


def test_property_pseudo_ne_peut_pas_etre_supprimee() -> None:
    """Tester que la propriété pseudo ne peut pas être supprimée."""
    personne = _Personne("Faker")

    with pytest.raises(AttributeError):
        del personne.pseudo


def test_eq_renvoie_true_si_memes_pseudos() -> None:
    """Tester l'égalité de deux personnes ayant le même pseudo."""
    personne_1 = _Personne("Faker")
    personne_2 = _Personne("Faker")

    assert personne_1 == personne_2


def test_eq_renvoie_false_si_pseudos_differents() -> None:
    """Tester l'inégalité de deux personnes ayant des pseudos différents."""
    personne_1 = _Personne("Faker")
    personne_2 = _Personne("Chovy")

    assert personne_1 != personne_2


def test_eq_avec_objet_non_personne() -> None:
    """Tester l'égalité avec un objet qui n'est pas une personne."""
    personne = _Personne("Faker")

    assert personne.__eq__(42) is NotImplemented


def test_str() -> None:
    """Tester la représentation informelle d'une personne."""
    personne = _Personne("Faker")

    assert str(personne) == "Faker"


def test_repr() -> None:
    """Tester la représentation officielle d'une personne."""
    personne = _Personne("Faker")

    assert repr(personne) == "_Personne('Faker')"


def test_hash() -> None:
    """Tester le hachage d'une personne."""
    personne = _Personne("Faker")

    assert hash(personne) == hash(repr(personne))


def test_deux_personnes_egales_ont_le_meme_hash() -> None:
    """Tester que deux personnes égales ont le même hash."""
    personne_1 = _Personne("Faker")
    personne_2 = _Personne("Faker")

    assert hash(personne_1) == hash(personne_2)
