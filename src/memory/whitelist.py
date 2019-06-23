import pandas as pd
from constants import columns

"""
@todo: this module should be converted to a Class.
"""

def has_equivalences(discipline):
    """
    Check in the database if the given discipline already 
    has calculated equivalences.

    @todo: implement using documents (MongoDB).
    """
    return True

def get_equivalences(discipline):
    """
    Get all the equivalences of the discipline.
    
    @todo: implement using documents (MongoDB).
    """
    equivalences = pd.DataFrame(columns=[
        columns.DISCIPLINE_NAME,
        columns.DISCIPLINE_WORKLOAD,
        columns.EQUIVALENT_DISCIPLINE_NAME,
        columns.EQUIVALENT_DISCIPLINE_WORKLOAD,
        columns.EQUIVALENCE_TYPE,
    ])

    equivalences = equivalences.append({
        columns.DISCIPLINE_NAME: discipline[columns.DISCIPLINE_NAME],
        columns.DISCIPLINE_WORKLOAD: discipline[columns.DISCIPLINE_WORKLOAD],
        columns.EQUIVALENT_DISCIPLINE_NAME: "Disciplina Equivalente #1",
        columns.EQUIVALENT_DISCIPLINE_WORKLOAD: (discipline[columns.DISCIPLINE_WORKLOAD] - 15),
        columns.EQUIVALENCE_TYPE: "2",
    }, ignore_index=True)

    equivalences = equivalences.append({
        columns.DISCIPLINE_NAME: discipline[columns.DISCIPLINE_NAME],
        columns.DISCIPLINE_WORKLOAD: discipline[columns.DISCIPLINE_WORKLOAD],
        columns.EQUIVALENT_DISCIPLINE_NAME: "Disciplina Equivalente #2",
        columns.EQUIVALENT_DISCIPLINE_WORKLOAD: (discipline[columns.DISCIPLINE_WORKLOAD] - 0),
        columns.EQUIVALENCE_TYPE: "1",
    }, ignore_index=True)

    return equivalences

def add(discipline_a, discipline_b):
    """
    Add `discipline_b` as an equivalence of `discipline_a`.

    @todo: implement using documents (MongoDB).
    """
    return True
    