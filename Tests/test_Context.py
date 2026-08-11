import unittest

from Context.ContextManager import ContextManager


class TestContextManager(unittest.TestCase):

    # =====================================
    # Criação
    # =====================================

    def test_initial_context(self):

        context_manager = ContextManager()

        context = context_manager.get_all()

        self.assertIsNone(
            context["message"]
        )

        self.assertIsNone(
            context["original_message"]
        )

        self.assertIsNone(
            context["intent"]
        )

        self.assertIsNone(
            context["last_response"]
        )

    # =====================================
    # Nova interação
    # =====================================

    def test_new_interaction(self):

        context_manager = ContextManager()

        context_manager.new_interaction(
            "Olá A.R.G."
        )

        self.assertEqual(
            context_manager.get("message"),
            "Olá A.R.G."
        )

        self.assertEqual(
            context_manager.get("original_message"),
            "Olá A.R.G."
        )

    # =====================================
    # Atualização
    # =====================================

    def test_update(self):

        context_manager = ContextManager()

        context_manager.update(
            "message",
            "teste"
        )

        self.assertEqual(
            context_manager.get("message"),
            "teste"
        )

    # =====================================
    # Intenção
    # =====================================

    def test_set_intent(self):

        context_manager = ContextManager()

        context_manager.set_intent(
            "GREETING"
        )

        self.assertEqual(
            context_manager.get("intent"),
            "GREETING"
        )

    # =====================================
    # Resposta
    # =====================================

    def test_set_response(self):

        context_manager = ContextManager()

        context_manager.set_response(
            "Olá!"
        )

        self.assertEqual(
            context_manager.get("last_response"),
            "Olá!"
        )

    # =====================================
    # Limpeza
    # =====================================

    def test_clear(self):

        context_manager = ContextManager()

        context_manager.new_interaction(
            "teste"
        )

        context_manager.set_intent(
            "GREETING"
        )

        context_manager.set_response(
            "Olá!"
        )

        context_manager.clear()

        context = context_manager.get_all()

        self.assertIsNone(
            context["message"]
        )

        self.assertIsNone(
            context["intent"]
        )

        self.assertIsNone(
            context["last_response"]
        )


if __name__ == "__main__":

    unittest.main()