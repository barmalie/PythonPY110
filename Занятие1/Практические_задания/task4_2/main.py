from itertools import count


def task():
    iterator_numbers = count(1, 1)
    #numbers = [i ** 2 for i in iterator_numbers if i % 2 == 0]  # TODO заменить на map и filter
    numbers = list(map(i**2, filter,count, iterator_numbers))
    for num in numbers:  # TODO напечатать первые 10 чисел
        print(num)  # TODO с помощью next получать следующий элемент от итератора


if __name__ == "__main__":
    task()
# map + filter
# some_list = [i - 10 for i in range(20)]
# def f2(x): return x**2
# def f(x): return x > 0
#
# print(some_list)
# print(list(map(f2, filter(f, some_list))))