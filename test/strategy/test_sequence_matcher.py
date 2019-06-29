from strategy.sequence_matcher import SequenceMatcher as SequenceMatcherStrategy

class TestSequenceMatcher:
    def test_compare_slightly_different_sentences_and_many_words(self):
        strategy = SequenceMatcherStrategy()
        expected = 0.26537216828478966
        actual = strategy.compare(
            "Aplicações executadas em dispositivos móveis, tipicamente telefones celulares, smartphones, PDAs (Personal Digital Assistant) e tablets",
            "Ambientes de desenvolvimento. Linguagens e bibliotecas. Motores para jogos. Programação de jogos 2D e 3D para dispositivos móveis. Construção de caso: 2D Platform / 2D Puzzle"
        )
        
        assert actual == expected

    def test_compare_real_equivalence_1(self):
        strategy = SequenceMatcherStrategy()
        expected = 0.013729977116704805
        actual = strategy.compare(
            "Desenvolvimento de algoritmos e estruturas de dados básicas. Desenvolvimento de programação em uma linguagem de alto nível. Metodologia de desenvolvimento de programas: refinamentos sucessivos, modularização e testes básicos",
            "Paradigmas de programação. Lógica de programação.Introdução ao conceito e uso de algoritmos. Estruturas condicionais e de seleção. Estrutura de repetição. Vetores e matrizes. Formas de representação dos algoritmos"
        )
        
        assert actual == expected

    def test_compare_real_equivalence_2(self):
        strategy = SequenceMatcherStrategy()
        expected = 0.012
        actual = strategy.compare(
            "Sistemas de Coordenadas Tridimensionais. Superfícies Cilíndricas e Quádricas. Coordenadas Cilíndricas e Esféricas. Funções Vetoriais. Funções de várias Variáveis. Derivadas Parciais. Plano Tangente. Regra da cadeia. Derivada Direcional e Vetor Gradie",
            "Funções Vetoriais. Funções de várias variáveis. Integrais múltiplas. Derivadas de funções vetoriais. Operadores diferenciais e aplicações. Equações diferenciais. Modelagem. Métodos para solução equações diferenciais ordinárias lineares e não lineares"
        )
        
        assert actual == expected