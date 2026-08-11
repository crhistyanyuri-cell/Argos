class CommandProcessor:

    def __init__(self):

        self.commands = {}

    # =====================================
    # Registro de comandos
    # =====================================

    def register(self, name, command):

        name = name.lower().strip()

        if not name:
            return

        self.commands[name] = command

    # =====================================
    # Remoção de comandos
    # =====================================

    def remove(self, name):

        name = name.lower().strip()

        if name in self.commands:

            del self.commands[name]

            return True

        return False

    # =====================================
    # Verificação
    # =====================================

    def is_command(self, message):

        if not message:
            return False

        return message.strip().startswith("/")

    # =====================================
    # Processamento
    # =====================================

    def process(self, message, manager):

        if not message:

            return None

        message = message.strip()

        # =================================
        # Não é comando
        # =================================

        if not self.is_command(message):

            return {
                "type": "message",
                "content": message
            }

        # =================================
        # Extrai comando
        # =================================

        command_line = message[1:].strip()

        if not command_line:

            return {
                "type": "command",
                "name": None,
                "args": []
            }

        parts = command_line.split()

        command_name = parts[0].lower()

        args = parts[1:]

        # =================================
        # Procura comando
        # =================================

        command = self.commands.get(command_name)

        if command is None:

            return {
                "type": "command",
                "name": command_name,
                "args": args,
                "found": False
            }

        # =================================
        # Executa comando
        # =================================

        response = command.execute(
            args,
            manager
        )

        return {
            "type": "command",
            "name": command_name,
            "args": args,
            "found": True,
            "response": response
        }

    # =====================================
    # Lista de comandos
    # =====================================

    def get_commands(self):

        return self.commands.copy()