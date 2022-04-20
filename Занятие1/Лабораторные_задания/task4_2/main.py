import itertools


def task():
    a = (1, 2, 3)
    repeater = itertools.cycle(a)  # TODO бесконечно повторяем элементы кортежа
    for _ in range(10):
        print(next(repeater))


if __name__ == "__main__":
    task()



# keys = [1, 2, 3, 4, 5, 6]
# values = ['a', 'b', 'c', 'd']
#
# dict_ = dict(zip(keys, cycle(values)))
# print(dict_)