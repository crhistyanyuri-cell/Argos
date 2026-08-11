import json
from pathlib import Path


class Memory:

    def __init__(self, file_path=None):

        if file_path is None:

            base_path = Path(__file__).resolve().parent.parent

            file_path = (
                base_path
                / "Data"
                / "memory.json"
            )

        self.file_path = Path(file_path)

        self.data = {}

        self.create_folder()
        self.load_memory()

    # =====================================
    # Preparação
    # =====================================

    def create_folder(self):

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    # =====================================
    # Carregar memória
    # =====================================

    def load_memory(self):

        if not self.file_path.exists():

            self.data = {}

            self.save_memory()

            return

        try:

            with self.file_path.open(
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                if isinstance(data, dict):

                    self.data = data

                else:

                    self.data = {}

        except (
            json.JSONDecodeError,
            OSError
        ):

            self.data = {}

    # =====================================
    # Salvar memória
    # =====================================

    def save_memory(self):

        try:

            with self.file_path.open(
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    self.data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except OSError:

            return False

    # =====================================
    # Salvar dado
    # =====================================

    def save(self, key, value):

        self.data[key] = value

        return self.save_memory()

    # =====================================
    # Carregar dado
    # =====================================

    def load(self, key, default=None):

        return self.data.get(
            key,
            default
        )

    # =====================================
    # Remover dado
    # =====================================

    def delete(self, key):

        if key not in self.data:

            return False

        del self.data[key]

        return self.save_memory()

    # =====================================
    # Obter tudo
    # =====================================

    def get_all(self):

        return self.data.copy()

    # =====================================
    # Limpar memória
    # =====================================

    def clear(self):

        self.data = {}

        return self.save_memory()