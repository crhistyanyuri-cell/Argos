import unittest

from Brain.Brain import Brain
from Brain.IntentTypes import IntentTypes


class FakeContextManager:

    def __init__(self):

        self.context = {
            "message": None,
            "original_message": None,
            "intent": None,
            "response": None
        }

    def new_interaction(self, message):

        self.context["message"] = message
        self.context["original_message"] = message
        self.context["response"] = None

    def set_intent(self, intent):

        self.context["intent"] = intent

    def set_response(self, response):

        self.context["response"] = response

    def get_all(self):

        return self.context.copy()


class FakeHandlerManager:

    def __init__(self, response=None):

        self.response = response
        self.last_context = None

    def process(self, context, manager):

        self.last_context = context

        return self.response


class FakeManager:

    def __init__(
        self,
        context_manager,
        handler_manager
    ):

        self.modules = {
            "context_manager": context_manager,
            "handler_manager": handler_manager
        }

    def get(self, name):

        return self.modules.get(name)


class TestBrain(unittest.TestCase):

    def setUp(self):

        self.brain = Brain()

        self.context_manager = FakeContextManager()

        self.handler_manager = FakeHandlerManager()

        self.manager = FakeManager(
            self.context_manager,
            self.handler_manager
        )

    # =====================================
    # Mensagem vazia
    # =====================================

    def test_empty_message(self):

        result = self.brain.think(
            "",
            self.manager
        )

        self.assertIsNone(
            result
        )

    # =====================================
    # Mensagem None
    # =====================================

    def test_none_message(self):

        result = self.brain.think(
            None,
            self.manager
        )

        self.assertIsNone(
            result
        )

    # =====================================
    # Detectar saudação
    # =====================================

    def test_greeting_intent(self):

        self.brain.think(
            "Olá",
            self.manager
        )

        self.assertEqual(
            self.context_manager.context["intent"],
            IntentTypes.GREETING
        )

    # =====================================
    # Detectar preferência
    # =====================================

    def test_preference_intent(self):

        self.brain.think(
            "Eu gosto de gatos",
            self.manager
        )

        self.assertEqual(
            self.context_manager.context["intent"],
            IntentTypes.LEARN_PREFERENCE
        )

    # =====================================
    # Resposta do Handler
    # =====================================

    def test_handler_response(self):

        self.handler_manager.response = (
            "Resposta de teste."
        )

        result = self.brain.think(
            "Olá",
            self.manager
        )

        self.assertEqual(
            result,
            "Resposta de teste."
        )

        self.assertEqual(
            self.brain.get_last_thought(),
            "Resposta de teste."
        )

    # =====================================
    # Sem resposta do Handler
    # =====================================

    def test_no_handler_response(self):

        self.handler_manager.response = None

        result = self.brain.think(
            "Mensagem desconhecida",
            self.manager
        )

        self.assertEqual(
            result,
            "Ainda estou aprendendo."
        )

        self.assertIsNone(
            self.brain.get_last_thought()
        )

    # =====================================
    # Contexto recebe resposta
    # =====================================

    def test_context_response(self):

        self.handler_manager.response = (
            "Resposta de teste."
        )

        self.brain.think(
            "Olá",
            self.manager
        )

        self.assertEqual(
            self.context_manager.context["response"],
            "Resposta de teste."
        )

    # =====================================
    # ContextManager ausente
    # =====================================

    def test_missing_context_manager(self):

        manager = FakeManager(
            None,
            self.handler_manager
        )

        result = self.brain.think(
            "Olá",
            manager
        )

        self.assertEqual(
            result,
            "Erro: ContextManager não encontrado."
        )

    # =====================================
    # HandlerManager ausente
    # =====================================

    def test_missing_handler_manager(self):

        manager = FakeManager(
            self.context_manager,
            None
        )

        result = self.brain.think(
            "Olá",
            manager
        )

        self.assertEqual(
            result,
            "Erro: HandlerManager não encontrado."
        )


if __name__ == "__main__":

    unittest.main()