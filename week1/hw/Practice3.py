while True:

    temperature: int = int(input("Enter the temperature: "))

    if temperature < 10:
        print("It's Cold!", '\n')

    elif temperature >= 10 and temperature <= 25:
        print("It's Normal.", '\n')

    elif temperature > 25:
        print("It's Hot!", '\n')