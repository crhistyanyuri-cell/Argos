class Config:

    def __init__(self):

        self.name = "ARGOS"
        self.version = "0.5"
        self.language = "pt-BR"

        self.debug = True

    # =====================================
    # Obter configuração
    # =====================================

    def get(self, key, default=None):

        return getattr(
            self,
            key,
            default
        )

    # =====================================
    # Alterar configuração
    # =====================================

    def set(self, key, value):

        setattr(
            self,
            key,
            value
        )

    # =====================================
    # Obter todas
    # =====================================

    def get_all(self):

        return {
            "name": self.name,
            "version": self.version,
            "language": self.language,
            "debug": self.debug
        }