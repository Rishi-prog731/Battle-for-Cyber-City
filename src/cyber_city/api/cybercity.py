"""
CyberCity is the main class that holds all the components of the City
"""

from typing import List
from cyber_city.api import TrafficLight, District, System


class CyberCity:
    """
    CyberCity is the main class that holds all the components of the City
    """

    def __init__(
        self,
        traffic_lights: List[TrafficLight],
        districts: List[District],
        power_grid: System,
    ) -> None:
        self.traffic_lights: List[TrafficLight] = traffic_lights
        self.districts: List[District] = districts
        self.power_grid: System = power_grid

    def write_all(self) -> None:
        """
        Write all the values of the traffic lights and districts to the modbus server
        """
        for item in self.traffic_lights:
            item.write()
        for item in self.districts:
            item.write()
