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
    def set_host(host: str):
        """
        Set the IP Address of the Modbus Server
        Args:
            host (str): IP Address of the Modbus Server
        """
        TrafficLight.HOST = host

        TrafficLight.client = ModbusClient(TrafficLight.HOST, TrafficLight.PORT)
    @staticmethod
    def set_port(port: int):
        """
        Set the Port of the Modbus Server
        Args:
            port (int): Port of the Modbus Server
        """
        TrafficLight.PORT = port
        TrafficLight.client = ModbusClient(TrafficLight.HOST, TrafficLight.PORT)

    def __init__(self, name: str, start_coil: int):
        """
        Initialize a Traffic Light Object
        Args:
            name (str): Name of the Traffic Light
            startCoil (int): Modbus coil address for GREEN Light, YELLOW is +1, RED is +2
        """
        self.name: str = name
        """ Name of the Traffic Light """
        self.start_coil: int = start_coil
        """ Modbus coil address for GREEN Light, YELLOW is +1, RED is +2 """

        self.red = False
        """ RED Light state """
        self.yellow = False
        """ YELLOW Light state """
        self.green = False
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
        return f'{"🔴" if self.red else "⚫"} {"🟡" if self.yellow else "⚫"} {"🟢" if self.green else "⚫"}'

    def to_red(self):
        """
        Set the light to RED
        """
        self.red = True
        self.yellow = False
        self.green = False
    def is_red(self) -> bool:
        """
        Check if the light is RED
        Returns:
            bool: True if RED, False if not
        """
        return self.red and not self.yellow and not self.green

    def to_yellow(self):
        """
        Set the light to YELLOW
        """
        self.red = False
        self.yellow = True
        self.green = False
    def is_yellow(self) -> bool:
        """
        Check if the light is YELLOW
        Returns:
            bool: True if YELLOW, False if not
        """
        return self.yellow and not self.red and not self.green

    def to_green(self):
        """
        Set the light to GREEN
        """
        self.red = False
        self.yellow = False
        self.green = True
    def is_green(self) -> bool:
        """
        Check if the light is GREEN
        Returns:
            bool: True if GREEN, False if not
        """
        return self.green and not self.red and not self.yellow

    def all_off(self):
        """
        Set all lights to OFF
        """
        self.red = False
        self.yellow = False
        self.green = False
    def is_off(self) -> bool:
        """
        Check if all lights are OFF
        Returns:
            bool: True if all lights are OFF, False if not
        """
        return not self.red and not self.yellow and not self.green

    def all_on(self):
        """
        Set all lights to ON
        """
        self.red = True
        self.yellow = True
        self.green = True
    def is_on(self) -> bool:
        """
        Check if all lights are ON
        Returns:
            bool: True if all lights are ON, False if not
        """
        return self.red and self.yellow and self.green

    def write(self):
        """
        Write the current state of the Traffic Light to the Modbus Server
        """
        if TrafficLight.client.connect():
            self.client.write_coils(self.start_coil, [self.green, self.yellow, self.red])
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
            result = self.client.read_coils(self.start_coil, 3)
            self.client.close()
            return result.bits[:3]
        else:
            return
