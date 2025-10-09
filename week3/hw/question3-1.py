import time
number_list = [154, 44, 98, 75, 14, 63, 10, 51, 24, 86, 37]

def bubble_sorting(numbers: list):
    """
    We want to sort a list of numbers using bubble sort.
    Bubble sort start from left and compare a number with another number,
     if the first number is greater than the second, it changes its
     place with second number.
    In this function, we use a nested for loop. Outer loop starts
     from first number, then inner loop starts from first number too,
     and it continues until first number keeps a right place. Then
     outer loop starts again from next number, then inner loop starts
     to compare that with other numbers.
    We can say outer loop run to iterate each number, and the inner
     one runs to comparing.
    """
    n = len(numbers)

    for i in range(n):
        for j in range(n - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

start = time.time()
print(bubble_sorting(number_list))
end = time.time()

print(end - start)