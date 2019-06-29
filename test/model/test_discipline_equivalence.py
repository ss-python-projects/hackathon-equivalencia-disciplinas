import pandas as pd
from model.discipline import Discipline
from model.discipline_equivalence import DisciplineEquivalence

class TestDisciplineEquivalence():
    def test_serialize(self):
        discipline = Discipline("2428", "Discipline A", "40", "Syllabus A")
        equivalence = Discipline("5050", "Discipline B", "35", "Syllabus B")
        discipline_equivalence = DisciplineEquivalence(discipline, equivalence)
        discipline_equivalence.uuid = "1234"
        actual = discipline_equivalence.serialize()
        expected = pd.DataFrame(
            columns=[
                "UUID",
                "COD_DISCIP_ORIG", "NOME_DISCIP_ORIG", "CARGAH_DISCIP_ORIG", "EMENTA_DISCIP_ORIG",
                "COD_DISCIP_EQUIV", "NOME_DISCIP_EQUIV", "CARGAH_DISCIP_EQUIV", "EMENTA_DISCIP_EQUIV",
                "TIPO_EQUIV",
            ],
            data = [[
                "1234",
                discipline.id, discipline.name, discipline.workload, discipline.syllabus,
                equivalence.id, equivalence.name, equivalence.workload, equivalence.syllabus,
                1,
            ]],
        )

        assert actual.equals(expected)
