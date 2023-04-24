"""
The class for the traffic lights.
"""

from typing import List

from pymodbus.client import ModbusTcpClient as ModbusClient

from .light import Light

class TrafficLight():
    """ The traffic light class."""
    HOST = '127.0.0.1'
    """ The Modbus host `IP address`. """
    PORT = 502
    """ The Modbus `port`. """
    CLIENT = ModbusClient(HOST, PORT)
    """ The ModBus `client`. """
    @staticmethod
    def set_host(val: str) -> None:
        """
        Sets the host `IP address` of the modbus client
        Args:
            val (str): `IP address`
        """
        TrafficLight.HOST = val
        TrafficLight.CLIENT = ModbusClient(TrafficLight.HOST, TrafficLight.PORT)
    @staticmethod
    def set_port(val: int) -> None:
        """
        Sets the host `port` of the modbus client
        Args:
            val (int): `port`
        """
        TrafficLight.PORT = val
        TrafficLight.CLIENT = ModbusClient(TrafficLight.HOST, TrafficLight.PORT)
    class States():
        """
        Enum for states that the traffic light can have
        
        [ `GREEN`, `YELLOW`, `RED` ]
        """
        RED_LIGHT = [True, False, False]
        YELLOW_LIGHT = [False, True, False]
        GREEN_LIGHT = [False, False, True]
        ALL_OFF = [False, False, False]
        ALL_ON = [True, True, True]
    def __init__(self, red_light: Light, yellow_light: Light,
                green_light: Light) -> None:
        self.red_light: Light = red_light
        self.yellow_light: Light = yellow_light
        self.green_light: Light = green_light
        self.state: List[bool] = TrafficLight.States.ALL_OFF
    def __str__(self) -> str:
        """
        Returns the current state of the `TrafficLight` as a `string`
        Returns:
            str: Current state of the Traffic Light
        ⚫⚫⚫ for OFF
        ⚫⚫🔴 for RED
        ⚫🟡⚫ for YELLOW
        🟢⚫⚫ for GREEN
        """
        out = ''
        out += '🟢' if self.green_light.state else '⚫'
        out += '🟡' if self.yellow_light.state else '⚫'
        out += '🔴' if self.red_light.state else '⚫'
        return out
    @property.setter
    def state(self, val: List[bool]) -> None:
        if self.state:
            self.state = val
        else:
            self.state = TrafficLight.States.ALL_OFF
    def update(self) -> None:
        """ Updates the states of the lights with the current state. """
        if self.state[0]:
            self.red_light.enable()
        else:
            self.red_light.disable()
        if self.state[1]:
            self.yellow_light.enable()
        else:
            self.yellow_light.disable()
        if self.state[2]:
            self.green_light.enable()
        else:
            self.green_light.disable()
    def write(self) -> None:
        """ Writes the states of the lights to the Modbus coils. """
        with TrafficLight.CLIENT.connect():
            TrafficLight.CLIENT.write_coil(
                self.red_light.coil, self.red_light.state)
            TrafficLight.CLIENT.write_coil(
                self.yellow_light.coil, self.yellow_light.state)
            TrafficLight.CLIENT.write_coil(
                self.green_light.coil, self.green_light.state)
    def read(self) -> List[bool]:
        """ Reads the current state of the Modbus Coils """
        out = [False, False, False]
        with TrafficLight.CLIENT.connect():
            out[0] = TrafficLight.CLIENT.read_coils(
                self.red_light.coil, 1).bits[0]
            out[1] = TrafficLight.CLIENT.read_coils(
                self.yellow_light.coil, 1).bits[0]
            out[2] = TrafficLight.CLIENT.read_coils(
                self.green_light.coil, 1).bits[0]
        return out
