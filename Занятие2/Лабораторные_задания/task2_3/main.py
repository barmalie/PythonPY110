def pow_gen(base: int):
    def count(*args, step: float = 1):
        counter = start_number
        while True:
            yield counter
            counter += step

    pow_gen = count(100, 10)


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
