""" API for CyberCity """

from typing import List
from pymodbus.client import ModbusTcpClient as ModbusClient

class District():
    """ The District Object """
    def __init__(self, name: str, power_coil: int):
        """
        Initialize a District Object
        Args:
            name (str): Name of the District
            power_coil (int): Modbus coil address for the District Power
        """
        self.name = name
        """ Name of the District """
        self.power = Power(name, power_coil)
        """ Power Object for the District """
    def __str__(self) -> str:
        """
        Returns the current state of the District as a string
        Returns:
            str: Current state of the District
        """
        out = ""
        out += self.name
        out += "\t=>\t"
        out += str(self.power)
        return out

class SpecialDistrict(District):
    """ The Special District Object """
    HOST = '127.0.0.1'
    """ IP Address of the Modbus Server """
    PORT = 502
    """ Port of the Modbus Server """
    CLIENT = ModbusClient(HOST, PORT)
    @staticmethod
    def set_host(host: str):
        """
        Set the IP Address of the Modbus Server
        Args:
            host (str): IP Address of the Modbus Server
        """
        SpecialDistrict.HOST = host
        SpecialDistrict.CLIENT = ModbusClient(SpecialDistrict.HOST, SpecialDistrict.PORT)
    @staticmethod
    def set_port(port: int):
        """
        Set the Port of the Modbus Server
        Args:
            port (int): Port of the Modbus Server
        """
        SpecialDistrict.PORT = port
        SpecialDistrict.CLIENT = ModbusClient(SpecialDistrict.HOST, SpecialDistrict.PORT)
    def __init__(self, name: str, power_coil: int):
        """
        Initialize a Special District Object
        Args:
            name (str): Name of the Special District
            power_coil (int): Modbus coil address for the Special District Power
        """
        super().__init__(name, power_coil)
        self.start_coil = 0
        """ Modbus coil address for the Special District """
        self.special_power = True
        """ Special Power state """
        self.special_generator = False
        """ Special Generator state """
    def __str__(self) -> str:
        """
        Returns the current state of the Special District as a string
        Returns:
            str: Current state of the Special District
        """
        return super().__str__() + "⚡" if self.special_power else "🔌" + "\t" + "🔋" if self.special_generator else "🔌"
    def special_power_on(self) -> None:
        """ Set the Special Power to ON """
        self.special_power = True
    def special_power_off(self) -> None:
        """ Set the Special Power to OFF """
        self.special_power = False
    def is_special_power_on(self) -> bool:
        """ Returns the Special Power state """
        return self.special_power
    def special_generator_on(self) -> None:
        """ Set the Special Generator to ON """
        self.special_generator = True
    def special_generator_off(self) -> None:
        """ Set the Special Generator to OFF """
        self.special_generator = False
    def is_special_generator_on(self) -> bool:
        """ Returns the Special Generator state """
        return self.special_generator
    def write(self):
        """ Write the current state of the Special District to the Modbus Server """
        if SpecialDistrict.CLIENT.connect():
            SpecialDistrict.CLIENT.write_coils(self.start_coil, [self.special_power, self.special_generator])
            SpecialDistrict.CLIENT.close()
        else:
            return
    def read(self) -> List[bool]:
        """
        Read the current state of the Special District from the Modbus Server and update the Special District
        Returns:
            List[bool]: Current state of the Special District
        """
        if SpecialDistrict.CLIENT.connect():
            result = SpecialDistrict.CLIENT.read_coils(self.start_coil, 2)
            SpecialDistrict.CLIENT.close()
            [self.special_power, self.special_generator] = result.bits[:2]
            return result.bits[:2]
        else:
            return []
