import unittest

from Learning.Learning import Learning
from Memory.Memory import Memory
from Memory.MemoryManager import MemoryManager


class TestLearning(unittest.TestCase):

    def setUp(self):

        self.memory = Memory()

        self.memory_manager = MemoryManager(
            self.memory
        )

        self.learning = Learning(
            self.memory_manager
        )

    # =====================================
    # Fato
    # =====================================

    def test_learn_fact(self):

        result = self.learning.learn_fact(
            "eu tenho um gato"
        )

        self.assertTrue(result)

        facts = self.memory_manager.get_facts()

        self.assertIn(
            "eu tenho um gato",
            facts
        )

    # =====================================
    # Fato vazio
    # =====================================

    def test_learn_empty_fact(self):

        result = self.learning.learn_fact(
            ""
        )

        self.assertFalse(result)

    # =====================================
    # Preferência
    # =====================================

    def test_learn_preference(self):

        result = self.learning.learn_preference(
            "animal_favorito",
            "gato"
        )

        self.assertTrue(result)

        preference = self.memory_manager.get_preference(
            "animal_favorito"
        )

        self.assertEqual(
            preference,
            "gato"
        )

    # =====================================
    # Preferência inválida
    # =====================================

    def test_learn_empty_preference(self):

        result = self.learning.learn_preference(
            "",
            "gato"
        )

        self.assertFalse(result)

        result = self.learning.learn_preference(
            "animal_favorito",
            ""
        )

        self.assertFalse(result)

    # =====================================
    # Nome
    # =====================================

    def test_learn_name(self):

        result = self.learning.learn_name(
            "Carlos"
        )

        self.assertTrue(result)

        name = self.memory_manager.get_user_name()

        self.assertEqual(
            name,
            "Carlos"
        )

    # =====================================
    # Nome vazio
    # =====================================

    def test_learn_empty_name(self):

        result = self.learning.learn_name(
            ""
        )

        self.assertFalse(result)

    # =====================================
    # Idade
    # =====================================

    def test_learn_age(self):

        result = self.learning.learn_age(
            17
        )

        self.assertTrue(result)

        age = self.memory_manager.load(
            "age"
        )

        self.assertEqual(
            age,
            17
        )

    # =====================================
    # Cidade
    # =====================================

    def test_learn_city(self):

        result = self.learning.learn_city(
            "Brasília"
        )

        self.assertTrue(result)

        city = self.memory_manager.load(
            "city"
        )

        self.assertEqual(
            city,
            "Brasília"
        )


if __name__ == "__main__":

    unittest.main()