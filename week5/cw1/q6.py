import random

while True:
    numbers = [0,1,2,3,4,5,6,7,8,9]
    code = random.sample(numbers, 4)
    count = 0

    while True:
        guess = input("guess the password(xxxx): ")
        if len(guess) != 4 or not guess.isdigit():
            print("invalid input try again")
            continue

        guess = [int(i) for i in guess]
        count += 1

        right_place = 0
        wrong_place = 0

        for i in range(4):
            if guess[i] == code[i]:
                right_place += 1
            elif guess[i] in code:
                wrong_place += 1

        if right_place == 4:
            print(f"you guessed correctly after{count} trying ")
            print("here is your bastani 🍦🍦🍦🍧🍧🍨🍨🍨")
            break
        else:
            print(right_place, "are in right place.")
            print(wrong_place, "are in wrong place.")

    again = input("wanna play again ?(y/n): ").lower()
    if again != "y":
        break
print("WRITTEN BY PARSA")
