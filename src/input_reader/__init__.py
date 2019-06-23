import pandas as pd
from constants import columns

def read_disciplines():
    """
    Reads both offered and not offered disciplines from an input.
    """
    disciplines = pd.read_csv("../assets/disciplines.csv", sep=";")
    disciplines = disciplines[[columns.DISCIPLINE_NAME, columns.DISCIPLINE_WORKLOAD]]

    # Currently, using the same entry list. There should be separated lists 
    # for both inputs.
    not_offered = disciplines[:5]
    offered = disciplines[5:40]

    return not_offered, offered
