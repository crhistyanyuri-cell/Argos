class CommandProcessor:

    def __init__(self):

        self.commands = {}

    # =====================================
    # Registrar comando
    # =====================================

    def register(self, name, command):

        if not name or command is None:

            return False

        name = name.strip().lower()

        if not name:

            return False

        self.commands[name] = command

        return True

    # =====================================
    # Verificar se é comando
    # =====================================

    def is_command(self, message):

        if not message:

            return False

        return message.strip().startswith("/")

    # =====================================
    # Processar
    # =====================================

    def process(self, message, manager):

        # =================================
        # Mensagem vazia
        # =================================

        if not message:

            return None

        message = message.strip()

        if not message:

            return None

        # =================================
        # Mensagem normal
        # =================================

        if not self.is_command(message):

            return {
                "type": "message",
                "content": message
            }

        # =================================
        # Extrair comando
        # =================================

        command_line = message[1:].strip()

        if not command_line:

            return {
                "type": "command",
                "name": None,
                "args": [],
                "found": False
            }

        parts = command_line.split()

        command_name = parts[0].lower()

        args = parts[1:]

        # =================================
        # Procurar comando
        # =================================

        command = self.commands.get(
            command_name
        )

        # =================================
        # Comando desconhecido
        # =================================

        if command is None:

            return {
                "type": "command",
                "name": command_name,
                "args": args,
                "found": False
            }

        # =================================
        # Executar comando
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
    def get_commands(self):
        return self.commands