from cyber_city.api import District, Power
from cyber_city.game.objects import Event

class GameDistrict(District):
    def __init__(self, name: str, power: Power) -> None:
        super().__init__(name, power)
        self.compromised_level: int = 0
        self.active_attacks: list = []
        self.active_defenses: list = []
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
        return out