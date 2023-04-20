from typing import List
from pymodbus.client import ModbusTcpClient as ModbusClient

class TrafficLight():
    """
    Traffic Light Object
    """
    HOST = '127.0.0.1'
    """ IP Address of the Modbus Server """
    PORT = 502
    """ Port of the Modbus Server """
    client = ModbusClient(HOST, PORT)
    """ Modbus Client """

    def __init__(self, name: str, startCoil: int):
        """
        Initialize a Traffic Light Object
        Args:
            name (str): Name of the Traffic Light
            startCoil (int): the coil for GREEN Light, YELLOW is +1, RED is +2
        """
        self.name: str = name
        """ Name of the Traffic Light """
        self.startCoil: int = startCoil
        """ The coil for GREEN Light, YELLOW is +1, RED is +2 """

        self.RED = False
        """ RED Light """
        self.YELLOW = False
        """ YELLOW Light """
        self.GREEN = False
        """ GREEN Light """

    def __str__(self) -> str:
        """
        Returns the current state of the Traffic Light as a string
        Returns:
            str: Current state of the Traffic Light 
        ⚫⚫⚫ for OFF
        ⚫⚫🔴 for RED
        ⚫🟡⚫ for YELLOW
        🟢⚫⚫ for GREEN
        """
        return f'{"🔴" if self.RED else "⚫"} {"🟡" if self.YELLOW else "⚫"} {"🟢" if self.GREEN else "⚫"}'

    def toRed(self):
        """
        Set the light to RED
        """
        self.RED = True
        self.YELLOW = False
        self.GREEN = False
    def isRed(self) -> bool:
        """
        Check if the light is RED
        Returns:
            bool: True if RED, False if not
        """
        return self.RED and not self.YELLOW and not self.GREEN

    def toYellow(self):
        """
        Set the light to YELLOW
        """
        self.RED = False
        self.YELLOW = True
        self.GREEN = False
    def isYellow(self) -> bool:
        """
        Check if the light is YELLOW
        Returns:
            bool: True if YELLOW, False if not
        """
        return self.YELLOW and not self.RED and not self.GREEN

    def toGreen(self):
        """
        Set the light to GREEN
        """
        self.RED = False
        self.YELLOW = False
        self.GREEN = True
    def isGreen(self) -> bool:
        """
        Check if the light is GREEN
        Returns:
            bool: True if GREEN, False if not
        """
        return self.GREEN and not self.RED and not self.YELLOW

    def allOff(self):
        """
        Set all lights to OFF
        """
        self.RED = False
        self.YELLOW = False
        self.GREEN = False
    def isOff(self) -> bool:
        """
        Check if all lights are OFF
        Returns:
            bool: True if all lights are OFF, False if not
        """
        return not self.RED and not self.YELLOW and not self.GREEN

    def allOn(self):
        """
        Set all lights to ON
        """
        self.RED = True
        self.YELLOW = True
        self.GREEN = True
    def isOn(self) -> bool:
        """
        Check if all lights are ON
        Returns:
            bool: True if all lights are ON, False if not
        """
        return self.RED and self.YELLOW and self.GREEN

    def write(self):
        """
        Write the current state of the Traffic Light to the Modbus Server
        """
        if TrafficLight.client.connect():
            self.client.write_coils(self.startCoil, [self.GREEN, self.YELLOW, self.RED])
            self.client.close()
        else:
            return
    def read(self) -> List[bool]:
        """
        Read the current state of the Traffic Light from the Modbus Server
        Returns:
            List[bool]: List of the current state of the Traffic Light
        """
        if TrafficLight.client.connect():
            result = self.client.read_coils(self.startCoil, 3)
            self.client.close()
            return result.bits[:3]
        else:
            return

class Power():
    HOST = '127.0.0.1'
    PORT = 502
    client = ModbusClient(HOST, PORT)

    mainGrid = True

    @staticmethod
    def mainGridOff():
        Power.mainGrid = False

    @staticmethod
    def mainGridOn():
        Power.mainGrid = True

    def __init__(self, name: str, globalPowerCoil: int):
        self.name = name
        self.globalPowerCoil = globalPowerCoil

        self.globalPower = True

    def __str__(self):
        return f'{"⚡" if self.globalPower else "⚫"}'

    def globalPowerOff(self):
        self.globalPower = False

    def globalPowerOn(self):
        self.globalPower = True

    def getGlobalPower(self) -> bool:
        return self.globalPower

    def write(self):
        if Power.client.connect():
            if Power.mainGrid:
                self.client.write_coil(self.globalPowerCoil, self.globalPower)
            else:
                self.client.write_coil(self.globalPowerCoil, False)
            self.client.close()
        else:
            return

    def read(self) -> bool:
        if Power.client.connect():
            result = self.client.read_coils(self.globalPowerCoil, 1)
            self.client.close()
            return result.bits[0]
        else:
            return

class District():
    def __init__(self, name: str, globalPowerCoil: int):
        self.name = name

        self.globalPower = Power(self.name, globalPowerCoil)

    def __str__(self):
        return f'{self.name} => {self.globalPower} '

class SpecialDistrict(District):
    def __init__(self, name: str, globalPowerCoil: int, host: str, port: int, startCoil: int = 0):
        super().__init__(name, globalPowerCoil)

        self.HOST = host
        self.PORT = port
        self.CLIENT = ModbusClient(self.HOST, self.PORT)

        self.localPower = True
        self.localGenerator = False

        self.startCoil = startCoil

    def __str__(self):
        return super().__str__() + f'{"🔌" if self.localPower else "⚫"} {"🔋" if self.localGenerator else "⚫"}'

    def localPowerOff(self):
        self.localPower = False
    def localPowerOn(self):
        self.localPower = True
    def getLocalPower(self) -> bool:
        return self.localPower

    def localGeneratorOff(self):
        self.localGenerator = False
    def localGeneratorOn(self):
        self.localGenerator = True
    def getLocalGenerator(self) -> bool:
        return self.localGenerator

    def write(self):
        if self.CLIENT.connect():
            self.CLIENT.write_coils(self.startCoil, [self.localPower, self.localGenerator])
            self.CLIENT.close()
        else:
            return

    def read(self) -> List[bool]:
        if self.CLIENT.connect():
            result = self.CLIENT.read_coils(self.startCoil, 2)
            self.CLIENT.close()
            return result.bits[:2]
        else:
            return