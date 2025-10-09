# def jjj(*args):


def enforce_types(func):
    def wrapper(*args, **kwargs):
        if isinstance(a, int) or isinstance(a, str) and isinstance(b, int):
            pass
        else:
            raise TypeError
    return wrapper

@enforce_types(int, int)
def add(a, b):
    return a + b

@enforce_types(str, int)
def repeat_message(message, times):
    for _ in range(times):
        print(message)


print(add(5, 10))
repeat_message("hello", 3)