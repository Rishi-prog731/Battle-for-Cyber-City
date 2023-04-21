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
    
    @staticmethod
    def setHost(host: str):
        """
        Set the IP Address of the Modbus Server
        Args:
            host (str): IP Address of the Modbus Server
        """
        TrafficLight.HOST = host
        
        TrafficLight.client = ModbusClient(TrafficLight.HOST, TrafficLight.PORT)
    @staticmethod
    def setPort(port: int):
        """
        Set the Port of the Modbus Server
        Args:
            port (int): Port of the Modbus Server
        """
        TrafficLight.PORT = port
        
        TrafficLight.client = ModbusClient(TrafficLight.HOST, TrafficLight.PORT)

    def __init__(self, name: str, startCoil: int):
        """
        Initialize a Traffic Light Object
        Args:
            name (str): Name of the Traffic Light
            startCoil (int): Modbus coil address for GREEN Light, YELLOW is +1, RED is +2
        """
        self.name: str = name
        """ Name of the Traffic Light """
        self.startCoil: int = startCoil
        """ Modbus coil address for GREEN Light, YELLOW is +1, RED is +2 """

        self.RED = False
        """ RED Light state """
        self.YELLOW = False
        """ YELLOW Light state """
        self.GREEN = False
        """ GREEN Light state """

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
