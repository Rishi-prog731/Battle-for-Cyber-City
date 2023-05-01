""" Power Object for districts and other things with power control """

from typing import List

from .modbus_system import ModbusSystem
from .system import System

class Power(ModbusSystem):
    """ Power Object """
    def __init__(self, coil: int, grid: List[ModbusSystem],
                host: str = '127.0.0.1', port: int = 502) -> None:
        super().__init__(coil, host, port)
        self.power_grid: System = grid

    def enable(self) -> None:
        self.state = True and self.power_grid.state
    def disable(self) -> None:
        self.state = False
    def set(self, val: bool) -> None:
        super().set(val and self.power_grid.state)
