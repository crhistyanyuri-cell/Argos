from Core.ModuleManager import ModuleManager

from Config.Config import Config
from Logger.Logger import Logger

from Memory.Memory import Memory
from Memory.MemoryManager import MemoryManager

from Context.ContextManager import ContextManager

from Learning.Learning import Learning
from Learning.LearningManager import LearningManager

from Handler.HandlerManager import HandlerManager
from Handler.GreetingHandler import GreetingHandler
from Handler.IdentityHandler import IdentityHandler
from Handler.MemoryHandler import MemoryHandler
from Handler.QuestionHandler import QuestionHandler

from Input.InputManager import InputManager

from Commands.CommandProcessor import CommandProcessor
from Commands.HelpCommand import HelpCommand
from Commands.MemoryCommand import MemoryCommand
from Commands.ExitCommand import ExitCommand

from Brain.Brain import Brain


class Bootstrap:

    def __init__(self):

        self.manager = ModuleManager()

    # =====================================
    # Construção do sistema
    # =====================================

    def build(self):

        self.register_core_modules()
        self.register_memory_modules()
        self.register_context_modules()
        self.register_learning_modules()
        self.register_handler_modules()
        self.register_input_modules()
        self.register_command_modules()
        self.register_brain_modules()

        return self.manager

    # =====================================
    # Core
    # =====================================

    def register_core_modules(self):

        config = Config()

        logger = Logger(config)

        self.manager.register(
            "config",
            config
        )

        self.manager.register(
            "logger",
            logger
        )

    # =====================================
    # Memória
    # =====================================

    def register_memory_modules(self):

        memory = Memory()

        memory_manager = MemoryManager(
            memory
        )

        self.manager.register(
            "memory",
            memory
        )

        self.manager.register(
            "memory_manager",
            memory_manager
        )

    # =====================================
    # Contexto
    # =====================================

    def register_context_modules(self):

        context_manager = ContextManager()

        self.manager.register(
            "context_manager",
            context_manager
        )

    # =====================================
    # Learning
    # =====================================

    def register_learning_modules(self):

        memory_manager = self.manager.get(
            "memory_manager"
        )

        learning = Learning(
            memory_manager
        )

        learning_manager = LearningManager(
            learning
        )

        self.manager.register(
            "learning",
            learning
        )

        self.manager.register(
            "learning_manager",
            learning_manager
        )

    # =====================================
    # Handlers
    # =====================================

    def register_handler_modules(self):

        handlers = [
            GreetingHandler(),
            IdentityHandler(),
            MemoryHandler(),
            QuestionHandler()
        ]

        handler_manager = HandlerManager(
            handlers
        )

        self.manager.register(
            "handler_manager",
            handler_manager
        )

    # =====================================
    # Input
    # =====================================

    def register_input_modules(self):

        input_manager = InputManager()

        self.manager.register(
            "input_manager",
            input_manager
        )

    # =====================================
    # Comandos
    # =====================================

    def register_command_modules(self):

        command_processor = CommandProcessor()

        command_processor.register(
            "help",
            HelpCommand()
        )

        command_processor.register(
            "memory",
            MemoryCommand()
        )

        command_processor.register(
            "sair",
            ExitCommand()
        )

        self.manager.register(
            "command_processor",
            command_processor
        )

    # =====================================
    # Brain
    # =====================================

    def register_brain_modules(self):

        brain = Brain()

        self.manager.register(
            "brain",
            brain
        )

    # =====================================
    # Acesso ao Manager
    # =====================================

    def get_manager(self):

        return self.manager