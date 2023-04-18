from typing import List
from pymodbus.client import ModbusTcpClient as ModbusClient

class TrafficLight():
    HOST = '127.0.0.1' 
    PORT = 502 
    client = ModbusClient(HOST, PORT) 

    def __init__(self, name: str, startCoil: int):
        self.name = name
        self.startCoil = startCoil

        self.RED = False
        self.YELLOW = False
        self.GREEN = False

    def __str__(self):
        return f'{"🔴" if self.RED else "⚫"} {"🟡" if self.YELLOW else "⚫"} {"🟢" if self.GREEN else "⚫"}'

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
            self.client.write_coils(self.startCoil, [self.GREEN, self.YELLOW, self.RED])
            self.client.close()
        else:
            return
    def writeList(self, list: List[bool]):
        if TrafficLight.client.connect():
            self.client.write_coils(self.startCoil, list)
            self.client.close()
        else:
            return
    def read(self) -> List[bool]:
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