def nested_sum(nums: list):
    """
    It calculates the sum of all elements in a nested list. So it's
     recursive function. It iterates through the list and when an
     element is found as a list, it iterates through this inner
     list and finally returns the sum of all elements.
    """
    total = 0
    for num in nums:
        if type(num) == list:
            total += nested_sum(num)

        else:
            total += num

    return total

numbers = [1, [2, 3], [4, [5]]]

print(nested_sum(numbers))