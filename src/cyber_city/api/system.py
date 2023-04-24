"""
The class for a system in modbus. It contains a coil and a state.
"""
class System():
    """ The System class """
    def __init__(self, coil: int) -> None:
        self.__coil: int = coil
        """ The coil address number of the System """
        self.state: bool = False
        """ The state of the System (on/off) """
    def __str__(self) -> str:
        """
        Returns:
            str: The string representation of the System
        """
        return f"{self.coil}: {'✅' if self.state else '☑️'}\t"
    @property
    def coil(self) -> int:
        """
        Returns:
            int: The coil address number of the system
        """
        return self.__coil
    def enable(self) -> None:
        """ Turns on the System """
        self.state = True
    def disable(self) -> None:
        """ Turns off the System """
        self.state = False
