from Brain.IntentTypes import IntentTypes


class GreetingHandler:

    def process(self, context, manager):

        intent = context.get("intent")

        if intent != IntentTypes.GREETING:

            return None

        return self.greet()

    def greet(self):

        return "Olá! Como posso ajudar?"