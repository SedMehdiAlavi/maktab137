import time
number_list = [44, 98, 75, 14, 154, 63, 10, 51, 24, 86, 37]

def quick_sorting(numbers: list):
    if len(numbers) <= 1 :
        return numbers

    pivot = numbers[0]
    smaller = []
    greater = []
    for number in numbers:
        if number < pivot:
            smaller.append(number)
        elif number > pivot:
            greater.append(number)

    return quick_sorting(smaller) + [pivot] + quick_sorting(greater)

start = time.time()
print(quick_sorting(number_list))
end = time.time()

print(end - start)

def quick_sorting2(numbers: list, low, high):
    if low < high:
        pivot = low
        i = low
        j = high

        while i < j:
            while numbers[i] <= numbers[pivot] and i < high:
                i += 1

            while numbers[j] >= numbers[pivot] and j > low:
                j -= 1

            if i < j:
                numbers[i], numbers[j] = numbers[j], numbers[i]

        numbers[j], numbers[pivot] = numbers[pivot], numbers[j]

        quick_sorting2(numbers, low, j - 1)
        quick_sorting2(numbers, j + 1, high)

    return numbers

start = time.time()
print(quick_sorting2(number_list, 0, len(number_list) - 1))
end = time.time()

print(end - start)