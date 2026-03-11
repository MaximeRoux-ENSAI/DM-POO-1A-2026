"""Vérifications des informations fournies dans le diagramme de classes."""

import datetime
import inspect
from abc import ABC
from unittest.mock import patch

from ..coach import Coach
from ..competition import Competition
from ..equipe import Equipe
from ..joueur import Joueur
from ..match import Match
from ..msi_2024 import MSI2024
from ..msi_2024_bracket import MSI2024Bracket
from ..msi_2024_playin import MSI2024PlayIn
from ..personne import _Personne
from ..phase import Phase
from ..tournoi import Tournoi


def test_verifier_personne():
    # Signature de la méthode __init__()
    signature_init = inspect.signature(getattr(_Personne, "__init__"))
    assert tuple(signature_init.parameters.keys()) == (
        "self",
        "pseudo",
    ), "Les noms des arguments du constructeur de la classe _Personne ne sont pas corrects."
    assert all(
        value.default == inspect.Parameter.empty for value in signature_init.parameters.values()
    ), "Les valeurs par défaut des arguments du constructeur de la classe _Personne ne sont pas correctes."

    # Création de l'instance
    personne = _Personne("pseudo")

    # Attribut privé pseudo
    assert hasattr(personne, "_Personne__pseudo") and not callable(
        getattr(personne, "_Personne__pseudo")
    ), "La classe _Personne n'a pas l'attribut privé 'pseudo'."

    # Propriété pseudo
    assert isinstance(
        inspect.getattr_static(_Personne, "pseudo", None), property
    ), "La classe _Personne n'a pas la propriété 'pseudo'."

    # Méthodes redéfinies
    methodes_redefinies = ("__init__", "__str__", "__repr__", "__eq__", "__hash__")
    for methode in methodes_redefinies:
        assert hasattr(_Personne, methode) and getattr(_Personne, methode) is not getattr(
            object, methode
        ), f"La classe _Personne ne redéfinit pas la méthode {methode!r}."


def test_verifier_joueur():
    assert issubclass(Joueur, _Personne), "La classe Joueur n'hérite pas de la classe _Personne."


def test_verifier_coach():
    assert issubclass(Coach, _Personne), "La classe Coach n'hérite pas de la classe _Personne."


def test_verifier_equipe():
    # Signature de la méthode __init__()
    signature_init = inspect.signature(getattr(Equipe, "__init__"))
    assert tuple(signature_init.parameters.keys()) == (
        "self",
        "nom_officiel",
        "nom_abreviation",
        "region",
        "joueurs",
        "coachs",
    ), "Les noms des arguments du constructeur de la classe Equipe ne sont pas corrects."
    assert all(
        value.default == inspect.Parameter.empty for value in signature_init.parameters.values()
    ), "Les valeurs par défaut des arguments du constructeur de la classe Equipe ne sont pas correctes."

    # Création de l'instance
    equipe = Equipe(
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
    # Attributs privés
    attributs_prives = ("nom_officiel", "nom_abreviation", "region", "joueurs", "coachs")
    for attribut in attributs_prives:
        assert hasattr(equipe, f"_Equipe__{attribut}") and not callable(
            getattr(equipe, f"_Equipe__{attribut}", None)
        ), f"La classe Equipe n'a pas l'attribut privé {attribut!r}."

    # Propriétés
    proprietes = ("nom_officiel", "nom_abreviation", "region")
    for propriete in proprietes:
        assert isinstance(
            inspect.getattr_static(Equipe, propriete, None), property
        ), f"La classe Equipe n'a pas la propriété {propriete!r}."

    # Méthodes redéfinies
    methodes_redefinies = ("__init__", "__str__", "__repr__", "__eq__", "__lt__", "__hash__")
    for methode in methodes_redefinies:
        assert hasattr(Equipe, methode) and getattr(Equipe, methode) is not getattr(
            object, methode
        ), f"La classe Equipe ne redéfinit pas la méthode {methode!r}."


def test_verifier_match():
    # Signature de la méthode __init__()
    signature_init = inspect.signature(getattr(Match, "__init__"))
    assert tuple(signature_init.parameters.keys()) == (
        "self",
        "best_of",
    ), "Les noms des arguments du constructeur de la classe Match ne sont pas corrects."
    assert all(
        value.default == inspect.Parameter.empty for value in signature_init.parameters.values()
    ), "Les valeurs par défaut des arguments du constructeur de la classe Match ne sont pas correctes."

    # Création de l'instance
    match_ = Match(best_of=5)

    # Attributs privés
    attributs_prives = ("best_of", "equipe_1", "equipe_2", "score_equipe_1", "score_equipe_2")
    for attribut in attributs_prives:
        assert hasattr(match_, f"_Match__{attribut}") and not callable(
            getattr(match_, f"_Match__{attribut}")
        ), f"La classe Match n'a pas l'attribut privé {attribut!r}."

    # Propriétés
    proprietes = ("best_of", "equipe_1", "equipe_2", "score_equipe_1", "score_equipe_2")
    for propriete in proprietes:
        assert isinstance(
            inspect.getattr_static(Match, propriete, None), property
        ), f"La classe Match n'a pas la propriété {propriete!r}."

    # Méthodes redéfinies
    methodes_redefinies = ("__init__", "__str__")
    for methode in methodes_redefinies:
        assert hasattr(Match, methode) and getattr(Match, methode) is not getattr(
            object, methode
        ), f"La classe Match ne redéfinit pas la méthode {methode!r}."

    # Méthodes publiques
    methodes_publiques = (
        "ajouter_equipe_1",
        "ajouter_equipe_2",
        "ajouter_equipes",
        "ajouter_scores",
        "ajouter_equipes_et_scores",
        "renvoyer_equipe_gagnante",
        "renvoyer_equipe_perdante",
        "renvoyer_regions_equipes",
        "simuler",
    )
    for methode in methodes_publiques:
        assert hasattr(Match, methode) and callable(
            getattr(Match, methode)
        ), f"La classe Match n'a pas la méthode publique {methode!r}."

    # Signature de la méthode ajouter_equipe_1()
    signature_ajouter_equipe_1 = inspect.signature(getattr(Match, "ajouter_equipe_1"))
    assert tuple(signature_ajouter_equipe_1.parameters.keys()) == (
        "self",
        "equipe_1",
    ), "Les noms des arguments de la méthode 'ajouter_equipe_1()' de la classe Match ne sont pas corrects."
    assert all(value.default == inspect.Parameter.empty for value in signature_ajouter_equipe_1.parameters.values()), (
        "Les valeurs par défaut des arguments de la méthode 'ajouter_equipe_1()' de la classe Match ne sont pas "
        "correctes."
    )

    # Signature de la méthode ajouter_equipe_2()
    signature_ajouter_equipe_2 = inspect.signature(getattr(Match, "ajouter_equipe_2"))
    assert tuple(signature_ajouter_equipe_2.parameters.keys()) == (
        "self",
        "equipe_2",
    ), "Les noms des arguments de la méthode 'ajouter_equipe_2()' de la classe Match ne sont pas corrects."
    assert all(value.default == inspect.Parameter.empty for value in signature_ajouter_equipe_2.parameters.values()), (
        "Les valeurs par défaut des arguments de la méthode 'ajouter_equipe_2()' de la classe Match ne sont pas "
        "correctes."
    )

    # Signature de la méthode ajouter_equipes()
    signature_ajouter_equipes = inspect.signature(getattr(Match, "ajouter_equipes"))
    assert tuple(signature_ajouter_equipes.parameters.keys()) == (
        "self",
        "equipe_1",
        "equipe_2",
    ), "Les noms des arguments de la méthode 'ajouter_equipes()' de la classe Match ne sont pas corrects."
    assert all(value.default == inspect.Parameter.empty for value in signature_ajouter_equipes.parameters.values()), (
        "Les valeurs par défaut des arguments de la méthode 'ajouter_equipes()' de la classe Match ne sont pas "
        "correctes."
    )

    # Signature de la méthode ajouter_scores()
    signature_ajouter_scores = inspect.signature(getattr(Match, "ajouter_scores"))
    assert tuple(signature_ajouter_scores.parameters.keys()) == (
        "self",
        "score_equipe_1",
        "score_equipe_2",
    ), "Les noms des arguments de la méthode 'ajouter_scores()' de la classe Match ne sont pas corrects."
    assert all(value.default == inspect.Parameter.empty for value in signature_ajouter_scores.parameters.values()), (
        "Les valeurs par défaut des arguments de la méthode 'ajouter_scores()' de la classe Match ne sont pas "
        "correctes."
    )

    # Signature de la méthode ajouter_equipes_et_scores()
    signature_ajouter_equipes_et_scores = inspect.signature(getattr(Match, "ajouter_equipes_et_scores"))
    assert tuple(signature_ajouter_equipes_et_scores.parameters.keys()) == (
        "self",
        "equipe_1",
        "equipe_2",
        "score_equipe_1",
        "score_equipe_2",
    ), "Les noms des arguments de la méthode 'ajouter_equipes_et_scores()' de la classe Match ne sont pas corrects."
    assert all(
        value.default == inspect.Parameter.empty for value in signature_ajouter_equipes_et_scores.parameters.values()
    ), (
        "Les valeurs par défaut des arguments de la méthode 'ajouter_equipes_et_scores()' de la classe Match ne sont "
        "pas correctes."
    )


def test_verifier_competition():
    # Héritage
    assert issubclass(Competition, ABC), "La classe Competition n'est pas abstraite."

    # Signature de la méthode ajouter_equipes()
    signature_ajouter_equipes = inspect.signature(getattr(Competition, "ajouter_equipes"))
    assert tuple(signature_ajouter_equipes.parameters.keys()) == (
        "self",
        "equipes",
    ), "Les noms des arguments de la méthode 'ajouter_equipes()' de la classe Competition ne sont pas corrects."
    assert all(value.default == inspect.Parameter.empty for value in signature_ajouter_equipes.parameters.values()), (
        "Les valeurs par défaut des arguments de la méthode 'ajouter_equipes()' de la classe Competition ne sont pas "
        "correctes."
    )

    # Méthodes abstraites
    methodes_abstraites = ("_CHAPEAUX", "renvoyer_classement", "renvoyer_resultats_str", "simuler")
    assert Competition.__abstractmethods__ == frozenset(
        methodes_abstraites
    ), "L'ensemble des méthodes abstraites de la classe Competition n'est pas correct."

    # Méthodes publiques
    methodes_publiques = ("renvoyer_places", "ajouter_equipes", "afficher_resultats")
    for methode in methodes_publiques:
        assert hasattr(Competition, methode) and callable(
            getattr(Competition, methode)
        ), f"La classe Competition n'a pas la méthode publique {methode!r}."


def test_verifier_phase():
    # Héritage
    assert issubclass(Phase, ABC), "La classe Phase n'est pas abstraite."

    # Méthodes redéfinies
    assert hasattr(Phase, "__init__") and getattr(Phase, "__init__") is not getattr(
        object, "__init__"
    ), "La classe Phase ne redéfinit pas la méthode '__init__'."
    assert hasattr(Phase, "simuler") and getattr(Phase, "simuler") is not getattr(
        Competition, "simuler"
    ), "La classe Phase ne redéfinit pas la méthode 'simuler'."

    # Méthodes abstraites
    methodes_abstraites = (
        "_CHAPEAUX",
        "_TABLEAU_VIDE",
        "_simuler_tirage",
        "_simuler_tours",
        "renvoyer_classement",
        "renvoyer_resultats_str",
    )
    assert Phase.__abstractmethods__ == frozenset(
        methodes_abstraites
    ), "L'ensemble des méthodes abstraites de classe Phase n'est pas correct."


def test_verifier_msi2024playin():
    # Héritage
    assert issubclass(MSI2024PlayIn, Phase), "La classe MSI2024PlayIn n'hérite pas de la classe Phase."

    # Attributs de classe
    attributs_classe = ("CHAPEAUX", "TABLEAU_VIDE")
    for attribut in attributs_classe:
        assert hasattr(MSI2024PlayIn, f"_{attribut}") and not callable(
            getattr(MSI2024PlayIn, f"_{attribut}")
        ), f"La classe MSI2024PlayIn n'a pas l'attribut de classe protégé {attribut!r}."

    # Méthodes privées
    methodes_privees = (
        "simuler_tour_1_matchs_1_2",
        "simuler_tour_2_matchs_1",
        "simuler_tour_1_matchs_3",
        "simuler_tour_2_matchs_2",
    )
    for methode in methodes_privees:
        assert callable(
            getattr(MSI2024PlayIn, f"_MSI2024PlayIn__{methode}", None)
        ), f"La classe MSI2024PlayIn n'a pas la méthode privée {methode!r}."

    # Méthodes protégées
    methodes_protegees = ("simuler_tirage", "simuler_tours")
    for methode in methodes_protegees:
        assert callable(
            getattr(MSI2024PlayIn, f"_{methode}", None)
        ), f"La classe MSI2024PlayIn n'a pas la méthode protégée {methode!r}."

    # Méthodes publiques
    methodes_publiques = ("renvoyer_classement", "renvoyer_resultats_str")
    for methode in methodes_publiques:
        assert callable(
            getattr(MSI2024PlayIn, methode, None)
        ), f"La classe MSI2024PlayIn n'a pas la méthode publique {methode!r}."


def test_verifier_msi2024bracket():
    # Héritage
    assert issubclass(MSI2024Bracket, Phase), "La classe MSI2024Bracket n'hérite pas de la classe Phase."

    # Attributs de classe
    attributs_classe = ("CHAPEAUX", "TABLEAU_VIDE")
    for attribut in attributs_classe:
        assert hasattr(MSI2024Bracket, f"_{attribut}") and not callable(
            getattr(MSI2024Bracket, f"_{attribut}")
        ), f"La classe MSI2024Bracket n'a pas l'attribut de classe protégé {attribut!r}."

    # Méthodes privées
    methodes_privees = (
        "simuler_tour_1_matchs_1_a_4",
        "simuler_tour_2_matchs_1_2",
        "simuler_tour_1_matchs_5_6",
        "simuler_tour_2_matchs_3_4",
        "simuler_tour_4_match_1",
        "simuler_tour_3",
        "simuler_tour_4_match_2",
        "simuler_tour_5",
    )
    for methode in methodes_privees:
        assert callable(
            getattr(MSI2024Bracket, f"_MSI2024Bracket__{methode}", None)
        ), f"La classe MSI2024Bracket n'a pas la méthode privée {methode!r}."

    # Méthodes protégées
    methodes_protegees = ("simuler_tirage", "simuler_tours")
    for methode in methodes_protegees:
        assert callable(
            getattr(MSI2024Bracket, f"_{methode}", None)
        ), f"La classe MSI2024Bracket n'a pas la méthode protégée {methode!r}."

    # Méthodes publiques
    methodes_publiques = ("renvoyer_classement", "renvoyer_resultats_str")
    for methode in methodes_publiques:
        assert callable(
            getattr(MSI2024Bracket, f"{methode}", None)
        ), f"La classe MSI2024Bracket n'a pas la méthode publique {methode!r}."


def test_verifier_tournoi():
    # Héritage
    assert issubclass(Tournoi, Competition), "La classe Tournoi n'hérite pas de la classe Competition."
    assert issubclass(Tournoi, ABC), "La classe Tournoi n'est pas abstraite."

    # Signature de la méthode __init__()
    signature_init = inspect.signature(getattr(Tournoi, "__init__"))
    assert tuple(signature_init.parameters.keys()) == (
        "self",
        "n_equipes",
        "cagnotte",
        "date_debut",
        "date_fin",
    ), "Les noms des arguments du constructeur de la classe Tournoi ne sont pas corrects."
    assert all(
        value.default == inspect.Parameter.empty for value in signature_init.parameters.values()
    ), "Les valeurs par défaut des arguments du constructeur de la classe Tournoi ne sont pas correctes."

    @patch.multiple(Tournoi, __abstractmethods__=set())
    def verifier_tournoi_attributs():
        # Création d'instance
        tournoi = Tournoi(
            n_equipes=2,
            cagnotte={"1": 100, "2": 50},
            date_debut=datetime.date(2024, 5, 1),
            date_fin=datetime.date(2024, 5, 19),
        )

        # Attributs privés
        attributs_prives = ("n_equipes", "date_debut", "date_fin")
        for attribut in attributs_prives:
            assert hasattr(tournoi, f"_Tournoi__{attribut}") and not callable(
                getattr(tournoi, f"_Tournoi__{attribut}")
            ), f"La classe Tournoi n'a pas l'attribut privé {attribut!r}."

        # Attributs protégés
        attributs_proteges = ("cagnotte", "phases")
        for attribut in attributs_proteges:
            assert hasattr(tournoi, f"_{attribut}") and not callable(
                getattr(tournoi, f"_{attribut}")
            ), f"La classe Tournoi n'a pas l'attribut protégé {attribut!r}."

    # Attributs d'instance
    verifier_tournoi_attributs()

    # Méthodes redéfinies
    methodes_redefinies = ("__init__", "__str__")
    for methode in methodes_redefinies:
        assert hasattr(Tournoi, methode) and getattr(Tournoi, methode) is not getattr(
            object, methode
        ), f"La classe Tournoi ne redéfinit pas la méthode {methode!r}."

    # Méthode statique
    assert isinstance(
        inspect.getattr_static(Tournoi, "_Tournoi__verifier_nombre_str", None), staticmethod
    ), "La classe Tournoi n'a pas la méthode statique privée 'verifier_nombre_str'."

    # Méthodes privées
    methodes_privees = ("verifier_cles_cagnotte", "verifier_valeurs_cagnotte")
    for methode in methodes_privees:
        assert callable(
            getattr(Tournoi, f"_Tournoi__{methode}", None)
        ), f"La classe Tournoi n'a pas la méthode privée {methode!r}."

    # Méthode publique
    assert callable(
        getattr(Tournoi, "calculer_cagnotte_totale", None)
    ), "La classe Tournoi n'a pas la méthode publique 'calculer_cagnotte_totale'."


def test_verifier_msi2024():
    # Héritage
    assert issubclass(MSI2024, Tournoi), "La classe MSI2024 n'hérite pas de la classe Tournoi."

    # Attributs de classe
    attributs_classe = ("CHAPEAUX",)
    for attribut in attributs_classe:
        assert hasattr(MSI2024, f"_{attribut}") and not callable(
            getattr(MSI2024, f"_{attribut}", None)
        ), f"La classe MSI2024 n'a pas l'attribut de classe protégé {attribut!r}."

    # Méthodes de Competition redéfinies
    methodes_competition_redefinies = ("simuler", "renvoyer_classement", "renvoyer_resultats_str")
    for methode in methodes_competition_redefinies:
        assert (
            callable(getattr(MSI2024, f"{methode}", None)) and
            getattr(MSI2024, methode) is not getattr(Competition, methode)
        ), f"La classe MSI2024 ne redéfinit pas la méthode publique {methode!r}."

    # Méthodes de Tournoi redéfinies
    methodes_tournoi_redefinies = ("renvoyer_classement_str",)
    for methode in methodes_tournoi_redefinies:
        assert (
            callable(getattr(MSI2024, f"{methode}", None)) and
            getattr(MSI2024, methode, False) is not getattr(Tournoi, methode, True)
        ), f"La classe MSI2024 ne redéfinit pas la méthode publique {methode!r}."
