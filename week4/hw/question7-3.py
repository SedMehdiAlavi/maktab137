def calculator(num1, num2, /, *, oper: str):
    """
    It's a simple calculator. The first couple arguments are
    positional only, you can't change their position, be careful
    when calling, specially when operator is division. The third
    argument are keyword only, you have to use it by keyword
    when calling.
    """

    if oper == '+':
        return num1 + num2

    elif oper == '-':
        return num1 - num2

    elif oper == '*':
        return num1 * num2

    elif oper == '/':
        return num1 / num2


print(calculator(2, 3, oper = '*'))