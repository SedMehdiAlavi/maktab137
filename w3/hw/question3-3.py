import time
number_list = [44, 98, 75, 14, 154, 63, 10, 51, 24, 86, 37]

def merge(numbers1: list, numbers2: list):
    """
    We want to merge two sorted lists into a new list. 'i' and 'j'
     are the number of index of each list we iterate over. In every
     element, we compare numbers and put the smaller number into
     the right plce.
    """
    len1 = len(numbers1)
    len2 = len(numbers2)
    numbers3 = []
    i = j = 0

    while i < len1 and j < len2:
        if numbers1[i] < numbers2[j]:
            numbers3.append(numbers1[i])
            i += 1

        else:
            numbers3.append(numbers2[j])
            j += 1

    numbers3 += numbers1[i:]
    numbers3 += numbers2[j:]

    return numbers3

def merge_sorting(numbers: list):
    """
    We want to split a disorganized list into two lists, and we
     continue to do that till catch lists with length 1 element.
     So it's a recursive function.
    After that, we can call merge() function to merge them in order.
    """
    if len(numbers) == 1:
        return numbers

    else:
        middle = len(numbers) // 2
        left = numbers[:middle]
        right = numbers[middle:]

    left = merge_sorting(left)
    right = merge_sorting(right)

    return merge(left, right)


start = time.time()
print(merge_sorting(number_list))
end = time.time()
print(end - start)