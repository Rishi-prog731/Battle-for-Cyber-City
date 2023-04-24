"""
The class for the lights for the traffic lights.
"""
class Light():
    """ The light class. """
    def __init__(self, coil: int) -> None:
        self.__coil: int = coil
        """ The coil address number of the light """
        self.state: bool = False
        """ The state of the light (on/off) """
    def __str__(self) -> str:
        """
        Returns:
            str: The string representation of the light
        """
        return f"Light(coil={self.coil}, state={self.state})"
    @property
    def coil(self) -> int:
        """
        Returns:
            int: The coil address number of the light
        """
        return self.__coil
    def enable(self) -> None:
        """ Turns on the light """
        self.state = True
    def disable(self) -> None:
        """ Turns off the light """
        self.state = False
