import re
import unicodedata

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

        message = context.get(
            "original_message"
        )

        if not message:
            return False

        name = self.extract_name(
            message
        )

        if not name:
            return False

        return self.learning.learn_name(
            name
        )

    # =====================================
    # Fato
    # =====================================

    def learn_fact(self, context):

        message = context.get(
            "original_message"
        )

        if not message:
            return False

        fact = self.extract_fact(
            message
        )

        if not fact:
            return False

        return self.learning.learn_fact(
            fact
        )

    # =====================================
    # Preferência
    # =====================================

    def learn_preference(self, context):

        message = context.get(
            "original_message"
        )

        if not message:
            return False

        preference = self.extract_preference(
            message
        )

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

        message_lower = self.normalize(
            message
        )

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

        message_lower = self.normalize(
            message
        )

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

        normalized = self.normalize(
            message
        )

        # =================================
        # Preferências estruturadas
        # =================================

        patterns = [

            # meu animal favorito é gato
            r"^meu\s+(.+?)\s+favorito\s+e\s+(.+)$",

            # minha cor favorita é roxo
            r"^minha\s+(.+?)\s+favorita\s+e\s+(.+)$",

            # meu jogo preferido é Minecraft
            r"^meu\s+(.+?)\s+preferido\s+e\s+(.+)$",

            # minha personagem preferida é Zelda
            r"^minha\s+(.+?)\s+preferida\s+e\s+(.+)$"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                normalized
            )

            if not match:
                continue

            subject = match.group(1).strip()
            value = match.group(2).strip()

            if not subject or not value:
                return None

            key = self.build_preference_key(
                subject
            )

            # =================================
            # Recuperar valor da mensagem original
            # =================================

            original_value = self.extract_original_value(
                message,
                normalized,
                value
            )

            return key, original_value

        # =================================
        # Preferências gerais
        # =================================

        general_patterns = [
            "eu gosto de",
            "eu gosto",
            "eu prefiro",
            "minha preferência é",
            "minha preferencia e"
        ]

        for pattern in general_patterns:

            normalized_pattern = self.normalize(
                pattern
            )

            if normalized_pattern in normalized:

                start = (
                    normalized.find(
                        normalized_pattern
                    )
                    + len(normalized_pattern)
                )

                value = message[start:].strip()

                value = value.strip(
                    " .,!?:;"
                )

                if value:

                    return "general", value

        return None

    # =====================================
    # Criar chave
    # =====================================

    def build_preference_key(self, subject):

        subject = subject.strip()

        subject = " ".join(
            subject.split()
        )

        subject = subject.replace(
            " ",
            "_"
        )

        return f"{subject}_favorito"

    # =====================================
    # Recuperar valor original
    # =====================================

    def extract_original_value(
        self,
        original_message,
        normalized_message,
        normalized_value
    ):

        start = normalized_message.rfind(
            normalized_value
        )

        if start == -1:

            return normalized_value

        original_value = (
            original_message[start:]
        )

        original_value = original_value.strip(
            " .,!?:;"
        )

        if original_value:

            return original_value

        return normalized_value

    # =====================================
    # Normalização
    # =====================================

    def normalize(self, message):

        message = str(message)

        message = message.lower().strip()

        message = unicodedata.normalize(
            "NFD",
            message
        )

        message = "".join(
            char
            for char in message
            if unicodedata.category(char) != "Mn"
        )

        message = re.sub(
            r"[!?.,;:]",
            "",
            message
        )

        message = re.sub(
            r"\s+",
            " ",
            message
        )

        return message.strip()