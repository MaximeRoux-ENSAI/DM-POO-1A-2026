"""Fichier principal à exécuter pour simuler un tournoi complet."""

if __name__ == "__main__":
    import datetime

    from src.coach import Coach
    from src.equipe import Equipe
    from src.joueur import Joueur
    from src.msi_2024 import MSI2024

    equipes_msi_2024 = {
        "KR #1": Equipe(
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
        ),
        "CN #1": Equipe(
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
        ),
        "EMEA #1": Equipe(
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
        ),
        "NA #1": Equipe(
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
        ),
        "KR #2": Equipe(
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
        ),
        "CN #2": Equipe(
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
        ),
        "EMEA #2": Equipe(
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
        ),
        "NA #2": Equipe(
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
        ),
        "APAC #1": Equipe(
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
        ),
        "VN #1": Equipe(
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
        ),
        "LAT #1": Equipe(
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
        ),
        "BR #1": Equipe(
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
        ),
    }

    cagnotte_msi_2024 = {
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
        cagnotte=cagnotte_msi_2024,
        date_debut=datetime.date(2024, 5, 1),
        date_fin=datetime.date(2024, 5, 19),
    )
    msi_2024.ajouter_equipes(equipes_msi_2024)
    msi_2024.simuler()
    msi_2024.afficher_resultats()
