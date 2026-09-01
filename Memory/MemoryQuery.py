
class MemoryQuery:

    def __init__(self, memory_manager):

        self.memory_manager = memory_manager

        # =====================================
        # Palavras que normalmente não ajudam
        # na identificação de uma informação
        # =====================================

        self.stop_words = {

            "o",
            "a",
            "os",
            "as",
            "um",
            "uma",
            "uns",
            "umas",

            "eu",
            "meu",
            "minha",
            "meus",
            "minhas",

            "você",
            "voce",
            "seu",
            "sua",
            "seus",
            "suas",

            "de",
            "do",
            "da",
            "dos",
            "das",

            "em",
            "no",
            "na",
            "nos",
            "nas",

            "é",
            "e",
            "que",
            "qual",
            "quais",
            "onde",
            "como",
            "quem",
            "quando",
            "por",
            "para",
            "sobre",
            "sou"
        }

        self.preference_map = {

            "game": "jogo_favorito",
            "animal": "animal_favorito",
            "film": "filme_favorito",
            "series": "serie_favorita",
            "music": "musica_favorita",
            "preference": "general"
        }

    # =====================================
    # Consulta principal
    # =====================================

    def query(
        self,
        message,
        subject=None
    ):

        if message:

            normalized = self.normalize(
                message
            )

        else:

            normalized = ""

        # =================================
        # Consulta por assunto
        # =================================

        if subject == "game":

            return self.query_preference_by_key(
                "jogo_favorito"
            )

        if subject == "animal":

            return self.query_preference_by_key(
                "animal_favorito"
            )

        if subject == "film":

            return self.query_preference_by_key(
                "filme_favorito"
            )

        if subject == "series":

            return self.query_preference_by_key(
                "serie_favorita"
            )

        if subject == "music":

            return self.query_preference_by_key(
                "musica_favorita"
            )

        if subject == "preference":

            return self.query_preference_by_key(
                "general"
            )

        if subject == "origin":

            return self.query_origin()

        # =================================
        # Cidade
        # =================================

        if subject == "city":

            return self.query_city()

        # =================================
        # Nome
        # =================================

        if self.is_name_query(
            normalized
        ):

            name = self.memory_manager.get_user_name()

            if name:

                return {
                    "type": "name",
                    "value": name
                }

        # =================================
        # Cidade
        # =================================

        if self.is_city_query(
            normalized
        ):

            city = self.memory_manager.load(
                "city"
            )

            if city:

                return {
                    "type": "city",
                    "value": city
                }

        # =================================
        # Preferências
        # =================================

        preference = self.query_preference(
            normalized
        )

        if preference:

            return preference

        # =================================
        # Fatos
        # =================================

        fact = self.query_fact(
            normalized
        )

        if fact:

            return fact

        return None

    # =====================================
    # Consultar preferência por chave
    # =====================================

    def query_preference_by_key(
        self,
        key
    ):

        preferences = (
            self.memory_manager.get_preferences()
        )

        if not preferences:

            return None

        value = preferences.get(
            key
        )

        if value is None:

            return None

        return {
            "type": "preference",
            "key": key,
            "value": value
        }

    # =====================================
    # Consultar cidade
    # =====================================

    def query_city(self):

        city = self.memory_manager.load(
            "city"
        )

        if not city:

            return None

        return {
            "type": "city",
            "value": city
        }

    # =====================================
    # Consultar origem
    # =====================================

    def query_origin(self):

        facts = self.memory_manager.get_facts()

        if not facts:

            return None

        for fact in facts:

            fact_lower = fact.lower()

            if fact_lower.startswith(
                "eu sou de "
            ):

                return {
                    "type": "fact",
                    "value": fact
                }

        return None

    # =====================================
    # Consultar nome
    # =====================================

    def is_name_query(
        self,
        message
    ):

        patterns = [

            "qual meu nome",
            "qual o meu nome",
            "como me chamo",
            "como eu me chamo",
            "voce lembra meu nome",
            "voce sabe meu nome",
            "voce sabe o meu nome"
        ]

        for pattern in patterns:

            if pattern in message:

                return True

        return False

    # =====================================
    # Consultar cidade
    # =====================================

    def is_city_query(
        self,
        message
    ):

        patterns = [

            "onde moro",
            "onde eu moro",
            "qual minha cidade",
            "qual a minha cidade",
            "em que cidade moro",
            "em que cidade eu moro",
            "voce lembra onde moro",
            "voce sabe onde moro"
        ]

        for pattern in patterns:

            if pattern in message:

                return True

        return False

    # =====================================
    # Consultar preferência
    # =====================================

    def query_preference(
        self,
        message
    ):

        preferences = (
            self.memory_manager.get_preferences()
        )

        if not preferences:

            return None

        # =================================
        # Procurar diretamente pelo tipo
        # =================================

        preference_map = {

            "jogo": [
                "jogo_favorito",
                "jogo_preferido"
            ],

            "animal": [
                "animal_favorito",
                "animal_preferido"
            ],

            "filme": [
                "filme_favorito",
                "filme_preferido"
            ],

            "serie": [
                "serie_favorita",
                "serie_preferida"
            ],

            "série": [
                "serie_favorita",
                "serie_preferida"
            ],

            "musica": [
                "musica_favorita",
                "musica_preferida"
            ],

            "música": [
                "musica_favorita",
                "musica_preferida"
            ]
        }

        for word, keys in preference_map.items():

            if word not in message:

                continue

            for key in keys:

                if key in preferences:

                    return {
                        "type": "preference",
                        "key": key,
                        "value": preferences[key]
                    }

        # =================================
        # Preferência genérica
        # =================================

        if (
            "preferencia" in message
            or "preferência" in message
        ):

            value = preferences.get(
                "general"
            )

            if value is not None:

                return {
                    "type": "preference",
                    "key": "general",
                    "value": value
                }

        return None

    # =====================================
    # Consultar fatos
    # =====================================

    def query_fact(
        self,
        message
    ):

        facts = self.memory_manager.get_facts()

        if not facts:

            return None

        # =================================
        # Pergunta genérica:
        #
        # "o que eu tenho?"
        #
        # Nesse caso, procurar primeiro
        # o fato "eu tenho ..." mais recente.
        # =================================

        if (
            "tenho" in message
            and "o que" in message
        ):

            for fact in reversed(facts):

                fact_lower = fact.lower()

                if fact_lower.startswith(
                    "eu tenho "
                ):

                    return {
                        "type": "fact",
                        "value": fact
                    }

        # =================================
        # Consulta normal por palavras-chave
        # =================================

        query_words = self.extract_keywords(
            message
        )

        if not query_words:

            return None

        best_fact = None
        best_score = 0

        for fact in facts:

            fact_words = self.extract_keywords(
                fact
            )

            score = len(
                query_words.intersection(
                    fact_words
                )
            )

            if score > best_score:

                best_score = score
                best_fact = fact

        if best_fact is None:

            return None

        # =================================
        # Exigir pelo menos uma palavra
        # significativa em comum
        # =================================

        if best_score < 1:

            return None

        return {
            "type": "fact",
            "value": best_fact
        }

    # =====================================
    # Extrair palavras importantes
    # =====================================

    def extract_keywords(
        self,
        message
    ):

        words = message.split()

        keywords = set()

        for word in words:

            word = word.strip(
                " .,!?:;"
            )

            if not word:

                continue

            if word in self.stop_words:

                continue

            keywords.add(
                word
            )

        return keywords

    # =====================================
    # Normalização
    # =====================================

    def normalize(
        self,
        message
    ):

        message = str(
            message
        )

        message = message.lower().strip()

        replacements = {

            "á": "a",
            "à": "a",
            "ã": "a",
            "â": "a",

            "é": "e",
            "ê": "e",

            "í": "i",

            "ó": "o",
            "ô": "o",
            "õ": "o",

            "ú": "u",

            "ç": "c"
        }

        for old, new in replacements.items():

            message = message.replace(
                old,
                new
            )

        for character in [

            "?",
            "!",
            ".",
            ",",
            ";",
            ":"
        ]:

            message = message.replace(
                character,
                ""
            )

        message = " ".join(
            message.split()
        )

        return message.strip()
