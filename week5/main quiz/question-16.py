#
# تابعی بنویسید که لیستی از اعداد را بگیرد و
# آن هارا بر اساس مجموع ارقام هر عدد به ترتیب  صعودی مرتب کند .
# اگر مجموع دو عدد برابر بود ، خود عدد کوچک تر اول بیاید .
#
# Input: [91, 23, 14, 101, 55]
# output: [101, 14, 23, 55, 91]
#
# چون مجموع ارقام به ترتیب 2 ، 5، 5، 10، 10 است .

Input = [91, 23, 14, 101, 55]

def sort_numbers(lst):
    """
    We want to sort our list by sum of digits of each number.
      so we iterate through the list and make them string then
      take sum of digits. then put each number with their sum(tuple)
      into a new list. then we append every index1 of each tuple
      into a newer list.
    """
    numbers = []
    for number in lst:
        total = 0
        for num in str(number):
            total += int(num)

        numbers.append((total, number))
    numbers.sort()
    sorted_numbers = []
    for item in numbers:
        sorted_numbers.append(item[1])
    return sorted_numbers

print(sort_numbers(Input))