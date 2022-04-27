import time


def time_decorator(fn):
    print("Этот код будет выведен в момент декорирования функции")

    def wrapper(*args, **kwargs):
        print("Этот код будет выполняться перед каждым вызовом функции")

        t1 = time.time()
        result = fn(*args, **kwargs)
        #ime.sleep(3)
        t2 = time.time()

        print("Этот код будет выполняться после каждого вызова функции")
        return (t2-t1), result
    return wrapper


@time_decorator # pow_ = time_decorator(pow_)
def pow_(a, n):
    #print(pow(a,n))
    return pow(a, n)


if __name__ == "__main__":
    print(pow_)
    print("=" * 25)

    print(pow_(5, 2))
    print("=" * 25)

    print(pow_(4, 4))
