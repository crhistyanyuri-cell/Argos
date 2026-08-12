from Brain.IntentTypes import IntentTypes


class MemoryHandler:

    def process(self, context, manager):

        intent = context.get("intent")

        # =====================================
        # Lembrar nome
        # =====================================

        if intent == IntentTypes.REMEMBER_USER_NAME:

            return self.remember_user_name(
                context,
                manager
            )

        # =====================================
        # Consultar nome
        # =====================================

        if intent == IntentTypes.ASK_USER_NAME:

            return self.get_user_name(
                manager
            )

        # =====================================
        # Consultar preferência
        # =====================================

        if intent == IntentTypes.ASK_USER_PREFERENCE:

            return self.get_user_preference(
                context,
                manager
            )

        return None

    # =====================================
    # Lembrar nome
    # =====================================

    def remember_user_name(self, context, manager):

        message = context.get(
            "original_message"
        )

        if not message:

            return "Não consegui identificar seu nome."

        name = self.extract_name(
            message
        )

        if not name:

            return "Não consegui identificar seu nome."

        memory_manager = manager.get(
            "memory_manager"
        )

        if memory_manager is None:

            return "Não consegui acessar minha memória."

        memory_manager.set_user_name(
            name
        )

        return (
            f"Prazer, {name}! "
            f"Vou lembrar do seu nome."
        )

    # =====================================
    # Consultar nome
    # =====================================

    def get_user_name(self, manager):

        memory_manager = manager.get(
            "memory_manager"
        )

        if memory_manager is None:

            return "Não consegui acessar minha memória."

        name = memory_manager.get_user_name()

        if not name:

            return "Ainda não sei seu nome."

        return f"Seu nome é {name}."

    # =====================================
    # Consultar preferência
    # =====================================

    def get_user_preference(
        self,
        context,
        manager
    ):

        memory_manager = manager.get(
            "memory_manager"
        )

        if memory_manager is None:

            return "Não consegui acessar minha memória."

        message = context.get(
            "original_message"
        )

        if not message:

            return (
                "Não consegui identificar "
                "qual preferência consultar."
            )

        key = self.extract_preference_key(
            message
        )

        if not key:

            return (
                "Não consegui identificar "
                "qual preferência você quer consultar."
            )

        value = memory_manager.get_preference(
            key
        )

        if value is None:

            return (
                f"Ainda não tenho uma preferência "
                f"registrada para "
                f"{key.replace('_', ' ')}."
            )

        # =================================
        # Nomes amigáveis
        # =================================

        labels = {

            "jogo_favorito":
                "seu jogo favorito",

            "animal_favorito":
                "seu animal favorito",

            "filme_favorito":
                "seu filme favorito",

            "serie_favorita":
                "sua série favorita",

            "musica_favorita":
                "sua música favorita",

            "general":
                "sua preferência"
        }

        label = labels.get(
            key,
            key.replace(
                "_",
                " "
            )
        )

        return (
            f"{label.capitalize()} é {value}."
        )

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

                start = (
                    message_lower.find(prefix)
                    + len(prefix)
                )

                name = message[start:].strip()

                name = name.strip(
                    " .,!?:;"
                )

                if name:

                    return name

        return None

    # =====================================
    # Extração da chave da preferência
    # =====================================

    def extract_preference_key(self, message):

        message_lower = message.lower()

        # =================================
        # Jogo favorito
        # =================================

        if "jogo favorito" in message_lower:

            return "jogo_favorito"

        # =================================
        # Animal favorito
        # =================================

        if "animal favorito" in message_lower:

            return "animal_favorito"

        # =================================
        # Filme favorito
        # =================================

        if "filme favorito" in message_lower:

            return "filme_favorito"

        # =================================
        # Série favorita
        # =================================

        if "serie favorita" in message_lower:

            return "serie_favorita"

        if "série favorita" in message_lower:

            return "serie_favorita"

        # =================================
        # Música favorita
        # =================================

        if "musica favorita" in message_lower:

            return "musica_favorita"

        if "música favorita" in message_lower:

            return "musica_favorita"

        # =================================
        # Preferência genérica
        # =================================

        if "preferência" in message_lower:

            return "general"

        if "preferencia" in message_lower:

            return "general"

        return None

