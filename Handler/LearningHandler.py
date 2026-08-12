from Brain.IntentTypes import IntentTypes


class LearningHandler:

    def process(self, context, manager):

        intent = context.get("intent")

        if intent not in (
            IntentTypes.LEARN_FACT,
            IntentTypes.LEARN_PREFERENCE
        ):

            return None

        learning_manager = manager.get(
            "learning_manager"
        )

        if learning_manager is None:

            return "Não consegui acessar meu sistema de aprendizado."

        success = learning_manager.process(
            context
        )

        if not success:

            return "Não consegui aprender essa informação."

        if intent == IntentTypes.LEARN_PREFERENCE:

            return "Entendi. Vou guardar essa preferência."

        if intent == IntentTypes.LEARN_FACT:

            return "Entendi. Vou guardar essa informação."

        return None