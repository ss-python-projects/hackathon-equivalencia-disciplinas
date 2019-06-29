class Syllabus:
    """
    Calculate the similarity between two disciplines 
    considering their syllabus.

    Syllabus accepts a comparison strategy.
    """
    
    def __init__(self, strategy, discipline_a, discipline_b):
        self.strategy = strategy
        self.discipline_a = discipline_a
        self.discipline_b = discipline_b

    def compare(self):
        """
        Compare two disciplines using the given strategy.
        """
        similarity = self.strategy.compare(self.discipline_a.syllabus, self.discipline_b.syllabus)
        return similarity