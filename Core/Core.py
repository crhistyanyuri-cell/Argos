class Core:

    def __init__(self, manager):

        self.manager = manager
        self.running = False

    # =====================================
    # Inicialização
    # =====================================

    def start(self):

        if self.running:

            return

        self.running = True

        config = self.manager.get("config")
        logger = self.manager.get("logger")

        if logger:

            if config:

                logger.info(
                    f"{config.name} "
                    f"v{config.version} iniciado."
                )

            else:

                logger.info(
                    "Sistema iniciado."
                )

        self.manager.start_all()

    # =====================================
    # Execução
    # =====================================

    def run(self):

        if not self.running:

            self.start()

        input_manager = self.manager.get(
            "input_manager"
        )

        if input_manager is None:

            return

        while self.running:

            message = input_manager.get_input()

            if message is None:

                break

            message = message.strip()

            if not message:

                continue

            if message.lower() in (
                "/sair",
                "/exit",
                "/quit"
            ):

                break

            self.process(message)

        self.stop()

    # =====================================
    # Processamento
    # =====================================

    def process(self, message):

        command_processor = self.manager.get(
            "command_processor"
        )

        brain = self.manager.get("brain")

        if command_processor is None:

            return

        result = command_processor.process(
            message,
            self.manager
        )

        if result is None:

            return

        if isinstance(result, dict):

            result_type = result.get("type")

            if result_type == "command":

                return result

            if result_type == "message":

                if brain is not None:

                    response = brain.think(
                        message,
                        self.manager
                    )

                    if response:

                        print(response)

                    return response

        return result

    # =====================================
    # Encerramento
    # =====================================

    def stop(self):

        if not self.running:

            return

        self.running = False

        self.manager.stop_all()

        logger = self.manager.get("logger")

        if logger:

            logger.info(
                "Sistema encerrado."
            )

    # =====================================
    # Estado
    # =====================================

    def is_running(self):

        return self.running