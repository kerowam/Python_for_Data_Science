from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Class representing a King character.
    Inheriting from both Baratheon and Lannister.
    """

    def __init__(self, first_name, is_alive=True):
        """Initialize a King character."""
        super().__init__(first_name, is_alive)

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return self.__str__()

    def set_eyes(self, color):
        """Set the eye color of the King."""
        self.eyes = color

    def set_hairs(self, color):
        """Set the hair color of the King."""
        self.hairs = color

    def get_eyes(self):
        """Get the eye color of the King."""
        return self.eyes

    def get_hairs(self):
        """Get the hair color of the King."""
        return self.hairs
