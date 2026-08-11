class ExitCommand:

    def execute(self, args, manager):

        core = manager.get("core")

        if core is None:

            return "Não foi possível encerrar o sistema."

        core.stop()

        return "Sistema encerrado."