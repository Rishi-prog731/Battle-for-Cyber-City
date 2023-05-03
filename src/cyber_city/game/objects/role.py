from typing import List

from .ability import Ability

class Role():
    def __init__(self,
                name: str = "",
                budget: int = 5000,
                abilities: List[Ability] = []) -> None:
        self.name: str = name
        self.budget: int = budget
        self.abilities: List[Ability] = abilities

    def __str__(self) -> str:
        out = ""
        out += "Role: " + self.name
        out += "\tBudget: " + str(self.budget)
        out += "\tAbilities: " + str(self.abilities)
        return out