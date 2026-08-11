from Memory.Memory import Memory


class MemoryManager:

    def __init__(self, memory):

        self.memory = memory

    # =====================================
    # Métodos genéricos
    # =====================================

    def save(self, key, value):

        self.memory.save(key, value)

    def load(self, key, default=None):

        return self.memory.load(key, default)

    def delete(self, key):

        return self.memory.delete(key)

    def get_all(self):

        return self.memory.get_all()

    # =====================================
    # Usuário
    # =====================================

    def set_user_name(self, name):

        self.save("user_name", name)

    def get_user_name(self):

        return self.load("user_name")

    def delete_user_name(self):

        return self.delete("user_name")

    # =====================================
    # Preferências
    # =====================================

    def set_preference(self, key, value):

        preferences = self.load("preferences", {})

        preferences[key] = value

        self.save("preferences", preferences)

    def get_preference(self, key, default=None):

        preferences = self.load("preferences", {})

        return preferences.get(key, default)

    def get_preferences(self):

        return self.load("preferences", {})

    # =====================================
    # Fatos
    # =====================================

    def add_fact(self, fact):

        facts = self.load("facts", [])

        if fact not in facts:

            facts.append(fact)

            self.save("facts", facts)

    def get_facts(self):

        return self.load("facts", [])

    def remove_fact(self, fact):

        facts = self.load("facts", [])

        if fact in facts:

            facts.remove(fact)

            self.save("facts", facts)

            return True

        return False