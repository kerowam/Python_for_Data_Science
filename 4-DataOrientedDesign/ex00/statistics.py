from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    def get_median(values: list[Any]) -> Any:
        size = len(values)
        middle = size // 2

        if size % 2 == 1:
            return values[middle]
        return (values[middle - 1] + values[middle]) / 2

    if len(args) == 0:
        for _ in kwargs.values():
            if _ in ["mean", "median", "quartile", "std", "var"]:
                print("ERROR")
        return

    data = sorted(args)

    mean = sum(data) / len(data)
    variance = sum((value - mean) ** 2 for value in data) / len(data)

    for operation in kwargs.values():
        if operation == "mean":
            print(f"mean : {mean}")
        elif operation == "median":
            print(f"median : {get_median(data)}")
        elif operation == "quartile":
            q1 = len(data) // 4
            q3 = (len(data) * 3) // 4
            q_25 = data[q1]
            q_75 = data[q3]
            print(f"quartile : {[float(q_25), float(q_75)]}")
        elif operation == "std":
            print(f"std : {variance ** 0.5}")
        elif operation == "var":
            print(f"var : {variance}")
