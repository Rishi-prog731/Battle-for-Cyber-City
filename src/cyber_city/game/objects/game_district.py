from typing import List

from cyber_city.api import District, Power, System, ModbusSystem
from cyber_city.game.objects import Event, Ability


class GameDistrict(District):
    def __init__(
        self,
        name: str,
        power: Power,
        default_abilities: List[Ability] = None,
        local_power: ModbusSystem = None,
        generator: System = None,
    ) -> None:
        super().__init__(name, power, local_power, generator)
        self.compromised_level: int = 0
        self.active_attacks: List[Ability] = []
        self.active_defenses: List[Ability] = []
        self.default_abilities: List[Ability] = default_abilities
        self.events: dict(int, Event) = {
            -100: None,
            -75: None,
            -50: None,
            -25: None,
            0: None,
            25: None,
            50: None,
            75: None,
            100: None,
        }

    def __str__(self) -> str:
        out = super().__str__()
        out += f"\tCompromised_Level({self.compromised_level})\n"
        out += f"\tActive_Attacks({self.active_attacks})\n"
        out += f"\tActive_Defenses({self.active_defenses})\n"
        out += f"\tEvents({self.events})\n"
        return out

    def calc_compromise_level(self) -> int:
        out = 0

        # Add Default Abilities to Compromise Level
        for ability in dict.fromkeys(self.default_abilities):
            out -= ability.modifier

        # Add Active Defences to Compromise Level
        for ability in dict.fromkeys(self.active_defenses):
            if not ability in self.default_abilities:
                out -= ability.modifier

        # Add active attacks but if matchup modify the attack modifier
        for ability in dict.fromkeys(self.active_attacks):
            if (
                ability.matchup in self.active_defenses
                or ability.matchup in self.default_abilities
            ):
                out += ability.modifier * 0.5
            else:
                out += ability.modifier

        return out
