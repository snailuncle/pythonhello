def print2(f):
    def wrapper(*args, **kwargs):
        print(f.__name__)
        return f(*args, **kwargs)
    return wrapper


@print2
def aandb(a, b):
    return (a + b)


num = aandb(1, 2)
print(num)
