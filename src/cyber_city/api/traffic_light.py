from typing import List

from pymodbus.client import ModbusTcpClient as ModbusClient

from .light import Light

class TrafficLight():
    """ The traffic light class."""
    HOST = '127.0.0.1'
    """ The Modbus host IP address. """
    PORT = 502
    """ The Modbus port. """
    CLIENT = ModbusClient(HOST, PORT)
    """ The ModBus client. """

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
        self.state = TrafficLight.States.ALL_OFF

    @property.setter
    def state(self, val) -> None:
        if self.state:
            self.state = val
        else:
            self.state = 'ALL_OFF'

    def update(self) -> None:
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
        with TrafficLight.CLIENT.connect():
            TrafficLight.CLIENT.write_coil(
                self.red_light.coil, self.red_light.state)
            TrafficLight.CLIENT.write_coil(
                self.yellow_light.coil, self.yellow_light.state)
            TrafficLight.CLIENT.write_coil(
                self.green_light.coil, self.green_light.state)

    def read(self) -> List[bool]:
        out = [False, False, False]
        with TrafficLight.CLIENT.connect():
            out[0] = TrafficLight.CLIENT.read_coils(
                self.red_light.coil, 1).bits[0]
            out[1] = TrafficLight.CLIENT.read_coils(
                self.yellow_light.coil, 1).bits[0]
            out[2] = TrafficLight.CLIENT.read_coils(
                self.green_light.coil, 1).bits[0]
        return out
