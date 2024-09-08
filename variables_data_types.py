# print("There once was a man named John, ")
# print("he was 35 years old.")


# character_name = "John"
# character_age = "35"
# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old.")


# Working With String
# phrase = "TNT Academy"
# print(phrase + " is cool")
# print(phrase[0])
# print(phrase.index("T"))
# print(phrase.replace("TNT", "Thuan"))

# # Working With Number
# my_number = 5
# # print(my_number + " my favorite number") // error 
# print(str(my_number) + " my favorite number")
# print(round(my_number))
# # import math => lots of functions

# Get inputs from users
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = 0
# result = float(num1) + float(num2)
# print(result)

# name = input('What is your name?\n')     # \n ---> newline  ---> It causes a line break
# print(name) 

# val = input("Enter your value: ")
# print(val)

# Lists
# friends = ["Kevin", "Karen", "Jim", "Katy", "Justin"]
# friends[2] = "Mike"
# print(friends[2]) #Mike
# print(friends[-1])
# print(friends[1:3])

# List Function
# lucky_number = [4, 8, 15, 16, 23, 42]
# lucky_number.reverse()
# print(lucky_number)
# friends = ["Kevin", "Karen", "Jim", "Katy", "Justin"]
# friends.insert(1, "Kelly")
# friends.remove("Jim")
# friends.clear()
# friends.pop() #pop all but got rid of the last element inside
# friends2 = friends.copy()
# print(friends)

#Tuples
# coordinates = (4,5) # [(4,5), (6,7), (45,78)]
# coordinates[1] = 10
# print(coordinates) #error

# def say_hi(name):
#     print("hello " + name)

# say_hi("Mike")

# Return Statement
# def cube(num):
#     return num*num*num

# result = 0
# result = cube(4)
# print(result)

# If statements
# is_male = True
# is_tall = True
# if is_male and is_tall:
#     print ("You are a tall male")
# elif is_male and not(is_tall):
#     print("you r a short male")
# elif not(is_male) and is_tall:
#     print ("you r not a male but are tall")
# else:
#     print ("you r either not male or not tall or both")

# If Statements And Comparision
# def max_num(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(max_num(300,15,19))

# Building a better Calculator
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")

# Dictionaries
# monthConversions = {
#     0: "January",
#     1: "Feburary",
#     10: "March",
#     "Apr": "April",
#     "May": "May"
# }

# print(monthConversions.get("Luv", "Not a valid Key")) #if not found, get a second value
# print(monthConversions.get("Apr"))

# While Loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# print("Done with loop")

# For Loops
# friends = ["Jim", "Karen", "Kevin"]

# for index in range(len(friends)):
#     print (friends[index])

# Exponent Function
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result

# print(raise_to_power(3,2))

# 2D Lists and Nested Loops
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]
# ]
# for row in number_grid:
#     for col in row:
#         print(col)

# Try/Except
# try:
#     answer = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("invalid input")

# Reaing Files
# employee_file = open("employee.txt", "r")
# print(employee_file.readable()) # return true or false
# print(employee_file.read())
# print(employee_file.readline()) # read just 1 line - return list
# employee_file.close() 

# Classes and Objects
from Student import Student
student1 = Student("Jim", "Business", 3.1, False)
print(student1.gpa)
print(student1.on_honor_roll())