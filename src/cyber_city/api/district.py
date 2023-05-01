""" District Class """
from .power import Power

class District():
    """ District Object """
    def __init__(self,name: str, power: Power) -> None:
        self.name: str = name
        self.power: Power = power
    def __str__(self) -> str:
        return f"{self.name}: Power({self.power})"
    def write(self) -> None:
        """ Write all systems to the modbus system """
        self.power.write()
