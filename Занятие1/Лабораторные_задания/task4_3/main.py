from itertools import repeat


# def task():
#     a = 10
#     for num in range(4):
#         for num in repeat(a):  # TODO повторить переменную a 4 раза
#             print(num)

def task():
    a = 10
    for num in range(4):    # TODO повторить переменную a 4 раза
        print(list(num, repeat(4)))


if __name__ == "__main__":
    task()
# return list(map(round, my_floats, repeat(2)))