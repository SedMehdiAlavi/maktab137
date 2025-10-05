while True:

    number: int = int(input("Enter a number: "))
    i = 1
    divisors: list = []

    while i < number:

        if number % i == 0:
            divisors.append(i)
            i += 1

        else:
            i += 1

# قسمت زیر صرفا جهت نمایش بهتر خروجی میباشد

    new_divisors = str(divisors)
    new_divisors = new_divisors.replace(" ", " + ")
    new_divisors = new_divisors.replace("[", "")
    new_divisors = new_divisors.replace("]", "")
    new_divisors = new_divisors.replace(",", "")

    print(new_divisors, ' = ',sum(divisors))


    if sum(divisors) == number:

        print('Yes')

    else:
        print('No')