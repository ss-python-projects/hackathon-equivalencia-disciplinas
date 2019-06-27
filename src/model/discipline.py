import pandas as pd

class Discipline:
    """
    Represent a discipline.
    """

    def __init__(self, id, name, workload, syllabus):
        self.id = id
        self.name = name
        self.workload = workload
        self.syllabus = syllabus

    def serialize(self):
        """
        Serialize properties to a DataFrame
        """
        return pd.DataFrame(
            columns=["COD_DISCIP", "NOME_DISCIP", "CARGAH_DISCIP", "EMENTA_DISCIP"],
            data=[[self.id, self.name, self.workload, self.syllabus]]
        )
