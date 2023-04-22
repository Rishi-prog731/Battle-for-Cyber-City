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
    STATES: dict[str, list[bool]] = {
        'RED_LIGHT': [True, False, False],
        'YELLOW_LIGHT': [False, True, False],
        'GREEN_LIGHT': [False, False, True],
        'ALL_OFF': [False, False, False],
        'ALL_ON': [True, True, True]
    }
    """ The possible states of the traffic light. """

    def __init__(self, red_light: Light, yellow_light: Light,
                green_light: Light) -> None:
        self.red_light: Light = red_light
        self.yellow_light: Light = yellow_light
        self.green_light: Light = green_light
