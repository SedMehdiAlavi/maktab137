while True:
    name: str = input("Enter Your Full Name: ")
    vowels = "eaiouEAIOU"
    letters: list = []
    name: str = name.replace(" ", "")

    for x in name:
        if x in vowels:
            letters.append(".")

        else:
            letters.append(x)

    name = "".join(letters)
    reverse_name = name [::-1]
    print(reverse_name)

