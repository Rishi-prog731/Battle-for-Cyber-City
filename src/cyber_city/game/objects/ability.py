"""
Here the class for the abilities the plays can use are defined.
"""

class Ability():
    """The Ability Class"""
    def __init__(self, name: str, cost: int, modifer: int) -> None:
        """
        Initialize a new Ability object.

        Args:
            name (str): name of the ability
            cost (int): cost of the ability
            modifer (int): modifer of the compromised percentage for ability
        """
        self.name: str = name
        self.cost: int = cost
        self.modifier: int = modifer