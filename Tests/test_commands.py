
import unittest

from Commands.CommandProcessor import CommandProcessor


class TestCommandProcessor(unittest.TestCase):

    def setUp(self):

        self.processor = CommandProcessor()

    # =====================================
    # Registrar comando
    # =====================================

    def test_register_command(self):

        class TestCommand:

            def execute(self, args=None, manager=None):

                return "teste"

        command = TestCommand()

        self.processor.register(
            "teste",
            command
        )

        self.assertIn(
            "teste",
            self.processor.commands
        )

    # =====================================
    # Comando desconhecido
    # =====================================

    def test_unknown_command(self):

        result = self.processor.process(
            "/inexistente",
            None
        )

        self.assertIsNotNone(
            result
        )

        self.assertEqual(
            result["type"],
            "command"
        )

        self.assertEqual(
            result["name"],
            "inexistente"
        )

        self.assertEqual(
            result["args"],
            []
        )

        self.assertFalse(
            result["found"]
        )

    # =====================================
    # Mensagem normal
    # =====================================

    def test_normal_message(self):

        result = self.processor.process(
            "oi",
            None
        )

        self.assertIsNotNone(
            result
        )

        self.assertEqual(
            result["type"],
            "message"
        )

        self.assertEqual(
            result["content"],
            "oi"
        )

    # =====================================
    # Registrar vários comandos
    # =====================================

    def test_register_multiple_commands(self):

        class TestCommand:

            def execute(self, args=None, manager=None):

                return "teste"

        command1 = TestCommand()
        command2 = TestCommand()

        self.processor.register(
            "teste1",
            command1
        )

        self.processor.register(
            "teste2",
            command2
        )

        self.assertIn(
            "teste1",
            self.processor.commands
        )

        self.assertIn(
            "teste2",
            self.processor.commands
        )


if __name__ == "__main__":

    unittest.main()



