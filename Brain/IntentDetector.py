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
                r"qual.*\bseu nome",
                r"como.*\bchama",
                r"quem.*\be voce"
            ],

            IntentTypes.ASK_AI_VERSION: [
                r"qual.*\bversao",
                r"que versao"
            ],

            IntentTypes.ASK_AI_LANGUAGE: [
                r"qual.*\bidioma",
                r"qual.*\blingua",
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
                r"qual.*\bmeu nome",
                r"como.*\bme chamo",
                r"voce lembra.*\bmeu nome"
            ],

            IntentTypes.ASK_USER_CITY: [
                r"onde.*\bmoro",
                r"onde.*\beu moro",
                r"qual.*\bminha cidade",
                r"em que cidade.*\bmoro",
                r"em que cidade.*\beu moro",
                r"voce lembra.*\bonde.*\bmoro"
            ],

            # =====================================
            # Consulta de fatos
            # =====================================

            IntentTypes.ASK_USER_FACT: [
                r"de onde.*\bsou",
                r"de onde.*\beu sou",
                r"de onde.*\bvenho",
                r"qual.*\bminha origem",
                r"voce lembra.*\bde onde.*\bsou"
            ],

            # =====================================
            # Consulta de preferências
            # =====================================

            IntentTypes.ASK_USER_PREFERENCE: [
                r"qual.*\bmeu.*\bfavorito",
                r"qual.*\bmeu.*\bfavorita",
                r"qual.*\bminha.*\bpreferencia",
                r"voce lembra.*\bmeu.*\bfavorito",
                r"voce lembra.*\bminha.*\bpreferencia"
            ],

            # =====================================
            # Aprendizado
            # =====================================

            IntentTypes.LEARN_PREFERENCE: [
                r"eu gosto de",
                r"eu gosto",
                r"eu prefiro",
                r"minha preferencia e",
                r"meu *.*\b favorito e",
                r"minha *.*\b favorita e"
            ],

            IntentTypes.LEARN_FACT: [
                r"eu sou",
                r"eu tenho",
                r"eu moro",
                r"eu faco"
            ]
        }

    def detect(self, message):

        if not message:
            return IntentTypes.UNKNOWN

        message = self.normalize(message)

        for intent, patterns in self.patterns.items():

            for pattern in patterns:

                if re.search(pattern, message):
                    return intent

        return IntentTypes.UNKNOWN

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