""" 
Class for all objects that have a on/oof state
"""

class System():
    """ The System class """
    def __init__(self):
        self.state = False

    def __str__(self) -> str:
        return "✔️" if self.state else "❌"

    def enable(self) -> None:
        """ Turn on the system by setting `state` to `True` """
        self.state = True
    def disable(self) -> None:
        """ Turn off the system by setting `state` to `False` """
        self.state = False
    def set(self, val: bool) -> None:
        """ Set the system state by setting `state` to `val` """
        self.state = val
