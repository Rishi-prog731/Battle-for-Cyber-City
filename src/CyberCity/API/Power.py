from pymodbus.client import ModbusTcpClient as ModbusClient

class Power():
    """
    Power Object
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
        Power.HOST = host
        
        Power.client = ModbusClient(Power.HOST, Power.PORT)
    @staticmethod
    def setPort(port: int):
        """
        Set the Port of the Modbus Server
        Args:
            port (int): Port of the Modbus Server
        """
        Power.PORT = port
        
        Power.client = ModbusClient(Power.HOST, Power.PORT)

    mainGrid = True
    """ Main Grid Status """

    @staticmethod
    def mainGridOff():
        """
        Turn the main grid off
        """
        Power.mainGrid = False
    @staticmethod
    def mainGridOn():
        """
        Turn the main grid on
        """
        Power.mainGrid = True
    @staticmethod
    def getMainGrid() -> bool:
        """
        Get the state of the main grid
        Returns:
            bool: state of the main grid
        """
        return Power.mainGrid

    def __init__(self, name: str, globalPowerCoil: int):
        """
        Initialize the Power Object
        Args:
            name (str): Name of the Power
            globalPowerCoil (int): Modbus coil address
        """
        self.name = name
        """ Name of the object """
        self.globalPowerCoil = globalPowerCoil
        """ Modbus coil address """

        self.globalPower = True
        """ Weather the power grid connection is on or off """

    def __str__(self) -> str:
        """
        Returns the current state of the Power Connection
        Returns:
            str: State of power connection
        ⚡ for True
        ⚫ for False
        """
        return f'{"⚡" if self.globalPower else "⚫"}'

    def globalPowerOff(self):
        """
        Turn of the power
        """
        self.globalPower = False
    def globalPowerOn(self):
        """
        Turn on the power
        """
        self.globalPower = True
    def getGlobalPower(self) -> bool:
        """
        Get the state of the power connection
        Returns:
            bool: the current state of the power connection
        """
        return self.globalPower

    def write(self):
        """
        Write the current state of the Power to the Modbus Server
        """
        if Power.client.connect():
            if Power.mainGrid:
                self.client.write_coil(self.globalPowerCoil, self.globalPower)
            else:
                self.client.write_coil(self.globalPowerCoil, False)
            self.client.close()
        else:
            return
    def read(self) -> bool:
        """
        Reads the current state of the Power from the Modbus Server
        Returns:
            bool: Current state of the Power
        """
        if Power.client.connect():
            result = self.client.read_coils(self.globalPowerCoil, 1)
            self.client.close()
            return result.bits[0]
        else:
            return
