from typing import List
from pymodbus.client import ModbusTcpClient as ModbusClient

from .District import District

class SpecialDistrict(District):
    """
    A special district is a district that has special features.
    """
    
    def __init__(self, name: str, globalPowerCoil: int, host: str, port: int, startCoil: int = 0):
        """
        Initialize a special district.
        Args:
            name (str): Name of the district.
            globalPowerCoil (int): Coil number of the global power coil.
            host (str): Hostname or IP address of the Modbus Server
            port (int): Port of the Modbus Server
            startCoil (int, optional): Defaults to 0. Coil number of the first coil of the special district.
        """
        super().__init__(name, globalPowerCoil)

        self.HOST = host
        """ Hostname or IP address of the Modbus Server """
        self.PORT = port
        """ Port of the Modbus Server """
        self.CLIENT = ModbusClient(self.HOST, self.PORT)
        """ Modbus Client """

        self.localPower = True
        """ Local power status of the district. """
        self.localGenerator = False
        """ Local generator status of the district."""

        self.startCoil = startCoil
        """ Coil number of the first coil of the special district. """

    def __str__(self) -> str:
        """
        Returns a string representation of the special district.
        Returns:
            str: String representation of the special district.
        """
        return super().__str__() + f'{"🔌" if self.localPower else "⚫"} {"🔋" if self.localGenerator else "⚫"}'

    def localPowerOff(self):
        """
        Turn off the local power of the district.
        """
        self.localPower = False
    def localPowerOn(self):
        """
        Turn on the local power of the district.
        """
        self.localPower = True
    def getLocalPower(self) -> bool:
        """
        Get the local power status of the district.
        Returns:
            bool: Local power status of the district.
        """
        return self.localPower

    def localGeneratorOff(self):
        """
        Turn off the local generator of the district.
        """
        self.localGenerator = False
    def localGeneratorOn(self):
        """
        Turn on the local generator of the district.
        """
        self.localGenerator = True
    def getLocalGenerator(self) -> bool:
        """
        Get the local generator status of the district.
        Returns:
            bool: Local generator status of the district.
        """
        return self.localGenerator

    def write(self):
        """
        write the local power and generator status to the Modbus Server.
        """
        if self.CLIENT.connect():
            self.CLIENT.write_coils(self.startCoil, [self.localPower, self.localGenerator])
            self.CLIENT.close()
        else:
            return
    def read(self) -> List[bool]:
        """
        Read the local power and generator status from the Modbus Server.
        Returns:
            List[bool]: Local power and generator status of the district.
        """
        if self.CLIENT.connect():
            result = self.CLIENT.read_coils(self.startCoil, 2)
            self.CLIENT.close()
            return result.bits[:2]
        else:
            return