import unittest

from Brain.MessageAnalyzer import MessageAnalyzer
from Brain.IntentTypes import IntentTypes


class TestMessageAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = MessageAnalyzer()

    # =====================================
    # Memória
    # =====================================

    def test_ask_user_name(self):
        result = self.analyzer.analyze(
            "Qual é meu nome?"
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.ASK_USER_NAME
        )

        self.assertEqual(
            result["subject"],
            "name"
        )

    def test_ask_user_city(self):
        result = self.analyzer.analyze(
            "Onde eu moro?"
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.ASK_USER_CITY
        )

        self.assertEqual(
            result["subject"],
            "city"
        )

    def test_ask_user_origin(self):
        result = self.analyzer.analyze(
            "De onde eu sou?"
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.ASK_USER_FACT
        )

        self.assertEqual(
            result["subject"],
            "origin"
        )

    # =====================================
    # Preferências
    # =====================================

    def test_ask_user_game_preference(self):
        result = self.analyzer.analyze(
            "Qual é meu jogo favorito?"
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.ASK_USER_PREFERENCE
        )

        self.assertEqual(
            result["subject"],
            "game"
        )

    def test_ask_user_animal_preference(self):
        result = self.analyzer.analyze(
            "Qual é meu animal favorito?"
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.ASK_USER_PREFERENCE
        )

        self.assertEqual(
            result["subject"],
            "animal"
        )

    def test_ask_user_film_preference(self):
        result = self.analyzer.analyze(
            "Qual é meu filme favorito?"
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.ASK_USER_PREFERENCE
        )

        self.assertEqual(
            result["subject"],
            "film"
        )

    def test_ask_user_series_preference(self):
        result = self.analyzer.analyze(
            "Qual é minha série favorita?"
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.ASK_USER_PREFERENCE
        )

        self.assertEqual(
            result["subject"],
            "series"
        )

    def test_ask_user_music_preference(self):
        result = self.analyzer.analyze(
            "Qual é minha música favorita?"
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.ASK_USER_PREFERENCE
        )

        self.assertEqual(
            result["subject"],
            "music"
        )

    def test_ask_user_general_preference(self):
        result = self.analyzer.analyze(
            "Qual é minha preferência?"
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.ASK_USER_PREFERENCE
        )

        self.assertEqual(
            result["subject"],
            "preference"
        )

    # =====================================
    # Normalização
    # =====================================

    def test_without_accents(self):
        result = self.analyzer.analyze(
            "Qual e meu jogo favorito?"
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.ASK_USER_PREFERENCE
        )

        self.assertEqual(
            result["subject"],
            "game"
        )

    def test_uppercase(self):
        result = self.analyzer.analyze(
            "QUAL E MEU JOGO FAVORITO?"
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.ASK_USER_PREFERENCE
        )

        self.assertEqual(
            result["subject"],
            "game"
        )

    # =====================================
    # Entrada vazia
    # =====================================

    def test_empty_message(self):
        result = self.analyzer.analyze(
            ""
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.UNKNOWN
        )

        self.assertIsNone(
            result["subject"]
        )

    def test_none_message(self):
        result = self.analyzer.analyze(
            None
        )

        self.assertEqual(
            result["intent"],
            IntentTypes.UNKNOWN
        )

        self.assertIsNone(
            result["subject"]
        )


if __name__ == "__main__":
    unittest.main()

    def test_semantic_game(self):

        result = self.analyzer.analyze(
        "você lembra daquele jogo que eu gosto?"
    )

        self.assertEqual(
        result["subject"],
        "game"
    )


def test_semantic_film(self):

    result = self.analyzer.analyze(
        "lembra qual filme eu gosto?"
    )

    self.assertEqual(
        result["subject"],
        "film"
    )


def test_semantic_city(self):

    result = self.analyzer.analyze(
        "você sabe onde eu moro?"
    )

    self.assertEqual(
        result["subject"],
        "city"
    )

    