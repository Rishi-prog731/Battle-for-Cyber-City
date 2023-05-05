""" District Class """
from .power import Power

from .modbus_system import ModbusSystem
from .system import System


class District:
    """District Object"""

    def __init__(
        self,
        name: str,
        power: Power,
        local_power: ModbusSystem = None,
        generator: System = None,
    ) -> None:
        self.name: str = name
        self.power: Power = power
        self.local_power: ModbusSystem = local_power
        self.generator: System = generator

    def __str__(self) -> str:
        out = f"{self.name}\n"
        out += f"\tPower({self.power})\n"
        if self.local_power and self.generator:
            out += f"\tLocal_Power({self.local_power})\n"
            out += f"\tGenerator({self.generator})\n"
        return out

    def write(self) -> None:
        """Write all systems to the modbus system"""
        self.power.write()
        if self.local_power and self.generator:
            self.local_power.write()
            self.generator.write()
