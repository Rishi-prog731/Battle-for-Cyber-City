"""
Ability is a class that holds the information about an ability
"""


class Ability:
    """
    Ability is a class that holds the information about an ability
    """

    def __init__(self, name: str, cost: int, modifier: int) -> None:
        self.name: str = name
        self.cost: int = cost
        self.modifier: int = modifier
        self.matchup: Ability = None

    def __str__(self) -> str:
        out = ""
        out += f"Name: {self.name}\n"
        out += f"Cost: {self.cost}\n"
        out += f"Modifier: {self.modifier}\n"
        if self.matchup is not None:
            out += f"Matchup: {self.matchup.name}"
        return out
