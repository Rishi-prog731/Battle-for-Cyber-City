"""
Game is the main class that holds all the components of the game and it 
inherits from the CyberCity class
"""

from typing import List

from cyber_city.game import Role, Ability, GameDistrict
from cyber_city.api import CyberCity, System, TrafficLight


class Game(CyberCity):
    """
    Game is the main class that holds all the components of the game

    Args:
        CyberCity (CyberCity): The CyberCity class that holds all the components of the city
    """

    def __init__(
        self,
        defender_abilities: List[Ability],
        attacker_abilities: List[Ability],
        districts: List[GameDistrict],
        power_grid: System,
        traffic_lights: List[TrafficLight],
        defender_budget: int = 5000,
        attacker_budget: int = 5000,
        max_rounds: int = 10,
    ) -> None:
        super().__init__(traffic_lights, districts, power_grid)
        self.max_rounds = max_rounds

        self.defender: Role = Role("Defender", defender_budget)
        self.attacker: Role = Role("Attacker", attacker_budget)

        self.defender.abilities = defender_abilities
        self.attacker.abilities = attacker_abilities

    def __str__(self) -> str:
        out = ""

        out += ""

        return out
