# For loop -  Repeat for a known range/items
# for i in range(5):
#     print(i)

# colors = ["red", "blue", "green"]
# for color in colors:
#     print(color)

# While - Repeat while a condition is true
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# password = ""
# while password != "1234":
#     password = input("Enter the password: ")
# print("Access granted!")


# Tasks
# 1)Print Numbers (For Loop)
# for i in range(1, 11):
#     print(i)

# 2)Sum of Numbers (For Loop)
# a = 0
# for i in range(5):
#     a += i
#
# print(a)

# 3)Count Down (While Loop)
# i = 5
# while i > 0:
#     print(i)
#     i -= 1

# 4) Print Each Character (For Loop)
# text = 'python'
# for i in text:
#     print(i)

# 5)Even Numbers (While Loop) 1-10
# i = 0
# while i <= 10 and i % 2 == 0:
#     print(i)
#     i += 2

# 6) Reverse a Number (While Loop) 1234 - 4321
# number = 1234
# reversed_number = 0
#
# while True:
#     first_number = number % 10
#     second_number = number % 100 // 10
#     third_number = number % 1000 // 100
#     fourth_number = number // 1000
#
#     reversed_number = (first_number * 1000 +
#                        second_number * 100 +
#                        third_number * 10 +
#                        fourth_number)
#     break
#
# print("Reversed number:", reversed_number)

# 7) Number Pyramid (For Loop)
# 1
# 12
# 123
# 1234

# rows = 5
#
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
