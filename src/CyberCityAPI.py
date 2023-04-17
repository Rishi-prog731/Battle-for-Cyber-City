from typing import List
from pymodbus.client import ModbusTcpClient as ModbusClient

class TrafficLight():
    HOST = '127.0.0.1' # Modbus Server's IP
    PORT = 502 # Modbus Server's Port
    client = ModbusClient(HOST, PORT) # Modbus Client

    def __init__(self, name: str, coilGreen: int):
        self.name = name
        self.coilGreen = coilGreen

        self.RED = False
        self.YELLOW = False
        self.GREEN = False

    def toRed(self):
        self.RED = True
        self.YELLOW = False
        self.GREEN = False
    def isRed(self) -> bool:
        return self.RED

    def toYellow(self):
        self.RED = False
        self.YELLOW = True
        self.GREEN = False
    def isYellow(self) -> bool:
        return self.YELLOW

    def toGreen(self):
        self.RED = False
        self.YELLOW = False
        self.GREEN = True
    def isGreen(self) -> bool:
        return self.GREEN

    def allOff(self):
        self.RED = False
        self.YELLOW = False
        self.GREEN = False
    def isOff(self) -> bool:
        return not self.RED and not self.YELLOW and not self.GREEN

    def allOn(self):
        self.RED = True
        self.YELLOW = True
        self.GREEN = True
    def isOn(self) -> bool:
        return self.RED and self.YELLOW and self.GREEN

    def write(self):
        if TrafficLight.client.connect():
            self.client.write_coils(self.coilGreen, [self.GREEN, self.YELLOW, self.RED])
            self.client.close()
    def writeList(self, list: List[bool]):
        if TrafficLight.client.connect():
            self.client.write_coils(self.coilGreen, list)
            self.client.close()
    def read(self):
        if TrafficLight.client.connect():
            result = self.client.read_coils(self.coilGreen, 3)
            self.client.close()
            return result.bits[:3]
