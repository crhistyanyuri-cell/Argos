import json


class MemoryCommand:

    def execute(self, args, manager):

        memory_manager = manager.get(
            "memory_manager"
        )

        if memory_manager is None:

            return "Não foi possível acessar a memória."

        memory = memory_manager.get_all()

        if not memory:

            return "A memória está vazia."

        return json.dumps(
            memory,
            ensure_ascii=False,
            indent=4
        )