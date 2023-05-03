from typing import List

from .objects import Role

class Game():
    def __init__(self,
                hacker: Role = Role("hacker", 5000),
                defender: Role = Role("defender", 5000),
                districts: List = []
                )-> None:
        self.hacker: Role = hacker
        self.defender: Role = defender
        self.districts: List = districts

    @property
    def data_str(self) -> str:
        out = ""
        out += "Hacker\n"
        out += str(self.hacker) + "\n\n"
        out += "Defender\n"
        out += str(self.defender) + "\n\n"
        out += "Districts\n"
        out += str(self.districts) + "\n\n"
        return out
