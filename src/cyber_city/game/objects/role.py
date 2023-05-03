class Role():
    def __init__(self, name: str, budget: int) -> None:
        self.name: str = name
        self.budget: int = budget
        self.abilities: list = []
    
    def __str__(self) -> str:
        out = ""
        out += f"Name:\n\t {self.name}\n"
        out += f"Budget:\n\t {self.budget}\n"
        out += "Abilities:\n\t"
        for ability in self.abilities:
            out += f"{ability.name}, "
        return out
