from itertools import count


def task():
    counter = count(100, 10)

    for _ in range(10):  # распечатать первые 5 натуральных чисел
        print(next(counter))  # TODO как получить от итератора следующий объект?


if __name__ == "__main__":
    task()
