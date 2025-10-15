# تابعی بنویسید که یک دیکشنری به شکل زیر دریافت کند .
#
# input_dict = {
# "apple": "fruit",
# "banana": "fruit",
# "carrot": "vegetable",
# "tomato": "vegetable",
# “laptop”: “technology”
# }
#
# و خروجی را برعکس کند به صورتی که کلید ها و مقدار ها عوض شوند،
# اما اگر چند کلید مقدار یکسان داشتند فقط در خروجی لیست شوند.
#
# Output:
# {
# "fruit": ["apple", "banana"],
# "vegetable": ["carrot", "tomato"],
# “technology”: “laptop”
# }

input_dict = {
    "apple": "fruit",
    "banana": "fruit",
    "carrot": "vegetable",
    "tomato": "vegetable",
    "laptop": "technology"
}

def reversed_dict(dictionary):
    new_dict = {}
    for key in dictionary:
        value = dictionary[key]

        if value not in new_dict:
            new_dict[value] = key

        else:
            if type(new_dict[value]) == list:
                new_dict[value].append(key)

            else:
                new_dict[value] = [new_dict[value], key]
    return new_dict

print(reversed_dict(input_dict))