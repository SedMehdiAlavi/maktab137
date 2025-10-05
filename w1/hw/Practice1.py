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

#  for vowel in vowels
# print(name)
# for
# new_name: str = name.replace(" ", "")
# new_name: str = new_name.replace("e", ".")
# new_name: str = new_name.replace("a", ".")
# new_name: str = new_name.replace("i", ".")
# new_name: str = new_name.replace("o", ".")
# new_name: str = new_name.replace("u", ".")
# new_name: str = new_name.replace("E", ".")
# new_name: str = new_name.replace("A", ".")
# new_name: str = new_name.replace("I", ".")
# new_name: str = new_name.replace("O", ".")
# new_name: str = new_name.replace("U", ".")
# reverse_name: str = new_name [::-1]
# print(reverse_name)
