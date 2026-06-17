from typing import Any


def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """
        Inner function that keeps track of the number of \
            calls to the decorated function.
        """
        def limit_function(*args: Any, **kwds: Any):
            """Function that checks if the limit has been reached \
                before calling the decorated function."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times.")
        return limit_function

    return callLimiter
