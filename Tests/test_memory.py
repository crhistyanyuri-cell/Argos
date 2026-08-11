import unittest
import tempfile
from pathlib import Path

from Memory.Memory import Memory
from Memory.MemoryManager import MemoryManager


class TestMemory(unittest.TestCase):

    def setUp(self):

        self.temp_dir = tempfile.TemporaryDirectory()

        self.memory_file = (
            Path(self.temp_dir.name)
            / "memory.json"
        )

        self.memory = Memory(
            self.memory_file
        )

        self.memory_manager = MemoryManager(
            self.memory
        )

    def tearDown(self):

        self.temp_dir.cleanup()

    # =====================================
    # Salvar
    # =====================================

    def test_save_and_load(self):

        self.memory_manager.save(
            "test_key",
            "test_value"
        )

        result = self.memory_manager.load(
            "test_key"
        )

        self.assertEqual(
            result,
            "test_value"
        )

    # =====================================
    # Valor padrão
    # =====================================

    def test_load_default(self):

        result = self.memory_manager.load(
            "unknown",
            "default"
        )

        self.assertEqual(
            result,
            "default"
        )

    # =====================================
    # Remover
    # =====================================

    def test_delete(self):

        self.memory_manager.save(
            "test_key",
            "test_value"
        )

        self.memory_manager.delete(
            "test_key"
        )

        result = self.memory_manager.load(
            "test_key"
        )

        self.assertIsNone(result)

    # =====================================
    # Persistência
    # =====================================

    def test_persistence(self):

        self.memory_manager.save(
            "persistent",
            "data"
        )

        new_memory = Memory(
            self.memory_file
        )

        new_memory_manager = MemoryManager(
            new_memory
        )

        result = new_memory_manager.load(
            "persistent"
        )

        self.assertEqual(
            result,
            "data"
        )

    # =====================================
    # Memória completa
    # =====================================

    def test_get_all(self):

        self.memory_manager.save(
            "one",
            1
        )

        self.memory_manager.save(
            "two",
            2
        )

        result = self.memory_manager.get_all()

        self.assertEqual(
            result["one"],
            1
        )

        self.assertEqual(
            result["two"],
            2
        )


if __name__ == "__main__":

    unittest.main()