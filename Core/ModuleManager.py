class ModuleManager:

    def __init__(self):

        self.modules = {}

    # =====================================
    # Registro
    # =====================================

    def register(self, name, module):

        self.modules[name] = module

    # =====================================
    # Recuperação
    # =====================================

    def get(self, name):

        return self.modules.get(name)

    # =====================================
    # Verificação
    # =====================================

    def has(self, name):

        return name in self.modules

    # =====================================
    # Remoção
    # =====================================

    def remove(self, name):

        if name in self.modules:

            del self.modules[name]

            return True

        return False

    # =====================================
    # Lista de módulos
    # =====================================

    def get_all(self):

        return self.modules.copy()

    # =====================================
    # Inicialização
    # =====================================

    def start_all(self):

        for name, module in self.modules.items():

            if hasattr(module, "start"):

                module.start()

    # =====================================
    # Encerramento
    # =====================================

    def stop_all(self):

        for name, module in reversed(list(self.modules.items())):

            if hasattr(module, "stop"):

                module.stop()