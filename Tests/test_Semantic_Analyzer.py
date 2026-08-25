import unittest

from Brain.SemanticAnalyzer import SemanticAnalyzer


class TestSemanticAnalyzer(unittest.TestCase):

    def setUp(self):

        self.analyzer = SemanticAnalyzer()

    # =====================================
    # Assuntos
    # =====================================

    def test_game(self):

        result = self.analyzer.analyze(
            "qual é meu jogo favorito?"
        )

        self.assertEqual(
            result["subject"],
            "game"
        )

    def test_animal(self):

        result = self.analyzer.analyze(
            "qual é meu animal favorito?"
        )

        self.assertEqual(
            result["subject"],
            "animal"
        )

    def test_film(self):

        result = self.analyzer.analyze(
            "você lembra qual filme eu gosto?"
        )

        self.assertEqual(
            result["subject"],
            "film"
        )

    def test_city(self):

        result = self.analyzer.analyze(
            "onde eu moro?"
        )

        self.assertEqual(
            result["subject"],
            "city"
        )

    # =====================================
    # Perguntas
    # =====================================

    def test_question(self):

        result = self.analyzer.analyze(
            "qual é meu jogo?"
        )

        self.assertTrue(
            result["question"]
        )

    def test_not_question(self):

        result = self.analyzer.analyze(
            "eu gosto de jogos"
        )

        self.assertFalse(
            result["question"]
        )

    # =====================================
    # Memória
    # =====================================

    def test_memory_question(self):

        result = self.analyzer.analyze(
            "você lembra qual é meu jogo?"
        )

        self.assertTrue(
            result["memory_related"]
        )

    def test_not_memory(self):

        result = self.analyzer.analyze(
            "eu joguei um jogo ontem"
        )

        self.assertFalse(
            result["memory_related"]
        )

    # =====================================
    # Entrada vazia
    # =====================================

    def test_empty(self):

        result = self.analyzer.analyze("")

        self.assertIsNone(
            result["subject"]
        )

        self.assertFalse(
            result["question"]
        )

        self.assertFalse(
            result["memory_related"]
        )


if __name__ == "__main__":
    unittest.main()