""" The class for the traffic lights. """

from typing import List

from pymodbus.client import ModbusTcpClient as ModbusClient

from .system import System

class TrafficLight():
    """ The traffic light class."""

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

    def __init__(self, red_light: System, yellow_light: System,
                green_light: System, host: str = '127.0.0.1', port: int = 502
                ) -> None:
        """
        Initialize a new Traffic Light.
        
        Args:
            red_light (System): Red Light System Object
            yellow_light (System): Yellow Light System Object
            green_light (System): Green Light System Object
            host (str): `IP address` of the Modbus Server
            port (int): `Port` of the Modbus Server
        """
        self.red_light: System = red_light
        """ Red Light System Object """
        self.yellow_light: System = yellow_light
        """ Yellow Light System Object """
        self.green_light: System = green_light
        """ Green Light System Object """
        self.state = TrafficLight.States.ALL_OFF
        """ `State` of the lights """
        self._host = host
        """ The Modbus host `IP address`. """
        self._port = port
        """ The Modbus `port`. """
        self._client = ModbusClient(self._host, self._port)
        """ The Modbus `client`. """
    def __str__(self) -> str:
        """
        Returns the current state of the `TrafficLight` as a `string`
        ⚫⚫⚫: ALL_OFF
        🟢🟡🔴: ALL_ON
        ⚫⚫🔴: RED_LIGHT
        ⚫🟡⚫: YELLOW_LIGHT
        🟢⚫⚫: GREEN_LIGHT

        Returns:
            str: Current state of the Traffic Light
        """
        out = ''
        out += '🟢' if self.green_light.state else '⚫'
        out += '🟡' if self.yellow_light.state else '⚫'
        out += '🔴' if self.red_light.state else '⚫'
        return out

    @property
    def host(self) -> str:
        """
        Get Host
        
        Returns:
            str: host `IP address`
        """
        return self.host
    @host.setter
    def host(self, val: str) -> None:
        self._host = val
        self._client = ModbusClient(self._host, self._port)
    @property
    def port(self) -> int:
        """
        Get Port

        Returns:
            int: host `port`
        """
        return self.port
    @port.setter
    def port(self, val: int) -> None:
        self._port = val
        self._client = ModbusClient(self._host, self._port)

    def update(self) -> None:
        """ Updates the states of the lights with the current state. """
        self.green_light.state = self.state[0]
        self.yellow_light.state = self.state[1]
        self.red_light.state = self.state[2]
    def write(self) -> None:
        """ Writes the states of the lights to the Modbus coils. """
        with self._client.connect():
            self._client.write_coil(
                self.red_light.coil, self.red_light.state)
            self._client.write_coil(
                self.yellow_light.coil, self.yellow_light.state)
            self._client.write_coil(
                self.green_light.coil, self.green_light.state)
    def read(self) -> List[bool]:
        """ Reads the current state of the Modbus Coils """
        out = [False, False, False]
        with self._client.connect():
            out[0] = self._client.read_coils(
                self.red_light.coil, 1).bits[0]
            out[1] = self._client.read_coils(
                self.yellow_light.coil, 1).bits[0]
            out[2] = self._client.read_coils(
                self.green_light.coil, 1).bits[0]
        return out
