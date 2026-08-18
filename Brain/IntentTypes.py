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
    # Identidade da A.R.G.O.S.
    # =====================================

    ASK_AI_NAME = "ask_ai_name"
    ASK_AI_VERSION = "ask_ai_version"
    ASK_AI_LANGUAGE = "ask_ai_language"

    # =====================================
    # Memória do usuário
    # =====================================

    REMEMBER_USER_NAME = "remember_user_name"
    ASK_USER_NAME = "ask_user_name"
    ASK_USER_PREFERENCE = "ask_user_preference"
    ASK_USER_CITY = "ask_user_city"
    ASK_USER_FACT = "ask_user_fact"

    # =====================================
    # Aprendizado
    # =====================================

    LEARN_FACT = "learn_fact"
    LEARN_PREFERENCE = "learn_preference"