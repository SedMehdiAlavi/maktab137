def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))



        else:
            flat_list.append(item)

    return flat_list

my_list = [1,[2,3],[4,[5,6]],7]
result = flatten(my_list)
print(result)