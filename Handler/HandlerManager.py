class HandlerManager:

    def __init__(self, handlers):

        self.handlers = handlers

    # =====================================
    # Processamento
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
    # Adicionar Handler
    # =====================================

    def add_handler(self, handler):

        self.handlers.append(handler)

    # =====================================
    # Remover Handler
    # =====================================

    def remove_handler(self, handler):

        if handler in self.handlers:

            self.handlers.remove(handler)

            return True

        return False

    # =====================================
    # Listar Handlers
    # =====================================

    def get_handlers(self):

        return self.handlers.copy()