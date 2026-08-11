import unittest

from Brain.IntentTypes import IntentTypes

from Handler.GreetingHandler import GreetingHandler
from Handler.IdentityHandler import IdentityHandler
from Handler.MemoryHandler import MemoryHandler
from Handler.QuestionHandler import QuestionHandler


class TestHandlers(unittest.TestCase):

    # =====================================
    # GreetingHandler
    # =====================================

    def test_greeting_handler(self):

        handler = GreetingHandler()

        context = {
            "message": "olá",
            "original_message": "Olá",
            "intent": IntentTypes.GREETING,
            "last_response": None
        }

        response = handler.process(
            context,
            None
        )

        self.assertIsNotNone(response)

        self.assertIsInstance(
            response,
            str
        )

    # =====================================
    # IdentityHandler
    # =====================================

    def test_identity_handler(self):

        handler = IdentityHandler()

        context = {
            "message": "qual é seu nome",
            "original_message": "Qual é seu nome?",
            "intent": IntentTypes.ASK_AI_NAME,
            "last_response": None
        }

        manager = FakeManager()

        manager.register(
            "config",
            FakeConfig()
        )

        response = handler.process(
            context,
            manager
        )

        self.assertIsNotNone(response)

        self.assertIsInstance(
            response,
            str
        )

    # =====================================
    # MemoryHandler
    # =====================================

    def test_memory_handler(self):

        handler = MemoryHandler()

        context = {
            "message": "qual é meu nome",
            "original_message": "Qual é meu nome?",
            "intent": IntentTypes.ASK_USER_NAME,
            "last_response": None
        }

        memory_manager = FakeMemoryManager()

        memory_manager.set_user_name(
            "Teste"
        )

        manager = FakeManager()

        manager.register(
            "memory_manager",
            memory_manager
        )

        response = handler.process(
            context,
            manager
        )

        self.assertIsNotNone(response)

        self.assertIsInstance(
            response,
            str
        )

    # =====================================
    # QuestionHandler
    # =====================================

    def test_question_handler(self):

        handler = QuestionHandler()

        context = {
            "message": "o que é uma estrela",
            "original_message": "O que é uma estrela?",
            "intent": IntentTypes.UNKNOWN,
            "last_response": None
        }

        response = handler.process(
            context,
            None
        )

        self.assertIsNotNone(response)

        self.assertIsInstance(
            response,
            str
        )


# =========================================
# Fakes para os testes
# =========================================

class FakeManager:

    def __init__(self):

        self.modules = {}

    def register(self, name, module):

        self.modules[name] = module

    def get(self, name):

        return self.modules.get(name)


class FakeConfig:

    name = "A.R.G."
    version = "0.1.0"
    language = "pt-BR"


class FakeMemoryManager:

    def __init__(self):

        self.data = {}

    def set_user_name(self, name):

        self.data["user_name"] = name

    def get_user_name(self):

        return self.data.get(
            "user_name"
        )


if __name__ == "__main__":

    unittest.main()