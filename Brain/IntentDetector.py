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
                r"\bolá\b",
                r"\bola\b",
                r"\be ai\b",
                r"\beai\b",
                r"\bbom dia\b",
                r"\bboa tarde\b",
                r"\bboa noite\b"
            ],

            # =====================================
            # Identidade da A.R.G.O.S.
            # =====================================

            IntentTypes.ASK_AI_NAME: [
                r"\bseu nome\b",
                r"qual.*seu nome",
                r"como.*chama",
                r"quem.*e voce"
            ],

            IntentTypes.ASK_AI_VERSION: [
                r"qual.*versao",
                r"que versao"
            ],

            IntentTypes.ASK_AI_LANGUAGE: [
                r"qual.*idioma",
                r"qual.*lingua",
                r"que idioma"
            ],

            # =====================================
            # Memória
            # =====================================

            IntentTypes.REMEMBER_USER_NAME: [
                r"meu nome e",
                r"me chamo",
                r"pode me chamar de"
            ],

            IntentTypes.ASK_USER_NAME: [
                r"\bmeu nome\b",
                r"qual.*meu nome",
                r"como.*me chamo",
                r"voce lembra.*meu nome"
            ],

            IntentTypes.ASK_USER_CITY: [
                r"onde.*moro",
                r"onde.*eu moro",
                r"qual.*minha cidade",
                r"em que cidade.*moro",
                r"em que cidade.*eu moro",
                r"voce lembra.*onde.*moro"
            ],

            # =====================================
            # Consulta de fatos
            # =====================================

            IntentTypes.ASK_USER_FACT: [
                r"de onde.*sou",
                r"de onde.*eu sou",
                r"de onde.*venho",
                r"qual.*minha origem",
                r"voce lembra.*de onde.*sou"
            ],

            # =====================================
            # Consulta de preferências
            # =====================================

            IntentTypes.ASK_USER_PREFERENCE: [
                r"qual.*meu.*favorito",
                r"qual.*meu.*favorita",
                r"qual.*minha.*preferencia",
                r"voce lembra.*meu.*favorito",
                r"voce lembra.*minha.*preferencia"
],

            # =====================================
            # Aprendizado
            # =====================================

            IntentTypes.LEARN_PREFERENCE: [
                r"eu gosto de",
                r"eu gosto",
                r"eu prefiro",
                r"minha preferencia e",
                r"meu .* favorito e",
                r"minha .* favorita e"
            ],

            IntentTypes.LEARN_FACT: [
                r"eu sou",
                r"eu tenho",
                r"eu moro",
                r"eu faco"
            ]
        }

    # =====================================
    # Detectar intenção
    # =====================================

    def detect(self, message):

        if not message:

            return IntentTypes.UNKNOWN

        message = self.normalize(
            message
        )

        for intent, patterns in self.patterns.items():

            for pattern in patterns:

                if re.search(
                    pattern,
                    message
                ):

                    return intent

        return IntentTypes.UNKNOWN

    # =====================================
    # Normalização
    # =====================================

    def normalize(self, message):

        message = str(
            message
        )

        message = message.lower().strip()

        # =================================
        # Remover acentos
        # =================================

        message = unicodedata.normalize(
            "NFD",
            message
        )

        message = "".join(
            char
            for char in message
            if unicodedata.category(char) != "Mn"
        )

        # =================================
        # Remover pontuação
        # =================================

        message = re.sub(
            r"[!?.,;:]",
            "",
            message
        )

        # =================================
        # Normalizar espaços
        # =================================

        message = re.sub(
            r"\s+",
            " ",
            message
        )

        return message.strip()