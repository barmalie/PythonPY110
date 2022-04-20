def filter_positive_number(x: int) -> bool:
    return x > 0  # функция возвращает только True или False


if __name__ == "__main__":
    #result = filter(filter_positive_number, [-2, -1, 0, 1, -3, 2, -3])
    result = filter(lambda: x > 0)
    # TODO заменить filter_positive_number на lambda функцию
    print(list(result))  # Возвращается итерируемый объект, поэтому приводим к списку
