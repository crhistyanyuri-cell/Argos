import unittest

from Learning.Learning import Learning
from Learning.LearningManager import LearningManager

from Memory.Memory import Memory
from Memory.MemoryManager import MemoryManager

from Brain.IntentTypes import IntentTypes


class TestLearningManager(unittest.TestCase):

    def setUp(self):

        self.memory = Memory()

        self.memory_manager = MemoryManager(
            self.memory
        )

        self.learning = Learning(
            self.memory_manager
        )

        self.learning_manager = LearningManager(
            self.learning
        )

    # =====================================
    # Preferência
    # =====================================

    def test_learn_preference(self):

        context = {
            "intent": IntentTypes.LEARN_PREFERENCE,
            "original_message":
                "meu animal favorito é gato"
        }

        result = self.learning_manager.process(
            context
        )

        self.assertTrue(result)

        value = self.memory_manager.get_preference(
            "animal_favorito"
        )

        self.assertEqual(
            value,
            "gato"
        )

    # =====================================
    # Jogo favorito
    # =====================================

    def test_learn_game_preference(self):

        context = {
            "intent": IntentTypes.LEARN_PREFERENCE,
            "original_message":
                "meu jogo favorito é Dark Souls 2"
        }

        result = self.learning_manager.process(
            context
        )

        self.assertTrue(result)

        value = self.memory_manager.get_preference(
            "jogo_favorito"
        )

        self.assertEqual(
            value,
            "Dark Souls 2"
        )

    # =====================================
    # Fato
    # =====================================

    def test_learn_fact(self):

        context = {
            "intent": IntentTypes.LEARN_FACT,
            "original_message":
                "eu moro no Brasil"
        }

        result = self.learning_manager.process(
            context
        )

        self.assertTrue(result)

        facts = self.memory_manager.get_facts()

        self.assertIn(
            "eu moro no Brasil",
            facts
        )

    # =====================================
    # Nome
    # =====================================

    def test_learn_name(self):

        context = {
            "intent":
                IntentTypes.REMEMBER_USER_NAME,
            "original_message":
                "meu nome é Carlos"
        }

        result = self.learning_manager.process(
            context
        )

        self.assertTrue(result)

        name = self.memory_manager.get_user_name()

        self.assertEqual(
            name,
            "Carlos"
        )

    # =====================================
    # Intenção desconhecida
    # =====================================

    def test_unknown_intent(self):

        context = {
            "intent": IntentTypes.UNKNOWN,
            "original_message": "teste"
        }

        result = self.learning_manager.process(
            context
        )

        self.assertFalse(result)


if __name__ == "__main__":

    unittest.main()