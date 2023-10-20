def square(x: int | float) -> int | float:
    return x * x


def pow(x: int | float) -> int | float:
    return x**x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:

        nonlocal count
        ret = x
        count += 1
        for _ in range(count):
            ret = function(ret)
        return ret
    return inner
