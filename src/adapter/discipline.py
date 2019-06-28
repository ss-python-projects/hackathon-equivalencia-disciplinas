from model.discipline import Discipline as DisciplineModel

class Discipline:

    @staticmethod
    def adapt(discipline_df):
        """
        Adapt a DataFrame to an instance of model.Discipline.
        """
        return DisciplineModel(
            id=discipline_df["COD_DISCIPLINA"],
            name=discipline_df["NOM_DISCIPLINA"],
            workload=discipline_df["VAL_CARGA_HORARIA"],
            syllabus=discipline_df["DSC_EMENTA"],
        )
