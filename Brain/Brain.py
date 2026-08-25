from .MessageAnalyzer import MessageAnalyzer


class Brain:

    def __init__(self):

        self.last_thought = None
        self.message_analyzer = MessageAnalyzer()

    # =====================================
    # Processamento principal
    # =====================================

    def think(self, message, manager):

        if not message:
            return None

        context_manager = manager.get(
            "context_manager"
        )

        handler_manager = manager.get(
            "handler_manager"
        )

        if context_manager is None:
            return "Erro: ContextManager não encontrado."

        if handler_manager is None:
            return "Erro: HandlerManager não encontrado."

        # =================================
        # Guardar contexto anterior
        # =================================

        previous_context = context_manager.get_all()

        previous_subject = previous_context.get(
            "subject"
        )

        # =================================
        # Nova interação
        # =================================

        context_manager.new_interaction(
            message
        )

        # =================================
        # Analisar mensagem
        # =================================

        analysis = self.message_analyzer.analyze(
            message
        )

        intent = analysis["intent"]
        subject = analysis["subject"]

        # =================================
        # Recuperar assunto anterior
        # =================================

        semantic = self.message_analyzer.semantic_analyzer.analyze(
            message
        )

        if (
            subject is None
            and semantic["memory_related"]
            and previous_subject is not None
        ):
            subject = previous_subject

        # =================================
        # Corrigir intenção após recuperar
        # assunto
        # =================================

        if semantic["question"] and subject is not None:

            if subject in (
                "game",
                "animal",
                "film",
                "series",
                "music",
                "preference"
            ):
                from Brain.IntentTypes import IntentTypes

                intent = IntentTypes.ASK_USER_PREFERENCE

            elif subject == "origin":

                from Brain.IntentTypes import IntentTypes

                intent = IntentTypes.ASK_USER_FACT

            elif subject == "city":

                from Brain.IntentTypes import IntentTypes

                intent = IntentTypes.ASK_USER_CITY

            elif subject == "name":

                from Brain.IntentTypes import IntentTypes

                intent = IntentTypes.ASK_USER_NAME

        # =================================
        # Atualizar contexto
        # =================================

        context_manager.set_intent(
            intent
        )

        context_manager.update(
            "subject",
            subject
        )

        # =================================
        # Processar Handler
        # =================================

        response = handler_manager.process(
            context_manager.get_all(),
            manager
        )

        # =================================
        # Resposta
        # =================================

        if response is not None:

            self.last_thought = response

            context_manager.set_response(
                response
            )

            return response

        # =================================
        # Sem resposta
        # =================================

        self.last_thought = None

        return "Ainda estou aprendendo."

    # =====================================
    # Último pensamento
    # =====================================

    def get_last_thought(self):

        return self.last_thought