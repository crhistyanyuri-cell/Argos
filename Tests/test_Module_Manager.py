import unittest

from Core.ModuleManager import ModuleManager


class TestModuleManager(unittest.TestCase):

    # =====================================
    # Registro
    # =====================================

    def test_register_module(self):

        manager = ModuleManager()

        module = object()

        manager.register(
            "test",
            module
        )

        self.assertIs(
            manager.get("test"),
            module
        )

    # =====================================
    # Recuperação
    # =====================================

    def test_get_unknown_module(self):

        manager = ModuleManager()

        result = manager.get(
            "unknown"
        )

        self.assertIsNone(result)

    # =====================================
    # Múltiplos módulos
    # =====================================

    def test_register_multiple_modules(self):

        manager = ModuleManager()

        config = object()
        logger = object()

        manager.register(
            "config",
            config
        )

        manager.register(
            "logger",
            logger
        )

        self.assertIs(
            manager.get("config"),
            config
        )

        self.assertIs(
            manager.get("logger"),
            logger
        )


if __name__ == "__main__":

    unittest.main()