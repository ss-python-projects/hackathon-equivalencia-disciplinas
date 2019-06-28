import pandas as pd

class DisciplineEquivalence:
    """
    Represent a discipline equivalence.
    """

    def __init__(self, original_discipline, equivalent_discipline):
        self.original_discipline = original_discipline
        self.equivalent_discipline = equivalent_discipline
        self.equivalence_type = DisciplineEquivalence.calculate_equivalence_type(original_discipline, equivalent_discipline)

    @staticmethod
    def calculate_equivalence_type(discipline_a, discipline_b):
        """
        Calculate the equivalence type based on the
        workload of both disciplines.
        """
        diff = (discipline_b.workload / discipline_a.workload)
        equivalence_type = 0

        if diff >= 0.75:
            equivalence_type = 1
        elif diff >= 0.6 and diff < 0.75:
            equivalence_type = 2

        return equivalence_type

    @staticmethod
    def are_equivalent_by_workload(discipline_a, discipline_b):
        """
        Check if both disciplines are really equivalent.
        Disciplines are really equivalent if they have an
        equivalence type higher than 0.
        """
        equivalence_type = DisciplineEquivalence.calculate_equivalence_type(discipline_a, discipline_b)
        return equivalence_type > 0

    def serialize(self):
        """
        Serialize properties to a DataFrame
        """
        return pd.DataFrame(
            columns=[
                "COD_DISCIP_ORIG", "NOME_DISCIP_ORIG", "CARGAH_DISCIP_ORIG", "EMENTA_DISCIP_ORIG",
                "COD_DISCIP_EQUIV", "NOME_DISCIP_EQUIV", "CARGAH_DISCIP_EQUIV", "EMENTA_DISCIP_EQUIV",
                "TIPO_EQUIV"
            ],
            data = [[
                self.original_discipline.id, self.original_discipline.name,
                self.original_discipline.workload, self.original_discipline.syllabus,
                self.equivalent_discipline.id, self.equivalent_discipline.name,
                self.equivalent_discipline.workload, self.equivalent_discipline.syllabus,
                self.equivalence_type
            ]],
        )
