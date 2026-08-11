
class HelpCommand:

    def execute(self, args, manager):

        command_processor = manager.get(
            "command_processor"
        )

        if command_processor is None:

            return "Não foi possível acessar os comandos."

        commands = command_processor.get_commands()

        if not commands:

            return "Nenhum comando está disponível."

        lines = [
            "Comandos disponíveis:"
        ]

        for name in sorted(commands.keys()):

            lines.append(
                f"/{name}"
            )

        return "\n".join(lines)

