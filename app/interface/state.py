from enum import Enum, auto


class State(Enum):
    start_page = auto()
    login_page = auto()
    interaction_page = auto()
    registration_page = auto()