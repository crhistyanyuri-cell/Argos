from Brain.IntentTypes import IntentTypes


class IdentityHandler:

    def process(self, context, manager):

        intent = context.get("intent")

        if intent == IntentTypes.ASK_AI_NAME:

            return self.get_name(manager)

        if intent == IntentTypes.ASK_AI_VERSION:

            return self.get_version(manager)

        if intent == IntentTypes.ASK_AI_LANGUAGE:

            return self.get_language(manager)

        return None

    # =====================================
    # Nome
    # =====================================

    def get_name(self, manager):

        config = manager.get("config")

        if config is None:

            return "Não consegui acessar minhas configurações."

        return f"Meu nome é {config.name}."

    # =====================================
    # Versão
    # =====================================

    def get_version(self, manager):

        config = manager.get("config")

        if config is None:

            return "Não consegui acessar minhas configurações."

        return f"Estou na versão {config.version}."

    # =====================================
    # Idioma
    # =====================================

    def get_language(self, manager):

        config = manager.get("config")

        if config is None:

            return "Não consegui acessar minhas configurações."

        return f"Meu idioma principal é {config.language}."