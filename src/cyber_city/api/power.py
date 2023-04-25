from typing import List

from .system import System

class PowerGrid():
    """ Power Grid Object """
    def __init__(self, systems: List[System]) -> None:
        """ Initialize the Power Grid """
        self.systems = systems
        self.main_grid = True

    def main_on(self) -> None:
        """ Turn on the main grid """
        self.main_grid = True
    def main_off(self) -> None:
        """ Turn off the main grid """
        self.main_grid = False
    def main_set(self, state: bool) -> None:
        """ Set the main grid to a state """
        self.main_grid = state

    def system_on(self, index: int) -> None:
        """ Turn on a system """
        self.systems[index].set(True and self.main_grid)
    def system_off(self, index: int) -> None:
        """ Turn off a system """
        self.systems[index].set(False)
    def system_set(self, index: int, state: bool) -> None:
        """ Set a system to a state """
        self.systems[index].set(state and self.main_grid)

    def write(self) -> None:
        """ Write the state of the power grid to the modbus server """
        for system in self.systems:
            system.write()
    def read(self) -> List[bool]:
        """
        Read and return the state of the power grid from the modbus server
        """
        out = []
        for system in self.systems:
            out.append(system.read())
        return out
