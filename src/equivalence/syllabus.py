from constants import columns

"""
@todo: this module should be converted to a Class.
"""

def similarity(discipline_a, discipline_b):
    """
    Calculate the percentage of similarity between the
    syllabus of both courses.

    @todo: implement this algorithm using some Machine
    Learning technique.
    """
    a = discipline_a[columns.DISCIPLINE_SYLLABUS]
    b = discipline_b[columns.DISCIPLINE_SYLLABUS]
    words_a = a.split()
    words_b = b.split()
    # return (len(words_b) / len(words_a))
    return True

