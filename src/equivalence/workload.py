from constants import columns

"""
@todo: this module should be converted to a Class.
"""

def difference(discipline_a, discipline_b):
    """
    Calculate `discipline_b`'s workload percentage 
    based on `discipline_a`'s workload.
    """
    a = discipline_a[columns.DISCIPLINE_WORKLOAD]
    b = discipline_b[columns.DISCIPLINE_WORKLOAD]
    return (b / a)
