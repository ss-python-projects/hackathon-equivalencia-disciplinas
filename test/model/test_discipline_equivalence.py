import pandas as pd
from model.discipline import Discipline
from model.discipline_equivalence import DisciplineEquivalence

class TestDisciplineEquivalence():
    def test_serialize(self):
        discipline = Discipline("2428", "Discipline A", "40", "Syllabus A")
        equivalence = Discipline("5050", "Discipline B", "35", "Syllabus B")
        discipline_equivalence = DisciplineEquivalence(discipline, equivalence)
        actual = discipline_equivalence.serialize()
        expected = pd.DataFrame(
            columns=[
                "COD_DISCIP_ORIG", "NOME_DISCIP_ORIG", "CARGAH_DISCIP_ORIG", "EMENTA_DISCIP_ORIG",
                "COD_DISCIP_EQUIV", "NOME_DISCIP_EQUIV", "CARGAH_DISCIP_EQUIV", "EMENTA_DISCIP_EQUIV"
            ],
            data = [[
                discipline.id, discipline.name, discipline.workload, discipline.syllabus,
                equivalence.id, equivalence.name, equivalence.workload, equivalence.syllabus,
            ]],
        )

        assert actual.equals(expected)
