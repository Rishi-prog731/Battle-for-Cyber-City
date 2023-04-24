""" The class for the power grid. """

from pymodbus.client import ModbusTcpClient as ModbusClient

from .system import System

class PowerGrid():
    """ The PowerGrid Class """
    HOST = '127.0.0.1'
    """ The Modbus host `IP address`. """
    PORT = 502
    """ The Modbus `port`."""
    CLIENT = ModbusClient(HOST, PORT)
    """ The Modbus `client`. """
    @staticmethod
    def set_host(val: str) -> None:
        """
        Sets the host `IP address` of the modbus client
        Args:
            val (str): `IP address`
        """
        PowerGrid.HOST = val
        PowerGrid.CLIENT = ModbusClient(PowerGrid.HOST, PowerGrid.PORT)
    @staticmethod
    def set_port(val: int) -> None:
        """
        Sets the host `port` of the modbus client
        Args:
            val (int): `port`
        """
        PowerGrid.PORT = val
        PowerGrid.CLIENT = ModbusClient(PowerGrid.HOST, PowerGrid.PORT)

    MAIN_GRID = True
    """ State of the main power grid """
    @staticmethod
    def main_grid_on() -> None:
        """ Turn `on` main power grid. """
        PowerGrid.MAIN_GRID = True
    @staticmethod
    def main_grid_off() -> None:
        """ Turn `off` main power grid. """
        PowerGrid.MAIN_GRID = False

    @staticmethod
    def write(system: System) -> None:
        """
        Writes the state of the `System` to the modbus coils

        Args:
            system (System): `System` you want to write from
        """
        on_: bool = PowerGrid.MAIN_GRID and system.state
        with PowerGrid.CLIENT.connect():
            PowerGrid.CLIENT.write_coil(system.coil, on_)

    @staticmethod
    def read(system: System) -> bool:
        """
        Reads the current Modbus state of a `System`'s coil
        
        Args:
            system (System): `System` you want to check the modbus state of
        Returns:
            bool: state of the `System`'s coil
        """
        with PowerGrid.CLIENT.connect():
            return PowerGrid.CLIENT.read_coils(system.coil, 1).bits[0]
