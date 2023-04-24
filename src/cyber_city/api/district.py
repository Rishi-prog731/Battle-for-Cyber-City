from .system import System

class District():
    """
    The District class
    """
    def __init__(self, name: str, power_coil: int) -> None:
        self.name = name
        self.power = System(power_coil)
