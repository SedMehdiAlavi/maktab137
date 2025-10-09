# Define a function that asks the user for two numbers, validates they’re numeric, and prints their sum with formatted output.
#
# Create a function that takes a name as input, trims whitespace, checks for empty input, and greets the user with proper capitalization.
#
# Write a function that asks for the radius of a circle, ensures it’s a positive number, and calculates both area and circumference with two decimal precision.
#
# Build a function that receives multiple item prices from the user, handles invalid entries, and returns the total cost rounded to two decimals.
#
# Design a function that asks for the user’s age, checks if it’s within a realistic range (e.g., 0–120), and calculates how many years until they turn 100.
#
# Make a function that converts Celsius to Fahrenheit, validates the input, and handles edge cases like extreme temperatures.
#
# Write a function that asks for a number, confirms it’s an integer, and determines whether it’s even, odd, or zero.
#
# Create a function that asks for a word, ensures it’s alphabetic, and prints it in reverse with a character count.
#
# Define a function that takes a sentence from the user, strips extra spaces, and counts the number of words and characters.
#
# Build a function that asks for a number and prints its multiplication table up to 10, formatted in aligned columns.
#
# To see these concepts in action and deepen your understanding, check out these tutorials:
#
# User input in Python is easy + exercises ⌨️ — covers input basics and builds up with examples like Mad Libs and shopping cart totals.
#
# 10 Simple Python exercises involving input/output (for ... — walks through real-world scenarios like calculating distance and handling purchases.
#
# Python Exercises - User Input and Print (Daily Python Practice ... — great for daily drills and building input/output fluency.
#
# Python Practice Problem - 02 Input — includes 12 progressively harder problems with input validation and logic.
#
# [Interactive Coding Exercise] Input Function — explains how to use input() effectively and test your code interactively.


# def jame_2adad():
#     while True:
#         a = input("avlin adad ro vared kon: ").strip()
#         b = input("dovomin adad ro vared kon: ").strip()
#         try:
#             a = float(a)
#             b = float(b)
#             majmoe = a + b
#             print("jame = {:.2f}".format(majmoe))
#             break
#         except ValueError:
#             print("vorodi namotabar. vorodi dorst benevis")
#             return jame_2adad
#
# print(jame_2adad())

# def name():
#     name = input("Enter your name: ")
#     name = name.replace(" ", "")
#
#     if not name.isalpha():
#         print("Enter a valid name")
#         return "Invalid input"
#
#     return f"Hello {name}"
#
# print(name())

# def radius():
#     radius = int(input("enter the radius of the circle: "))
#
#     if radius <= 0:
#         print(radius * -1)
#         return "invalid radius"
#     area = (radius ** 2) * 3.14
#     return {area}
#
#
# print(radius())

# def charkhe_hesabi():
#     pi = 3.14
#     while True:
#         r = input("shoa ra vared konid: ").strip()
#         try:
#             r = float(r)
#             if r <= 0:
#                 print("shoa bayad ,osbar bashad na manfi nadan.")
#                 continue
#             p = pi * r * r
#             s = 2 * pi * r
#             print("mohit = {:.2f}".format(p))
#             print("s = {:.2f}".format(s))
#             break
#         except ValueError:
#             print("adad namotabar, dobare talash konid.")
#             return charkhe_hesabi
#
# print(charkhe_hesabi())

# def item():
#     item1 = input("enter item 1 price: ")
#     item2 = input("enter item 2 price: ")
#
#     if item1 == "" or item2 == "":
#         print("your choice is not valid")
#         return "invalid input"
#
#     item1 = int(item1)
#     item2 = int(item2)
#     total_cost = item1 + item2
#     return total_cost
#
# print(item())

#
# def jam_kol_ghimat_ha():
#     while True:
#         n = input("tedad kalaharo vared konid: ").strip()
#         if not n.isdigit():
#             print("ye adad sahih vared konid: ")
#             continue
#         n = int(n)
#         jam = 0.0
#         for i in range(n):
#             while True:
#                 g = input("gheimat kala ra {} vared konid: ".format(i+1)).strip()
#                 try:
#                     g = float(g)
#                     if g < 0:
#                         print("gheimat nemitavanad manfi bashad: ")
#                         continue
#                     jam += g
#                     break
#                 except ValueError:
#                     print("gheimar namotabar ast, adad vared konid:")
#         jam_round = round(jam, 2)
#         print("jame kol = {:.2f}".format(jam_round))
#         return jam_round
#
# jam_kol_ghimat_ha()


#
# def range(num):
#     if 0 < num < 100:
#         return f"{100 - num} years remaining"
#
#     else:
#         return "Mordi badbakht"
#
#
# print(range(120))

def celsius_be_fahrenheit():
    while True:
        c = input("dama be Celsius ra vared konid: ").strip()
        try:
            c = float(c)
            if c < -273.15:
                print("dama zir (-273.15°C) momken nist.")
                continue
            f = c * 9/5 + 32
            print("{:.2f}°C = {:.2f}°F".format(c, f))
            break
        except ValueError:
            print("lotfan yek adad motabar vared konid.")

print(celsius_be_fahrenheit())

