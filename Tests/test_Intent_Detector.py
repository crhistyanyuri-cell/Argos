import unittest

from Brain.IntentDetector import IntentDetector
from Brain.IntentTypes import IntentTypes


class TestIntentDetector(unittest.TestCase):

    def setUp(self):

        self.detector = IntentDetector()

    # =====================================
    # Saudações
    # =====================================

    def test_greeting(self):

        result = self.detector.detect(
            "Olá"
        )

        self.assertEqual(
            result,
            IntentTypes.GREETING
        )

    def test_good_morning(self):

        result = self.detector.detect(
            "Bom dia"
        )

        self.assertEqual(
            result,
            IntentTypes.GREETING
        )

    # =====================================
    # Normalização
    # =====================================

    def test_uppercase(self):

        result = self.detector.detect(
            "OLÁ"
        )

        self.assertEqual(
            result,
            IntentTypes.GREETING
        )

    def test_extra_spaces(self):

        result = self.detector.detect(
            "   bom    dia   "
        )

        self.assertEqual(
            result,
            IntentTypes.GREETING
        )

    def test_without_accents(self):

        result = self.detector.detect(
            "Qual e seu nome?"
        )

        self.assertEqual(
            result,
            IntentTypes.ASK_AI_NAME
        )

    # =====================================
    # Identidade do A.R.G.O.S.
    # =====================================

    def test_ask_ai_name(self):

        result = self.detector.detect(
            "Qual é seu nome?"
        )

        self.assertEqual(
            result,
            IntentTypes.ASK_AI_NAME
        )

    def test_ask_ai_version(self):

        result = self.detector.detect(
            "Qual é sua versão?"
        )

        self.assertEqual(
            result,
            IntentTypes.ASK_AI_VERSION
        )

    def test_ask_ai_language(self):

        result = self.detector.detect(
            "Qual é seu idioma?"
        )

        self.assertEqual(
            result,
            IntentTypes.ASK_AI_LANGUAGE
        )

    # =====================================
    # Memória
    # =====================================

    def test_remember_user_name(self):

        result = self.detector.detect(
            "Meu nome é Carlos"
        )

        self.assertEqual(
            result,
            IntentTypes.REMEMBER_USER_NAME
        )

    def test_ask_user_name(self):

        result = self.detector.detect(
            "Qual é meu nome?"
        )

        self.assertEqual(
            result,
            IntentTypes.ASK_USER_NAME
        )

    def test_remember_name_with_me_chamo(self):

        result = self.detector.detect(
            "Me chamo Carlos"
        )

        self.assertEqual(
            result,
            IntentTypes.REMEMBER_USER_NAME
        )

    # =====================================
    # Aprendizado
    # =====================================

    def test_learn_preference(self):

        result = self.detector.detect(
            "Eu gosto de música"
        )

        self.assertEqual(
            result,
            IntentTypes.LEARN_PREFERENCE
        )

    def test_learn_fact(self):

        result = self.detector.detect(
            "Eu moro no Brasil"
        )

        self.assertEqual(
            result,
            IntentTypes.LEARN_FACT
        )

    # =====================================
    # Falsos positivos
    # =====================================

    def test_not_remember_name_with_eu_sou(self):

        result = self.detector.detect(
            "Eu sou muito feliz hoje"
        )

        self.assertNotEqual(
            result,
            IntentTypes.REMEMBER_USER_NAME
        )

    # =====================================
    # Desconhecido
    # =====================================

    def test_unknown(self):

        result = self.detector.detect(
            "xyz mensagem completamente aleatória"
        )

        self.assertEqual(
            result,
            IntentTypes.UNKNOWN
        )

    # =====================================
    # Entrada vazia
    # =====================================

    def test_empty_message(self):

        result = self.detector.detect(
            ""
        )

        self.assertEqual(
            result,
            IntentTypes.UNKNOWN
        )

    def test_none_message(self):

        result = self.detector.detect(
            None
        )

        self.assertEqual(
            result,
            IntentTypes.UNKNOWN
        )


if __name__ == "__main__":
    unittest.main()

    # =====================================
# Consulta de preferências
# =====================================

def test_ask_user_game_preference(self):

    result = self.detector.detect(
        "Qual é o meu jogo favorito?"
    )

    self.assertEqual(
        result,
        IntentTypes.ASK_USER_PREFERENCE
    )


def test_ask_user_animal_preference(self):

    result = self.detector.detect(
        "Qual é o meu animal favorito?"
    )

    self.assertEqual(
        result,
        IntentTypes.ASK_USER_PREFERENCE
    )


def test_ask_user_preference_without_accents(self):

    result = self.detector.detect(
        "Qual e o meu jogo favorito?"
    )

    self.assertEqual(
        result,
        IntentTypes.ASK_USER_PREFERENCE
    )