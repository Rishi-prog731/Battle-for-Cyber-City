"""
Game is the main class that holds all the components of the game and it 
inherits from the CyberCity class
"""

import pandas as pd
from typing import List

from cyber_city.game import Role, Ability, GameDistrict
from cyber_city.api import CyberCity, System, TrafficLight


excelFileName = input("What file name do you want")


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
"""Main class variables"""


class CyberCityGameRules:
    def __init__(
        self,
        turns,
        budget,
        actions_per_turn,
        defender_turn,
        attacker_turn,
        compromise_threshold,
    ):
        self.turns = turns
        self.budget = budget
        self.actions_per_turn = actions_per_turn
        self.defender_turn = defender_turn
        self.attacker_turn = attacker_turn
        self.compromise_threshold = compromise_threshold


"""
Reading in file using pandas
"""
df = pd.read_excel(excelFileName)
"""
Getting values of variables from excel file
"""
turns = df.loc[df["Rule"] == "Turns", "Description"].values[0]
budget_defender = df.loc[df["Rule"] == "Budget", "Defender"].values[0]
budget_attacker = df.loc[df["Rule"] == "Budget", "Attacker"].values[0]
actions_per_turn = df.loc[df["Rule"] == "Action per turn", "Description"].values[0]
defender_turn_desc = df.loc[df["Rule"] == "Defender's turn", "Description"].values[0]
defender_turn_success_rate = df.loc[
    df["Rule"] == "Defender's turn", "Success rate"
].values[0]
attacker_turn_desc = df.loc[df["Rule"] == "Attacker's turn", "Description"].values[0]
attacker_turn_success_rate = df.loc[
    df["Rule"] == "Attacker's turn", "Success rate"
].values[0]
compromise_threshold = df.loc[
    df["Rule"] == "Compromise Threshold", "Description"
].values[0]

"""Creating object using the variables from excel"""
game_rules = CyberCityGameRules(
    turns=turns,
    budget={"defender": budget_defender, "attacker": budget_attacker},
    actions_per_turn=actions_per_turn,
    defender_turn={
        "description": defender_turn_desc,
        "success_rate": defender_turn_success_rate,
    },
    attacker_turn={
        "description": attacker_turn_desc,
        "success_rate": attacker_turn_success_rate,
    },
    compromise_threshold=compromise_threshold,
)
