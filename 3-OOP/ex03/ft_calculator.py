class calculator:
    """
    A simple calculator class that performs basic arithmetic \
    operations on a list of values.
    """
    def __init__(self, vector: list):
        """Initialize the calculator with a list of values."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a value to each element in the list."""
        if isinstance(object, (int, float)):
            self.vector = [x + object for x in self.vector]
            print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply each element in the list by a value."""
        if isinstance(object, (int, float)):
            self.vector = [x * object for x in self.vector]
            print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a value from each element in the list."""
        if isinstance(object, (int, float)):
            self.vector = [x - object for x in self.vector]
            print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide each element in the list by a value."""
        if object == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        if isinstance(object, (int, float)):
            self.vector = [x / object for x in self.vector]
            print(self.vector)
