from brain.syllabus import Syllabus as SyllabusBrain
from model.discipline import Discipline as DisciplineModel
from strategy.cosine_similarity import CosineSimilarity as CosineSimilarityStrategy

class TestSyllabus:
    def test_calculate_similarity_equal_syllabus(self):
        discipline_a = DisciplineModel("2458", "Discipline A", "80", "Programming Introduction")
        discipline_b = DisciplineModel("2411", "Discipline B", "80", "Programming Introduction")
        actual = SyllabusBrain(CosineSimilarityStrategy(), discipline_a, discipline_b).compare()
        expected = 1
        assert actual == expected, "Similarity should be 1 for completely equal syllabus"

    def test_calculate_similarity_slightly_different_syllabus(self):
        discipline_a = DisciplineModel("2458", "Discipline A", "80", "Programming Introduction for Beginners")
        discipline_b = DisciplineModel("2411", "Discipline B", "80", "Programming Introduction")
        actual = SyllabusBrain(CosineSimilarityStrategy(), discipline_a, discipline_b).compare()
        expected = 0.6546536707079772
        assert actual == expected, "Similarity should be ~= 0.65 for slightly different syllabus" # not a cool result - I'd expect at least 80% :(
