class InputManager:

    def __init__(self, prompt="> "):

        self.prompt = prompt

    # =====================================
    # Entrada
    # =====================================

    def get_input(self):

        try:

            return input(self.prompt)

        except EOFError:

            return None

        except KeyboardInterrupt:

            print()

            return None

    # =====================================
    # Alterar prompt
    # =====================================

    def set_prompt(self, prompt):

        self.prompt = prompt

    # =====================================
    # Obter prompt
    # =====================================

    def get_prompt(self):

        return self.prompt