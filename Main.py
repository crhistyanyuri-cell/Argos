from Core.Bootstrap import Bootstrap

from Core.Core import Core


def main():

    # =====================================
    # Construção do sistema
    # =====================================

    bootstrap = Bootstrap()

    manager = bootstrap.build()

    # =====================================
    # Inicialização do Core
    # =====================================

    core = Core(manager)

    manager.register(
        "core",
        core
    )

    # =====================================
    # Execução
    # =====================================

    core.start()
    core.run()


if __name__ == "__main__":

    main()