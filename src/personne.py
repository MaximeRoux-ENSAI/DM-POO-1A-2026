"""Implémentation de la classe _Personne."""


class _Personne:
    """Représenter une personne par son pseudonyme.

    Parameters
    ----------
    pseudo : str
        Le pseudo de la personne (entre 2 et 16 caractères inclus).
    """

    def __init__(self, pseudo: str) -> None:
        if not isinstance(pseudo, str):
            raise TypeError("Le pseudo doit être une chaîne de caractères.")
        if not 2 <= len(pseudo) <= 16:
            raise ValueError(
                "Le pseudo doit être une chaîne de caractères de longueur "
                "comprise entre 2 et 16 inclus."
            )
        self.__pseudo = pseudo

    @property
    def pseudo(self) -> str:
        """Renvoyer le pseudonyme de la personne.

        Returns
        -------
        str
            Le pseudonyme de la personne.
        """
        return self.__pseudo

    def __eq__(self, other: object) -> bool:
        if isinstance(other, _Personne):
            return self.pseudo == other.pseudo
        return NotImplemented

    def __str__(self) -> str:
        return self.pseudo

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.pseudo!r})"

    def __hash__(self) -> int:
        return hash(repr(self))
