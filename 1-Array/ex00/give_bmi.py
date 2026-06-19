import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """Calculate BMIs for parallel ``height`` and ``weight`` lists.

    Raise a ``ValueError`` when lists have different lengths.
    Raise a ``TypeError`` when elements are not ``int`` or ``float``.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length")

    for h in height:
        if isinstance(h, bool) or not isinstance(h, (int, float)):
            raise TypeError("Height list must contain only int or float value")
    for w in weight:
        if isinstance(w, bool) or not isinstance(w, (int, float)):
            raise TypeError("Weight list must contain only int or float value")

    h_arr = np.array(height)
    w_arr = np.array(weight)
    bmi = w_arr / (h_arr ** 2)
    return bmi.tolist()


def apply_limit(
    bmi: list[int | float],
    limit: int,
) -> list[bool]:
    """Return booleans for values in ``bmi`` greater than ``limit``.

    Raises TypeError when bmi elements are not numeric or when limit is not
    an integer.
    """
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")

    for b in bmi:
        if isinstance(b, bool) or not isinstance(b, (int, float)):
            raise TypeError("BMI list must contain only int or float values")

    return [b > limit for b in bmi]
