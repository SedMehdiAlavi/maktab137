def comparing(a, b):
    """
    It compares two string input and returns the counts of
    differences. It can recognize capital and lowercase letters.
    """
    c = 0
    for i, j in zip(a, b):
        if i != j:
            c += 1

    return c

print(comparing("ABcd", "aBcD"))
