import re

from Brain.IntentTypes import IntentTypes


class IntentDetector:

    def __init__(self):

        self.patterns = {

            # =====================================
            # Conversação
            # =====================================

            IntentTypes.GREETING: [
                r"\boi\b",
                r"\bolá\b",
                r"\be ai\b",
                r"\beai\b",
                r"\bbom dia\b",
                r"\bboa tarde\b",
                r"\bboa noite\b"
            ],

            # =====================================
            # Identidade da A.R.G.
            # =====================================

            IntentTypes.ASK_AI_NAME: [
                r"qual.*seu nome",
                r"como.*chama",
                r"quem.*é você",
                r"quem.*e voce"
            ],

            IntentTypes.ASK_AI_VERSION: [
                r"qual.*versão",
                r"qual.*versao",
                r"que versão",
                r"que versao"
            ],

            IntentTypes.ASK_AI_LANGUAGE: [
                r"qual.*idioma",
                r"qual.*língua",
                r"qual.*lingua",
                r"que idioma"
            ],

            # =====================================
            # Memória
            # =====================================

            IntentTypes.REMEMBER_USER_NAME: [
                r"meu nome é",
                r"meu nome e",
                r"me chamo",
                r"pode me chamar de"
            ],

            IntentTypes.ASK_USER_NAME: [
                r"qual.*meu nome",
                r"como.*me chamo",
                r"você lembra.*meu nome",
                r"voce lembra.*meu nome"
            ],

            # =====================================
            # Aprendizado
            # =====================================

            IntentTypes.LEARN_PREFERENCE: [
                r"eu gosto de",
                r"eu gosto",
                r"eu prefiro",
                r"minha preferência é",
                r"minha preferencia e"
            ],

            IntentTypes.LEARN_FACT: [
                r"eu sou",
                r"eu tenho",
                r"eu moro",
                r"eu faço",
                r"eu faco"
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

        message = message.lower().strip()

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

        return message