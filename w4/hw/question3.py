def repeat_counter(lst: list):
    """
    This function is used to take a list and return an element with
     the most repeating, So it counts duplication of each element
     and returns the most duplicated element as key, and the number
     of times the element is repeated as value, in a dictionary.
    """
    counter = {item: lst.count(item) for item in lst}
    maximum = max(counter ,key = counter.get)
    result = {maximum: counter[maximum]}
    return result

list1 = [1,3,5,7,9,3,4,8,3,4,1,3,3,9,3]
print(repeat_counter(list1))
