""" 
The class object that represents and manages traffic lights and makes it 
easier to manage and program them. It is a wrapper around the `System` class.
"""

from typing import List

from .modbus_system import ModbusSystem


class TrafficLight:
    """Traffic Light Object"""

    class States:
        """
        Enum containing all Traffic Light States
        [`RED`, `YELLOW`, `GREEN`]
        """

        ALL_ON = [True, True, True]
        ALL_OFF = [False, False, False]
        RED_LIGHT = [True, False, False]
        YELLOW_LIGHT = [False, True, False]
        GREEN_LIGHT = [False, False, True]

    def __init__(
        self,
        red_light: ModbusSystem,
        yellow_light: ModbusSystem,
        green_light: ModbusSystem,
    ) -> None:
        self.red_light = red_light
        self.yellow_light = yellow_light
        self.green_light = green_light

    def __str__(self) -> str:
        out = ""
        out += "🔴" if self.red_light.state else "⚫️"
        out += "🟡" if self.yellow_light.state else "⚫️"
        out += "🟢" if self.green_light.state else "⚫️"
        return out

    def set_state(self, state: List[bool]) -> None:
        """
        Set the state of the traffic light
        """
        self.red_light.set(state[0])
        self.yellow_light.set(state[1])
        self.green_light.set(state[2])

    def write(self) -> None:
        """
        Write the state of the traffic light to the modbus server
        """
        self.red_light.write()
        self.yellow_light.write()
        self.green_light.write()

    def read(self) -> List[bool]:
        """
        Read and return the state of the traffic light from the modbus server
        """
        return [
            self.red_light.read(),
            self.yellow_light.read(),
            self.green_light.read(),
        ]
