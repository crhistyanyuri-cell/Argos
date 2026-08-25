
import re


class SemanticAnalyzer:

    def __init__(self):

        # =====================================
        # Conceitos relacionados
        # =====================================

        self.concepts = {

            "game": {
                "jogo",
                "jogos",
                "game",
                "games"
            },

            "animal": {
                "animal",
                "animais",
                "bicho",
                "bichos"
            },

            "film": {
                "filme",
                "filmes"
            },

            "series": {
                "serie",
                "series"
            },

            "music": {
                "musica",
                "musicas",
                "música",
                "músicas",
                "canção",
                "cancao",
                "canções",
                "cancoes"
            },

            "city": {
                "cidade",
                "moro",
                "moradia",
                "morando"
            },

            "name": {
                "nome",
                "chamo"
            },

            "origin": {
                "origem",
                "venho",
                "sou"
            }
        }

        # =====================================
        # Indicadores de pergunta
        # =====================================

        self.question_words = {
            "qual",
            "que",
            "quem",
            "onde",
            "como",
            "quando",
            "porque",
            "por"
        }

        # =====================================
        # Perguntas relacionadas à memória
        #
        # Algumas frases são perguntas mesmo
        # sem possuir uma palavra interrogativa.
        #
        # Exemplos:
        #
        # "você lembra?"
        # "você recorda?"
        # "você sabe?"
        # "você esqueceu?"
        # =====================================

        self.memory_question_words = {
            "lembra",
            "lembrar",
            "lembrou",
            "lembrava",
            "lembre",

            "recorda",
            "recordar",
            "recordou",
            "recordava",
            "recorde",

            "sabe",
            "saber",
            "sabia",

            "esqueceu",
            "esquecer"
        }

        # =====================================
        # Indicadores de memória
        # =====================================

        self.memory_words = {
            "meu",
            "minha",
            "meus",
            "minhas",

            "lembra",
            "lembrar",
            "lembrou",
            "lembrava",
            "lembre",

            "recorda",
            "recordar",
            "recordou",
            "recordava",
            "recorde",

            "sabe",
            "saber",
            "sabia",

            "esqueceu",
            "esquecer",
            "esquecido",
            "esquecida"
        }

        # =====================================
        # Indicadores de referência
        #
        # Usados quando a pessoa fala de algo
        # sem mencionar diretamente o assunto.
        # =====================================

        self.reference_words = {
            "aquele",
            "aquela",
            "aquilo",

            "mesmo",
            "mesma",

            "isso",
            "disso",
            "dessa",
            "desse",

            "ele",
            "ela",
            "dele",
            "dela",

            "qual"
        }

        # =====================================
        # Indicadores de preferência
        # =====================================

        self.preference_words = {
            "gosto",
            "gosta",
            "gostar",

            "favorito",
            "favorita",
            "favoritos",
            "favoritas",

            "prefiro",
            "preferido",
            "preferida"
        }

    # =====================================
    # Analisar mensagem
    # =====================================

    def analyze(self, message):

        if not message:
            return {
                "subject": None,
                "question": False,
                "memory_related": False,
                "context_reference": False
            }

        normalized = message.lower()

        # =================================
        # Remover pontuação
        # =================================

        normalized = re.sub(
            r"[^\w\s]",
            "",
            normalized
        )

        words = normalized.split()

        subject = self.detect_subject(
            words
        )

        memory_related = self.detect_memory_relation(
            words
        )

        question = self.detect_question(
            words,
            memory_related
        )

        context_reference = self.detect_context_reference(
            words,
            question,
            memory_related
        )

        return {
            "subject": subject,
            "question": question,
            "memory_related": memory_related,
            "context_reference": context_reference
        }

    # =====================================
    # Detectar assunto
    # =====================================

    def detect_subject(self, words):

        for subject, concepts in self.concepts.items():

            for word in words:

                if word in concepts:
                    return subject

        return None

    # =====================================
    # Detectar pergunta
    # =====================================

    def detect_question(
        self,
        words,
        memory_related=False
    ):

        # ---------------------------------
        # Perguntas tradicionais
        # ---------------------------------

        for word in words:

            if word in self.question_words:
                return True

        # ---------------------------------
        # Perguntas de memória
        # ---------------------------------

        if memory_related:

            for word in words:

                if word in self.memory_question_words:
                    return True

        return False

    # =====================================
    # Detectar relação com memória
    # =====================================

    def detect_memory_relation(self, words):

        for word in words:

            if word in self.memory_words:
                return True

        return False

    # =====================================
    # Detectar referência contextual
    # =====================================

    def detect_context_reference(
        self,
        words,
        question,
        memory_related
    ):

        # ---------------------------------
        # Precisa ser uma pergunta
        # ---------------------------------

        if not question:
            return False

        # ---------------------------------
        # Referência explícita
        # ---------------------------------

        for word in words:

            if word in self.reference_words:
                return True

        # ---------------------------------
        # Pergunta relacionada à memória
        #
        # Se não existe assunto explícito,
        # significa que a pergunta provavelmente
        # está se referindo ao assunto anterior.
        # ---------------------------------

        if memory_related:

            subject = self.detect_subject(
                words
            )

            if subject is None:
                return True

        # ---------------------------------
        # Perguntas de preferência sem
        # assunto explícito
        # ---------------------------------

        has_preference = False

        for word in words:

            if word in self.preference_words:

                has_preference = True
                break

        if has_preference:

            subject = self.detect_subject(
                words
            )

            if subject is None:
                return True

        return False
