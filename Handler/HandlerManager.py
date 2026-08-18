class HandlerManager:

    def __init__(self, handlers=None):

        self.handlers = handlers or []

    # =====================================
    # Registrar Handler
    # =====================================

    def register(self, handler):

        if handler not in self.handlers:

            self.handlers.append(
                handler
            )

    # =====================================
    # Processar
    # =====================================

    def process(self, context, manager):

        for handler in self.handlers:

            response = handler.process(
                context,
                manager
            )

            if response is not None:

                return response

        return None

    # =====================================
    # Listar Handlers
    # =====================================

    def get_handlers(self):

        return self.handlers