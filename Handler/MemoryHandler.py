from Brain.IntentTypes import IntentTypes


class MemoryHandler:

    def process(self, context, manager):

        intent = context.get("intent")

        if intent == IntentTypes.REMEMBER_USER_NAME:

            return self.remember_user_name(context, manager)

        if intent == IntentTypes.ASK_USER_NAME:

            return self.get_user_name(manager)

        return None

    # =====================================
    # Lembrar nome
    # =====================================

    def remember_user_name(self, context, manager):

        message = context.get("original_message")

        if not message:

            return "Não consegui identificar seu nome."

        name = self.extract_name(message)

        if not name:

            return "Não consegui identificar seu nome."

        memory_manager = manager.get("memory_manager")

        if memory_manager is None:

            return "Não consegui acessar minha memória."

        memory_manager.set_user_name(name)

        return f"Prazer, {name}! Vou lembrar do seu nome."

    # =====================================
    # Consultar nome
    # =====================================

    def get_user_name(self, manager):

        memory_manager = manager.get("memory_manager")

        if memory_manager is None:

            return "Não consegui acessar minha memória."

        name = memory_manager.get_user_name()

        if not name:

            return "Ainda não sei seu nome."

        return f"Seu nome é {name}."

    # =====================================
    # Extração do nome
    # =====================================

    def extract_name(self, message):

        prefixes = [
            "meu nome é",
            "meu nome e",
            "me chamo",
            "pode me chamar de"
        ]

        message_lower = message.lower()

        for prefix in prefixes:

            if prefix in message_lower:

                start = message_lower.find(prefix) + len(prefix)

                name = message[start:].strip()

                name = name.strip(" .,!?:;")

                if name:

                    return name

        return None