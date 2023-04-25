""" Special District Class"""

from .district import District
from .modbus_system import ModbusSystem
from .system import System
from .power import Power

class SpecialDistrict(District):
    """ Special District Object """
    def __init__(self, name: str, power: Power,
                local_power: ModbusSystem, generator: System) -> None:
        super().__init__(name, power)
        self.local_power: ModbusSystem = local_power
        self.generator: System = generator
    def __str__(self) -> str:
        return f"{super().__str__()}, Local_Power({self.local_power}), Generator({self.generator})"
