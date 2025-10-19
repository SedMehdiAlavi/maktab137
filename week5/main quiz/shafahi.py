input_dict = {
"apple": "fruit",
"banana": "fruit",
"carrot": "vegetable",
"tomato": "vegetable",
"laptop": "technology"
}

def reversed_dict(input):
    new_dict = {}
    for key, value in input.items():
        if value in new_dict:
            if isinstance(new_dict[value], list):
                new_dict[value].append(key)
            else:
                new_dict[value] = [new_dict[value], key]

        else:
            new_dict[value] = key
    return new_dict

print(reversed_dict(input_dict))

def remove_duplicates(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)

    return new_lst

print(remove_duplicates([1,2,3,4,5,6,7,8,9,5,6,7,8,9]))