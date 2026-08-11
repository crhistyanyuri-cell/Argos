class CommandManager:

    def __init__(self):

        self.commands = {}

    # =====================================
    # Registro
    # =====================================

    def register(self, name, command):

        name = name.lower().strip()

        if not name:
            return

        self.commands[name] = command

    # =====================================
    # Remoção
    # =====================================

    def remove(self, name):

        name = name.lower().strip()

        if name in self.commands:

            del self.commands[name]

            return True

        return False

    # =====================================
    # Execução
    # =====================================

    def execute(self, name, args, manager):

        name = name.lower().strip()

        command = self.commands.get(name)

        if command is None:

            return {
                "success": False,
                "message": (
                    f"Comando desconhecido: /{name}"
                )
            }

        try:

            response = command.execute(
                args,
                manager
            )

            return {
                "success": True,
                "message": response
            }

        except Exception as error:

            logger = manager.get("logger")

            if logger:

                logger.error(
                    f"Erro ao executar "
                    f"/{name}: {error}"
                )

            return {
                "success": False,
                "message": (
                    "Ocorreu um erro ao executar "
                    "esse comando."
                )
            }

    # =====================================
    # Consulta
    # =====================================

    def has(self, name):

        return name.lower().strip() in self.commands

    def get(self, name):

        return self.commands.get(
            name.lower().strip()
        )

    def get_commands(self):

        return self.commands.copy()