"""
Extension of the `System` class. The class for objects that communicate with the
modbus server. It conects to the server and can read and write.
"""

from pymodbus.client import ModbusTcpClient as ModbusClient

from .system import System


class ModbusSystem(System):
    """The Modbus System class"""

    def __init__(self, coil: int, host: str = "127.0.0.1", port: int = 502) -> None:
        super().__init__()
        self.__host: str = host
        self.__port: int = port
        self.client = ModbusClient(self.__host, self.__port)
        self.coil: int = coil

    def __str__(self) -> str:
        return f"{self.coil}: {super().__str__()}"

    @property
    def host(self) -> str:
        """Getters and Setters for the modbus servers 'ip address'"""
        return self.__host

    @host.setter
    def host(self, val: str) -> None:
        self.__host = val
        self.client = ModbusClient(self.__host, self.__port)

    @property
    def port(self) -> int:
        """Getters and Setters for the modbus servers `port`"""
        return self.__port

    @port.setter
    def port(self, val) -> None:
        self.__port = val
        self.client = ModbusClient(self.__host, self.__port)

    def write(self) -> None:
        """Write the value of `state` to the modbus server"""
        if self.client.connect():
            self.client.write_coil(self.coil, self.state)
            self.client.close()

    def read(self) -> bool:
        """Read and return the value of the system from the modbus server"""
        if self.client.connect():
            result = self.client.read_coils(self.coil, 0)
            self.client.close()
            return result.bits[0]
