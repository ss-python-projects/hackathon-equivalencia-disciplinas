import pandas as pd
from model.discipline import Discipline

class TestDiscipline():
    def test_serialize(self):
        discipline = Discipline(
            "2428", "Trabalho Interdisciplinar",
            "40", "Proposição de soluções-problema"
        )

        actual = discipline.serialize()
        expected = pd.DataFrame(
            columns=["COD_DISCIP", "NOME_DISCIP", "CARGAH_DISCIP", "EMENTA_DISCIP"],
            data=[[discipline.id, discipline.name, discipline.workload, discipline.syllabus]]
        )

        assert actual.equals(expected)
