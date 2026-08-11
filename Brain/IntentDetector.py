import re
import unicodedata

from Brain.IntentTypes import IntentTypes


class IntentDetector:

    def __init__(self):

        self.patterns = {

            # =====================================
            # Conversação
            # =====================================

            IntentTypes.GREETING: [
                r"\boi\b",
                r"\bola\b",
                r"\be ai\b",
                r"\beai\b",
                r"\bbom dia\b",
                r"\bboa tarde\b",
                r"\bboa noite\b"
            ],

            # =====================================
            # Identidade do A.R.G.O.S.
            # =====================================

            IntentTypes.ASK_AI_NAME: [
                r"\bseu nome\b",
                r"qual.*seu nome",
                r"como.*chama",
                r"quem.*e voce"
            ],

            IntentTypes.ASK_AI_VERSION: [
                r"qual.*versao",
                r"que versao",
                r"qual.*versao voce esta usando",
                r"qual.*versao do sistema"
            ],

            IntentTypes.ASK_AI_LANGUAGE: [
                r"qual.*idioma",
                r"qual.*lingua",
                r"que idioma",
                r"que lingua"
            ],

            # =====================================
            # Memória
            # =====================================

            IntentTypes.REMEMBER_USER_NAME: [
                r"\bmeu nome e\b",
                r"\bme chamo\b",
                r"\bpode me chamar de\b"
            ],

            IntentTypes.ASK_USER_NAME: [
                r"\bmeu nome\b",
                r"qual.*meu nome",
                r"como.*me chamo",
                r"voce lembra.*meu nome"
            ],

            # =====================================
            # Aprendizado
            # =====================================

            IntentTypes.LEARN_PREFERENCE: [
                r"\beu gosto de\b",
                r"\beu gosto\b",
                r"\beu prefiro\b",
                r"\bminha preferencia e\b"
            ],

            IntentTypes.LEARN_FACT: [
                r"\beu tenho\b",
                r"\beu moro\b",
                r"\beu faco\b"
            ]
        }

    # =====================================
    # Detectar intenção
    # =====================================

    def detect(self, message):

        if not message:
            return IntentTypes.UNKNOWN

        message = self.normalize(message)

        for intent, patterns in self.patterns.items():

            for pattern in patterns:

                if re.search(pattern, message):
                    return intent

        return IntentTypes.UNKNOWN

    # =====================================
    # Normalização
    # =====================================

    def normalize(self, message):

        message = str(message)

        message = message.lower().strip()

        # Remove acentos
        message = unicodedata.normalize(
            "NFD",
            message
        )

        message = "".join(
            char
            for char in message
            if unicodedata.category(char) != "Mn"
        )

        # Remove pontuação
        message = re.sub(
            r"[!?.,;:]",
            "",
            message
        )

        # Remove espaços duplicados
        message = re.sub(
            r"\s+",
            " ",
            message
        )

        return message.strip()