from Brain.IntentTypes import IntentTypes


class LearningManager:

    def __init__(self, learning):

        self.learning = learning

    # =====================================
    # Processamento
    # =====================================

    def process(self, context):

        intent = context.get("intent")

        if intent == IntentTypes.LEARN_FACT:

            return self.learn_fact(context)

        if intent == IntentTypes.LEARN_PREFERENCE:

            return self.learn_preference(context)

        if intent == IntentTypes.REMEMBER_USER_NAME:

            return self.learn_name(context)

        return False

    # =====================================
    # Nome
    # =====================================

    def learn_name(self, context):

        message = context.get("original_message")

        if not message:

            return False

        name = self.extract_name(message)

        if not name:

            return False

        return self.learning.learn_name(name)

    # =====================================
    # Fato
    # =====================================

    def learn_fact(self, context):

        message = context.get("original_message")

        if not message:

            return False

        fact = self.extract_fact(message)

        if not fact:

            return False

        return self.learning.learn_fact(fact)

    # =====================================
    # Preferência
    # =====================================

    def learn_preference(self, context):

        message = context.get("original_message")

        if not message:

            return False

        preference = self.extract_preference(message)

        if not preference:

            return False

        key, value = preference

        return self.learning.learn_preference(
            key,
            value
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
    # Extração de fato
    # =====================================

    def extract_fact(self, message):

        prefixes = [
            "eu sou",
            "eu tenho",
            "eu moro",
            "eu faço",
            "eu faco"
        ]

        message_lower = message.lower()

        for prefix in prefixes:

            if prefix in message_lower:

                start = (
                    message_lower.find(prefix)
                    + len(prefix)
                )

                fact = message[start:].strip()

                fact = fact.strip(
                    " .,!?:;"
                )

                if fact:

                    return f"{prefix} {fact}"

        return None

    # =====================================
    # Extração de preferência
    # =====================================

    def extract_preference(self, message):

        patterns = [
            "eu gosto de",
            "eu gosto",
            "eu prefiro",
            "minha preferência é",
            "minha preferencia e"
        ]

        message_lower = message.lower()

        for pattern in patterns:

            if pattern in message_lower:

                start = (
                    message_lower.find(pattern)
                    + len(pattern)
                )

                value = message[start:].strip()

                value = value.strip(
                    " .,!?:;"
                )

                if value:

                    return "general", value

        return None