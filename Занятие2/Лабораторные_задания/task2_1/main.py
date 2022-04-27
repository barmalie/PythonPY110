from itertools import count


def task():
    num = 2 ** 0  # 1
    yield num

    for num in count(1, 1):
        yield (i ** 2 for i in num) # TODO с помощью yield вернуть оставшиеся степени двойки до бесконечности


if __name__ == "__main__":
    numbers = task()

    for _ in range(11):
        print(next(numbers))
