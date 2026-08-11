from enum import Enum


class IntentTypes(Enum):

    # =====================================
    # Geral
    # =====================================

    UNKNOWN = "unknown"

    # =====================================
    # Conversação
    # =====================================

    GREETING = "greeting"

    # =====================================
    # Identidade do A.R.G.O.S.
    # =====================================

    ASK_AI_NAME = "ask_ai_name"
    ASK_AI_VERSION = "ask_ai_version"
    ASK_AI_LANGUAGE = "ask_ai_language"

    # =====================================
    # Memória do usuário
    # =====================================

    REMEMBER_USER_NAME = "remember_user_name"
    ASK_USER_NAME = "ask_user_name"

    # =====================================
    # Aprendizado
    # =====================================

    LEARN_FACT = "learn_fact"
    LEARN_PREFERENCE = "learn_preference"