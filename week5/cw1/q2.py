def number_etela(n):
    if n <= 0:
        print("the intreded number must be positive!!!!!!")
        return
    for i in range(1, n + 1):
        print(i)
    dobarabr = lambda x: x * 2
    tavan2 = lambda x: x ** 2
    result_dict = {}
    for i in range(1, n + 1):
        if i % 2 == 0:
            result_dict[i] = tavan2(i)
        else:
            result_dict[i] = dobarabr(i)
    values_list = list(map(lambda x: x, result_dict.values()))
    print(values_list)

number_etela(55)
