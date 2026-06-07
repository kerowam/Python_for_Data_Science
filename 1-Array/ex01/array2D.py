import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''Return a slice of the 2D list ``family`` from ``start`` to ``end``.'''
    if not isinstance(family, list):
        raise TypeError("Family must be a list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers")
    lengths = [len(row) for row in family]
    if len(set(lengths)) != 1:
        raise ValueError("All rows in family must have the same length")
    arr = np.array(family)
    print(f'My shape is : ({arr.shape[0]}, {arr.shape[1]})')
    new_arr = arr[start:end].tolist()
    print(f'My new shape is : ({len(new_arr)}, {len(new_arr[0]) if new_arr else 0})')
    return new_arr
