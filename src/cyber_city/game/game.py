from typing import List

from cyber_city.game import Role, Ability, District
from cyber_city.api import System, TrafficLight


class Game:
    def __init__(
        self,
        defender_budget: int = 5000,
        attacker_budget: int = 5000,
        max_rounds: int = 10,
        defender_abilities: List[Ability] = [],
        attacker_abilities: List[Ability] = [],
        districts: List[District] = [],
        power_grid: List[System] = [],
        traffic_lights: List[TrafficLight] = [],
    ) -> None:
        self.max_rounds = max_rounds

        self.defender: Role = Role("Defender", defender_budget)
        self.attacker: Role = Role("Attacker", attacker_budget)

        self.defender.abilities = defender_abilities
        self.attacker.abilities = attacker_abilities

        self.power_grid = power_grid

        self.traffic_lights = traffic_lights

        self.districts = districts
