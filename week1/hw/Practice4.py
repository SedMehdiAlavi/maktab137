while True:

    name: str = input("what's your name? ")
    score: int = int(input("Please enter youre score: "))

    if score >= 90:
        print(f"{name} : PERFECT!", '\n')

    elif score >= 70 and score < 90:
        print(f"{name} : Good.", '\n')

    elif score < 70:
        print(f"{name} : Need more Progress :) ", '\n')