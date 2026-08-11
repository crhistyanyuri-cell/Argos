class HelpCommand:

    def execute(self, args, manager):

        command_manager = manager.get(
            "command_manager"
        )

        if command_manager is None:

            return "Não foi possível acessar os comandos."

        commands = command_manager.get_commands()

        if not commands:

            return "Nenhum comando está disponível."

        lines = [
            "Comandos disponíveis:"
        ]

        for name in sorted(commands.keys()):

            lines.append(f"/{name}")

        return "\n".join(lines)