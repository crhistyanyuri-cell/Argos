from Brain.IntentTypes import IntentTypes


class QuestionHandler:

    def process(self, context, manager):

        intent = context.get("intent")

        if intent != IntentTypes.UNKNOWN:

            return None

        message = context.get("message")

        if not message:

            return None

        return self.answer(message)

    # =====================================
    # Perguntas
    # =====================================

    def answer(self, message):

        if "o que é uma estrela" in message:

            return (
                "Uma estrela é um corpo celeste que produz "
                "sua própria energia através de reações de "
                "fusão nuclear em seu núcleo."
            )

        if "o que é python" in message:

            return (
                "Python é uma linguagem de programação de "
                "alto nível, conhecida por sua sintaxe simples "
                "e por ser utilizada em diversas áreas."
            )

        return "Ainda estou aprendendo a responder esse tipo de pergunta."