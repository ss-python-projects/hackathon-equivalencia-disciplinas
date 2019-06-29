import pandas as pd
from memory.database import Database

class Blacklist:
    """
    A class that manages the blacklisted disciplines.
    Blacklisted disciplines are disciplines that were already
    considered as not equivalents.
    """

    def __init__(self):
        self.db = Database()

    def are_disciplines_related(self, discipline_a, discipline_b):
        """
        Check if 'discipline_b' was already set as not equivalent
        to 'discipline_a'.
        """
        non_equivalences = self.get_related_disciplines(discipline_a)
        is_id_equal_to_discipline_b = non_equivalences["COD_DISCIP_EQUIV"] == discipline_b.id
        return non_equivalences[is_id_equal_to_discipline_b].shape[0] > 0

    def get_related_disciplines(self, discipline):
        """
        Get all disciplines not equivalent to the given discipline.
        """
        related_disciplines = self.db.get_documents("blacklist", discipline.id)
        return related_disciplines

    def add_discipline(self, discipline_equivalence):
        """
        Add a non-equivalence discipline to the blacklist.
        """
        self.db.add_document("blacklist", discipline_equivalence.serialize())
