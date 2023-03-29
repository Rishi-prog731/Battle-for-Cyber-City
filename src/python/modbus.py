from pymodbus.client import ModbusTcpClient

class Modbus:
    def __init__(self, HOST='127.0.0.1', POST=502):
        self.client = ModbusTcpClient(HOST, POST)
        
    def connect(self):
        self.client.connect()
    
    def disconnect(self):
        self.client.close()