def task() -> list:
    temp_tuple = (0, 36.6, 100)
    #return [(i*9)/5+32 for i in temp_tuple]
    return lambda i: (i * 9) / 5 + 32 temp_tuple

       # return ("температура по Цельсию", (lambda i: ((i*9/5)+32)),"=","температура по Фаренгейту")


if __name__ == "__main__":
    print(task())
