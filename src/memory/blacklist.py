import pandas as pd
from memory.database import Database
from equivalence import discipline_equivalence as de

class Blacklist:
    """
    A class that manages the blacklisted disciplines.
    Blacklisted disciplines are disciplines that were already 
    considered as not equivalents.
    """

    def __init__(self):
        self.db = Database()

    def has_record(self, discipline_a, discipline_b):
        """
        Check if 'discipline_b' was already set as not equivalent 
        to 'discipline_a'.
        """
        records_for_a = self.get_records_for(discipline_a)
        is_id_equal_to_discipline_b = records_for_a["COD_DISCIP_EQUIV"] == discipline_b["COD_DISCIPLINA"]
        return records_for_a[is_id_equal_to_discipline_b].shape[0] > 0

    def get_records_for(self, discipline_a):
        """
        Get all disciplines not equivalent to 'discipline_a'.
        """
        return self.db.get_documents("blacklist", discipline_a["COD_DISCIPLINA"])

    def add_record(self, discipline_a, discipline_b):
        """
        Add 'discipline_b' as not equivalent to 'discipline_a'.
        """
        not_equivalence = de.DisciplineEquivalence(
            orig_discipline_id=discipline_a["COD_DISCIPLINA"],
            orig_discipline_name=discipline_a["NOM_DISCIPLINA"],
            orig_discipline_workload=discipline_a["VAL_CARGA_HORARIA"],
            orig_discipline_syllabus=discipline_a["DSC_EMENTA"],

            equiv_discipline_id=discipline_b["COD_DISCIPLINA"],
            equiv_discipline_name=discipline_b["NOM_DISCIPLINA"],
            equiv_discipline_workload=discipline_b["VAL_CARGA_HORARIA"],
            equiv_discipline_syllabus=discipline_b["DSC_EMENTA"],
        )

        self.db.add_document("blacklist", not_equivalence.serialize())
