class ContextManager:

    def __init__(self):

        self.context = self.create_context()

    # =====================================
    # Criar contexto
    # =====================================

    def create_context(self):

        return {
            "message": None,
            "original_message": None,
            "intent": None,
            "last_response": None
        }

    # =====================================
    # Atualizar contexto
    # =====================================

    def update(self, key, value):

        self.context[key] = value

    # =====================================
    # Obter valor
    # =====================================

    def get(self, key, default=None):

        return self.context.get(
            key,
            default
        )

    # =====================================
    # Obter contexto completo
    # =====================================

    def get_all(self):

        return self.context.copy()

    # =====================================
    # Limpar contexto
    # =====================================

    def clear(self):

        self.context = self.create_context()

    # =====================================
    # Novo ciclo de interação
    # =====================================

    def new_interaction(self, message):

        self.context = self.create_context()

        self.context["original_message"] = message

        self.context["message"] = message

    # =====================================
    # Definir intenção
    # =====================================

    def set_intent(self, intent):

        self.context["intent"] = intent

    # =====================================
    # Definir resposta
    # =====================================

    def set_response(self, response):

        self.context["last_response"] = response