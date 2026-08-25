import re

from Brain.IntentDetector import IntentDetector
from Brain.IntentTypes import IntentTypes
from Brain.SemanticAnalyzer import SemanticAnalyzer


class MessageAnalyzer:

    def __init__(self):

        self.intent_detector = IntentDetector()
        self.semantic_analyzer = SemanticAnalyzer()

        # =====================================
        # Padrões de assuntos
        # =====================================

        self.subject_patterns = {

            "name": [
                r"\bmeu nome\b",
                r"\bqual meu nome\b",
                r"\bqual o meu nome\b",
                r"\bcomo me chamo\b",
                r"\bque nome eu tenho\b",
                r"\bvoce sabe meu nome\b",
                r"\bvoce sabe o meu nome\b"
            ],

            "city": [
                r"\bonde moro\b",
                r"\bonde eu moro\b",
                r"\bminha cidade\b",
                r"\bqual minha cidade\b",
                r"\bqual a minha cidade\b",
                r"\bem que cidade moro\b",
                r"\bem que cidade eu moro\b",
                r"\bvoce sabe onde moro\b"
            ],

            "origin": [
                r"\bde onde (eu )?sou\b",
                r"\bde onde (eu )?venho\b",
                r"\bqual (e )?(a )?minha origem\b",
                r"\bvoce sabe de onde (eu )?sou\b",
                r"\bvoce lembra de onde (eu )?sou\b"
            ],

            "game": [
                r"\bmeu jogo\b",
                r"\bqual meu jogo\b",
                r"\bqual o meu jogo\b",
                r"\bjogo favorito\b",
                r"\bjogo preferido\b",
                r"\bque jogo\b",
                r"\bqual jogo\b",
                r"\bvoce lembra qual jogo\b",
                r"\bvoce sabe qual jogo\b"
            ],

            "animal": [
                r"\bmeu animal\b",
                r"\bqual meu animal\b",
                r"\bqual o meu animal\b",
                r"\banimal favorito\b",
                r"\banimal preferido\b",
                r"\bque animal\b",
                r"\bqual animal\b",
                r"\bvoce lembra qual animal\b",
                r"\bvoce sabe qual animal\b"
            ],

            "film": [
                r"\bmeu filme\b",
                r"\bqual meu filme\b",
                r"\bqual o meu filme\b",
                r"\bfilme favorito\b",
                r"\bfilme preferido\b",
                r"\bque filme\b",
                r"\bqual filme\b",
                r"\bvoce lembra qual filme\b",
                r"\bvoce sabe qual filme\b"
            ],

            "series": [
                r"\bminha serie\b",
                r"\bqual minha serie\b",
                r"\bqual a minha serie\b",
                r"\bserie favorita\b",
                r"\bserie preferida\b",
                r"\bque serie\b",
                r"\bqual serie\b"
            ],

            "music": [
                r"\bminha musica\b",
                r"\bqual minha musica\b",
                r"\bqual a minha musica\b",
                r"\bmusica favorita\b",
                r"\bmusica preferida\b",
                r"\bque musica\b",
                r"\bqual musica\b"
            ],

            "preference": [
                r"\bminha preferencia\b",
                r"\bqual minha preferencia\b",
                r"\bqual a minha preferencia\b",
                r"\bvoce lembra minha preferencia\b",
                r"\bvoce lembra a minha preferencia\b",
                r"\bvoce sabe minha preferencia\b",
                r"\bvoce sabe a minha preferencia\b"
            ]
        }

        # =====================================
        # Palavras interrogativas
        # =====================================

        self.question_words = {
            "qual",
            "que",
            "como",
            "onde",
            "quem",
            "quando",
            "porque",
            "por que"
        }

        # =====================================
        # Perguntas curtas por assunto
        #
        # Permite frases como:
        #
        # "e o filme?"
        # "e o jogo?"
        # "e o animal?"
        #
        # =====================================

        self.short_question_subjects = {

            "game": [
                "e o jogo",
                "e jogo",
                "jogo"
            ],

            "animal": [
                "e o animal",
                "e animal",
                "animal"
            ],

            "film": [
                "e o filme",
                "e filme",
                "filme"
            ],

            "series": [
                "e a serie",
                "e serie",
                "serie"
            ],

            "music": [
                "e a musica",
                "e musica",
                "musica"
            ]
        }

    # =====================================
    # Analisar mensagem
    # =====================================

    def analyze(self, message):

        if not message:
            return {
                "intent": IntentTypes.UNKNOWN,
                "subject": None
            }

        normalized = self.normalize(
            message
        )

        # =================================
        # Detectar intenção
        # =================================

        intent = self.intent_detector.detect(
            normalized
        )

        # =================================
        # Detectar assunto por padrões
        # =================================

        subject = self.detect_subject(
            normalized
        )

        # =================================
        # Análise semântica
        # =================================

        semantic = self.semantic_analyzer.analyze(
            normalized
        )

        # =================================
        # Usar análise semântica como
        # alternativa
        # =================================

        if subject is None:
            subject = semantic["subject"]

        # =================================
        # Detectar pergunta
        # =================================

        question = self.is_question(
            normalized
        )

        # =================================
        # Pergunta curta por assunto
        #
        # Exemplo:
        #
        # "e o filme?"
        #
        # Não possui palavra interrogativa,
        # mas semanticamente é uma consulta.
        # =================================

        if not question:
            question = self.is_short_subject_question(
                normalized,
                subject
            )

        # =================================
        # Corrigir perguntas
        # =================================

        if question:

            if subject in (
                "game",
                "animal",
                "film",
                "series",
                "music",
                "preference"
            ):
                intent = IntentTypes.ASK_USER_PREFERENCE

            elif subject == "origin":
                intent = IntentTypes.ASK_USER_FACT

            elif subject == "city":
                intent = IntentTypes.ASK_USER_CITY

            elif subject == "name":
                intent = IntentTypes.ASK_USER_NAME

        return {
            "intent": intent,
            "subject": subject
        }

    # =====================================
    # Detectar assunto
    # =====================================

    def detect_subject(self, message):

        for subject, patterns in self.subject_patterns.items():

            for pattern in patterns:

                if re.search(
                    pattern,
                    message
                ):
                    return subject

        return None

    # =====================================
    # Detectar pergunta
    # =====================================

    def is_question(self, message):

        normalized = self.normalize(
            message
        )

        words = normalized.split()

        for word in self.question_words:

            if word in words:
                return True

        return False

    # =====================================
    # Detectar pergunta curta por assunto
    # =====================================

    def is_short_subject_question(
        self,
        message,
        subject
    ):

        if subject is None:
            return False

        patterns = self.short_question_subjects.get(
            subject,
            []
        )

        for pattern in patterns:

            if message == pattern:
                return True

        return False

    # =====================================
    # Normalização
    # =====================================

    def normalize(self, message):

        return self.intent_detector.normalize(
            message
        )