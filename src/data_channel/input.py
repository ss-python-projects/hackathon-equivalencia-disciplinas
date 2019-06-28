import pandas as pd
from constants import columns

def read_disciplines():
    """
    Reads both offered and not offered disciplines from an input.
    """
    disciplines = pd.read_csv("assets/disciplines.csv", sep=";")
    disciplines = disciplines[[
        "COD_DISCIPLINA",
        "NOM_DISCIPLINA",
        "VAL_CARGA_HORARIA",
        "DSC_EMENTA",
    ]]

    # Currently, using the same entry list. There should be separated lists
    # for both inputs.
    not_offered = disciplines[:1]
    offered = disciplines[5:15]

    return not_offered, offered
