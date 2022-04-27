def positive_check(fn):
    def wrapper(arg):
       # try:
       #     arg < 0
       # except:
        if not arg > 0:
           raise ValueError("Аргумент функции не является положительным числом")
           # TODO написать проверку положительности аргумента arg

        result = fn(arg)
        return result

    return wrapper


@positive_check
def some_func(num: int):
    pass


if __name__ == "__main__":
    some_func(5)  # всё хорошо

    some_func(-5)  # должна быть вызвана ошибка ValueError
