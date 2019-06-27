import pandas as pd

class DisciplineEquivalence:
    """
    Represent a discipline equivalence.
    """
    
    def __init__(self, original_discipline, equivalent_discipline):
        self.original_discipline = original_discipline
        self.equivalent_discipline = equivalent_discipline
        
    def serialize(self):
        """
        Serialize properties to a DataFrame
        """
        return pd.DataFrame(
            columns=[
                "COD_DISCIP_ORIG", "NOME_DISCIP_ORIG", "CARGAH_DISCIP_ORIG", "EMENTA_DISCIP_ORIG",
                "COD_DISCIP_EQUIV", "NOME_DISCIP_EQUIV", "CARGAH_DISCIP_EQUIV", "EMENTA_DISCIP_EQUIV"
            ],
            data = [[
                self.original_discipline.id, self.original_discipline.name, 
                self.original_discipline.workload, self.original_discipline.syllabus,                
                self.equivalent_discipline.id, self.equivalent_discipline.name, 
                self.equivalent_discipline.workload, self.equivalent_discipline.syllabus,
            ]],
        )
