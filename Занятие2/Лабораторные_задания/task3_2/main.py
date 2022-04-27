def min_len_check(fn: str):
    if len(str(fn)) > len(str(10)):
        if len(str(fn)) < len(str(10)):
            raise ValueError("Строка слишком короткая")

            def wrapper():
                result = fn()
                return result


            return wrapper


@min_len_check# TODO задекорировать функцию
def some_func(str_arg: str):
    ...


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
