import pandas as pd
from memory import database as db
from equivalence import discipline_equivalence as de

class Blacklist:
    """
    A class that manages the blacklisted disciplines.
    Blacklisted disciplines are disciplines that were already 
    considered as not equivalents.
    """

    def has_record(self, discipline_a, discipline_b):
        """
        Check if 'discipline_b' was already set as not equivalent 
        to 'discipline_a'.
        """
        return False

    def get_records_for(self, discipline_a):
        """
        Get all disciplines not equivalent to 'discipline_a'.
        """
        return pd.DataFrame()

    def add_record(self, discipline_a, discipline_b):
        """
        Add 'discipline_b' as not equivalent to 'discipline_a'.
        """
        not_equivalence = de.DisciplineEquivalence(
            orig_discipline_name = discipline_a["NOM_DISCIPLINA"],
            orig_discipline_workload = discipline_a["VAL_CARGA_HORARIA"],
            orig_discipline_syllabus = discipline_a["DSC_EMENTA"],
            equiv_discipline_name = discipline_b["NOM_DISCIPLINA"],
            equiv_discipline_workload = discipline_b["VAL_CARGA_HORARIA"],
            equiv_discipline_syllabus = discipline_b["DSC_EMENTA"],
        )

        db.add_document("blacklist", not_equivalence.serialize())
