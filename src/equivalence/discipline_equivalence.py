import pandas as pd

class DisciplineEquivalence:
    """
    Represent a discipline equivalence.
    """
    
    def __init__(
        self,
        orig_discipline_id, orig_discipline_name, orig_discipline_workload, orig_discipline_syllabus,
        equiv_discipline_id, equiv_discipline_name, equiv_discipline_workload, equiv_discipline_syllabus
    ):
        self.orig_discipline_id = orig_discipline_id
        self.orig_discipline_name = orig_discipline_name
        self.orig_discipline_workload = orig_discipline_workload
        self.orig_discipline_syllabus = orig_discipline_syllabus

        self.equiv_discipline_id = equiv_discipline_id,
        self.equiv_discipline_name = equiv_discipline_name
        self.equiv_discipline_workload = equiv_discipline_workload
        self.equiv_discipline_syllabus = equiv_discipline_syllabus

    def serialize(self):
        """
        Serialize values to a DataFrame row
        """
        return pd.DataFrame(
            columns=[
                "COD_DISCIP_ORIG", "NOME_DISCIP_ORIG", "CARGAH_DISCIP_ORIG", "EMENTA_DISCIP_ORIG",
                "COD_DISCIP_EQUIV", "NOME_DISCIP_EQUIV", "CARGAH_DISCIP_EQUIV", "EMENTA_DISCIP_EQUIV"
            ],
            data = [[
                self.orig_discipline_id, self.orig_discipline_name, self.orig_discipline_workload, self.orig_discipline_syllabus,
                self.equiv_discipline_id, self.equiv_discipline_name, self.equiv_discipline_workload, self.equiv_discipline_syllabus,
            ]],
        )
