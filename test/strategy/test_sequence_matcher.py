from strategy.sequence_matcher import SequenceMatcher as SequenceMatcherStrategy

class TestSequenceMatcher:
    def test_compare_with_equal_sentences(self):
        strategy = SequenceMatcherStrategy()
        expected = 1
        actual = strategy.compare(
            "Aplicações executadas em dispositivos móveis",
            "Aplicações executadas em dispositivos móveis"
        )
        
        assert actual == expected

    def test_compare_with_slightly_different_sentences(self):
        strategy = SequenceMatcherStrategy()
        expected = 0.625
        actual = strategy.compare(
            "Aplicações executadas em dispositivos móveis",
            "Programação para dispositivos móveis"
        )
        
        assert actual == expected

    def test_compare_slightly_different_sentences_and_many_words(self):
        strategy = SequenceMatcherStrategy()
        expected = 0.26537216828478966
        actual = strategy.compare(
            "Aplicações executadas em dispositivos móveis, tipicamente telefones celulares, smartphones, PDAs (Personal Digital Assistant) e tablets",
            "Ambientes de desenvolvimento. Linguagens e bibliotecas. Motores para jogos. Programação de jogos 2D e 3D para dispositivos móveis. Construção de caso: 2D Platform / 2D Puzzle"
        )
        
        assert actual == expected