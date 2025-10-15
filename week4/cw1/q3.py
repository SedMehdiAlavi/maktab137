def enforce_types(type1, type2):
    def decorator(func):
        def wrapper(arg1, arg2):
            if type1 == type(arg1) and type2 == type(arg2):
                result = func(arg1, arg2)
                return result

            else:
                raise TypeError("Type mismatch")

        return wrapper
    return decorator


@enforce_types(int, int)
def add(a, b):
    return a + b

@enforce_types(str, int)
def repeat_message(message, times):
    for _ in range(times):
        print(message)


print(add(5,10))
repeat_message("hello", 3)