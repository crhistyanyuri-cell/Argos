from Brain.IntentTypes import IntentTypes


class MemoryHandler:

    def process(self, context, manager):

        intent = context.get(
            "intent"
        )

        # =====================================
        # Lembrar nome
        # =====================================

        if intent == IntentTypes.REMEMBER_USER_NAME:

            return self.remember_user_name(
                context,
                manager
            )

        # =====================================
        # Consultar memória
        # =====================================

        if intent in (
            IntentTypes.ASK_USER_NAME,
            IntentTypes.ASK_USER_CITY,
            IntentTypes.ASK_USER_FACT,
            IntentTypes.ASK_USER_PREFERENCE
        ):

            return self.query_memory(
                context,
                manager
            )

        return None

    # =====================================
    # Consultar memória
    # =====================================

    def query_memory(
        self,
        context,
        manager
    ):

        memory_query = manager.get(
            "memory_query"
        )

        if memory_query is None:

            return (
                "Não consegui acessar "
                "meu sistema de memória."
            )

        message = context.get(
            "original_message"
        )

        if not message:

            return (
                "Não consegui identificar "
                "o que você quer consultar."
            )

        result = memory_query.query(
            message
        )

        if result is None:

            return (
                "Ainda não tenho "
                "essa informação."
            )

        result_type = result.get(
            "type"
        )

        value = result.get(
            "value"
        )

        # =================================
        # Nome
        # =================================

        if result_type == "name":

            return (
                f"Seu nome é {value}."
            )

        # =================================
        # Cidade
        # =================================

        if result_type == "city":

            return (
                f"Você mora em {value}."
            )

        # =================================
        # Fato
        # =================================

        if result_type == "fact":

            return self.format_fact(
                value
            )

        # =================================
        # Preferência
        # =================================

        if result_type == "preference":

            key = result.get(
                "key"
            )

            return self.format_preference(
                key,
                value
            )

        return (
            "Encontrei a informação, "
            "mas ainda não sei como "
            "responder a essa pergunta."
        )

    # =====================================
    # Formatar fato
    # =====================================

    def format_fact(self, fact):

        fact_lower = fact.lower()

        # =================================
        # Origem
        # =================================

        if fact_lower.startswith(
            "eu sou de "
        ):

            origin = fact[
                len("eu sou de "):
            ].strip()

            return (
                f"Você é de {origin}."
            )

        # =================================
        # Moradia
        # =================================

        if fact_lower.startswith(
            "eu moro em "
        ):

            place = fact[
                len("eu moro em "):
            ].strip()

            return (
                f"Você mora em {place}."
            )

        # =================================
        # Fato genérico
        # =================================

        if fact_lower.startswith(
            "eu "
        ):

            content = fact[
                len("eu "):
            ].strip()

            return (
                f"Você {content}."
            )

        return fact

    # =====================================
    # Formatar preferência
    # =====================================

    def format_preference(
        self,
        key,
        value
    ):

        labels = {

            "jogo_favorito":
                "Seu jogo favorito",

            "animal_favorito":
                "Seu animal favorito",

            "filme_favorito":
                "Seu filme favorito",

            "serie_favorita":
                "Sua série favorita",

            "musica_favorita":
                "Sua música favorita",

            "general":
                "Sua preferência"
        }

        label = labels.get(
            key,
            key.replace(
                "_",
                " "
            ).capitalize()
        )

        return (
            f"{label} é {value}."
        )

    # =====================================
    # Lembrar nome
    # =====================================

    def remember_user_name(
        self,
        context,
        manager
    ):

        message = context.get(
            "original_message"
        )

        if not message:

            return (
                "Não consegui "
                "identificar seu nome."
            )

        name = self.extract_name(
            message
        )

        if not name:

            return (
                "Não consegui "
                "identificar seu nome."
            )

        memory_manager = manager.get(
            "memory_manager"
        )

        if memory_manager is None:

            return (
                "Não consegui acessar "
                "minha memória."
            )

        memory_manager.set_user_name(
            name
        )

        return (
            f"Prazer, {name}! "
            f"Vou lembrar do seu nome."
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

                name = message[
                    start:
                ].strip()

                name = name.strip(
                    " .,!?:;"
                )

                if name:

                    return name

        return None