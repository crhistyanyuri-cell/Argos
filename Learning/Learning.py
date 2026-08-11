class Learning:

    def __init__(self, memory_manager):

        self.memory_manager = memory_manager

    # =====================================
    # Aprender um fato
    # =====================================

    def learn_fact(self, fact):

        if not fact:

            return False

        fact = fact.strip()

        if not fact:

            return False

        self.memory_manager.add_fact(fact)

        return True

    # =====================================
    # Aprender uma preferência
    # =====================================

    def learn_preference(self, key, value):

        if not key or not value:

            return False

        key = key.strip()
        value = value.strip()

        if not key or not value:

            return False

        self.memory_manager.set_preference(
            key,
            value
        )

        return True

    # =====================================
    # Aprender nome
    # =====================================

    def learn_name(self, name):

        if not name:

            return False

        name = name.strip()

        if not name:

            return False

        self.memory_manager.set_user_name(name)

        return True

    # =====================================
    # Aprender idade
    # =====================================

    def learn_age(self, age):

        if age is None:

            return False

        self.memory_manager.save(
            "age",
            age
        )

        return True

    # =====================================
    # Aprender cidade
    # =====================================

    def learn_city(self, city):

        if not city:

            return False

        city = city.strip()

        if not city:

            return False

        self.memory_manager.save(
            "city",
            city
        )

        return True