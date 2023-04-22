from pymodbus.client import ModbusTcpClient as ModbusClient

from .light import Light

class TrafficLight():
    HOST = '127.0.0.1'
    PORT = 502
    CLIENT = ModbusClient(HOST, PORT)

    def __init__(self, red_light: Light, yellow_light: Light, green_light: Light) -> None:
        self.red_light: Light = red_light
        self.yellow_light: Light = yellow_light
        self.green_light: Light = green_light