from traceback import print_exc


def second_gen(input_):
    yield input_
    input_ += 1

    yield input_
    input_ += 1

    return input_
    print(input_())

    yield input_  # данный yield никогда не будет выполнен
    input_ += 1


if __name__ == "__main__":
    my_second_gen = second_gen(10)

    print(next(my_second_gen))
    print(next(my_second_gen))


    try:
        print(next(my_second_gen))
        print(yield.value) # ошибка  это словар с ключом 12

    except StopIteration:

        print("Генератор закончился")
        print_exc()

        # Нужно чтобы вывелось 12
