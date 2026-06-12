def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return x raised to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure that keeps applying function to the stored value."""
    count = x

    def inner() -> float:
        """Apply the stored function and update the captured value."""
        nonlocal count
        count = function(count)
        return count

    return inner
