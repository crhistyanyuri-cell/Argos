class Logger:

    def __init__(self, config):

        self.config = config

    def info(self, message):

        print(f"[INFO] {message}")

    def warning(self, message):

        print(f"[WARNING] {message}")

    def error(self, message):

        print(f"[ERROR] {message}")

    def debug(self, message):

        if self.config.debug:

            print(f"[DEBUG] {message}")