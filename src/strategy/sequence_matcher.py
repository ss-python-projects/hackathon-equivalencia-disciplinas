import difflib

class SequenceMatcher:
    """
    Compare sentences using the SequenceMatcher
    technique.
    """

    def compare(self, sentence_a, sentence_b):
        """
        Compare both sentences.
        """
        sequence = difflib.SequenceMatcher(None, sentence_a, sentence_b)
        similarity = sequence.ratio()
        return similarity