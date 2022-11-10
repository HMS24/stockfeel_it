# fibonacci 縮寫 fib
fib_cache = {
    # 第 n 項: fib_num
    0: 0,
    1: 1,
}


def fib_of(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError(f'"{n}" is not positive integer number!')

    try:
        return fib_cache[n]
    except KeyError:
        prev = fib_cache[0]
        fib_num = fib_cache[1]

        for i in range(2, n+1):
            prev, fib_num = fib_num, prev + fib_num

            fib_cache[i] = fib_num

        return fib_cache[n]


def permutate(m, n):
    result = 1

    for _ in range(n):
        result *= m
        m -= 1

    return result


def to_digits(num):
    if num == 0:
        return []

    return [num % 10] + to_digits(num // 10)


if __name__ == '__main__':
    # test fib_of
    assert fib_of(10) == 55

    # test permutate
    assert permutate(5, 5) == 120

    # test to_digits
    from unittest import TestCase

    TestCase().assertListEqual(
        to_digits(55),
        [5, 5],
    )
