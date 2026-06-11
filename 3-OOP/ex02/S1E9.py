from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for all characters."""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Initialize a character."""
        self.first_name = first_name
        self.is_alive = is_alive
        pass

    def die(self):
        """
        Kill the character.
        This method sets the is_alive attribute to False.
        """
        self.is_alive = False


class Stark(Character):
    """Class representing a Stark character."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Stark character."""
        super().__init__(first_name, is_alive)
