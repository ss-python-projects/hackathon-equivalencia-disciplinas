import pandas as pd
from memory.database import Database

class Whitelist:
    """
    A class that manages the whitelisted disciplines.
    Whitelisted disciplines are disciplines that were already
    considered as equivalents.
    """

    def __init__(self):
        self.db = Database()

    def are_disciplines_related(self, discipline_a, discipline_b):
        """
        Check if 'discipline_b' was already set as equivalent
        to 'discipline_a'.
        """
        equivalences = self.get_related_disciplines(discipline_a)
        is_id_equal_to_discipline_b = equivalences["COD_DISCIP_EQUIV"] == discipline_b.id
        return equivalences[is_id_equal_to_discipline_b].shape[0] > 0

    def has_any_related_discipline(self, discipline):
        """
        Check if given discipline has any recorded equivalence.
        """
        equivalences = self.get_related_disciplines(discipline)
        return equivalences.shape[0] > 0

    def get_related_disciplines(self, discipline):
        """
        Get all disciplines equivalent to the given discipline.
        """
        return self.db.get_documents("whitelist", discipline.id)

    def add_discipline(self, discipline_equivalence):
        """
        Add a discipline equivalence to the whitelist.
        """
        self.db.add_document("whitelist", discipline_equivalence.serialize())
