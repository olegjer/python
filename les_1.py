# ---------------practice code -------------
# x = 1
# y = 2
# print(x, y)
# print("Hello, World!")

# if 5 > 2:
#     print("Five is greater than two!")
# if 5 > 2:
#     print("Five is greater than two!")

# x = 5
# y = "John"
# print(x)
# print(y)

# x = 4       # x is of type int
# x = "Behn"  # x is now of type str
# print(x)

# x = 5
# y = "John"
# print(type(x))
# print(type(y))


# x = "awesome"
# print("Python is " + x)

# x = 5
# y = "John"
# print(x + y) #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# # Python Program - Get String Input from User
# str = input("Enter any string: ")
# print(str, type(str))

# num = int(input("Enter an Integer: "))
# print(num,  type(num))


# # Python Program - Get Float Input from User
# num = float(input("Enter a float value: "))
# print(num,  type(num))
# ------------end of practice code---------------

# Write a Python program to print the result of the following operations.
# print(-5 + 8 * 6 )
# print( (55+9) % 9 )
# print( 20 + -3*5 / 8  )
# print( 5 + 15 / 3 * 2 - 8 % 3 )


# Write a Python program to divide two numbers, using the input from the user, and print the result on the screen
# Input the first number: 6
# Input the second number: 2
# The division of the first number and the second number is: 3

# num1 = int(input(" Input the first number: "))
# num2 = int(input(" Input the second number: "))
# result = num1/num2
# print("The division of the first number and the second number is: ", result)


# num1 = int(input("input first number: "))
# num2 = int(input("input second number: "))
# num3 = int(input("input third number: "))

# ------------------ All numbers are uqual.
# if num1 == num2 and num2 == num3:
#     print("all numbers are equal")


# -------------All numbers are different
# elif num1 != num2 and num2 != num3 and num3 != num1:
#     print("all numbers are different")

# --------Neither all equal or different
# else:
#     print("Neither all are equal or different")

# -----------------------------------Testing code for practice---------------
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#     print(x)

# for x in "cherry":
#     print(x)

# for x in range(2, 10, 2):
#     print(x)

# print("end")
# ---------------------------------------end of code----------------

# ----------Fibonacci series between 0 to 50.

# def fib(i):
#     if i == 0:
#         return 0
#     elif i == 1:
#         return 1
#     else:
#         return fib(i - 2) + fib(i - 1)


# for x in range(11):
#     print(fib(x))

# ------the multiplication table -----------

# num1 = int(input("input number: "))

# for x in range(1, 11):
#     print(f"{num1} x {x} = {x*num1} ")

# --------------practice code---------------

# myList = ["red", "green", "blue"]
# print(myList)

# myList = ["red", "green", "blue", "red", "blue"]
# print(len(myList))

# myList = ["red", "green", "blue"]
# print(len(myList))

# myList1 = ["red", "green", "blue"]
# myList2 = [1, 5, 7, 9, 3]
# myList3 = [True, False, False]
# print(myList1)
# print(myList2)
# print(myList3)

# myList1 = ["abc", 34, True, 40, "male"]
# print(myList1)

# myList = ["red", "green", "blue"]
# print(type(myList))
# myList[0] = "Yellow"
# myList.sort()
# print(myList)
# myList.append("Orange")
# myList.pop(1)

# for x in myList:
#   print(x)


# ------- Python program to find sum of elements in list
# total = 0
# i = 0

# # creating a list
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Iterate each element in list
# # and add them in variable total
# while (i < len(list1)):
#     total = total + list1[i]
#     i = i + 1

# # printing total value
# print("Sum of all elements in given list: ", total)

# ------- Python program to get average of a list
# def Average(lst):
# 	return sum(lst) / len(lst)

# # Driver Code
# lst = [20, 30, 25, 35, -16, 60, -100]
# average = Average(lst)

# # Printing average of the list
# print("Average of the list =", average)

# # ----------Write a Python program to find the maximum and minimum value of a list.
# # listt of numbers
# my_list = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]
# # using min and max function
# min_value = min(my_list)
# max_value = max(my_list)
# # print result
# print(min_value)
# print(max_value)

# ---------------test code----------------

# def my_function():
#     print("Hello from a function")

# my_function()

# def my_function(fname):
#   print(fname + " Smith")

# my_function("John")
# my_function("William")
# my_function("James")

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("John", "Smith")

# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)
# -------test code end----------------

# ------------Task 1----------
# show the list content
# list =  [10, 2, 3, 4, 7]

# for x in list:
#     print(x)

# The max value in the list

# max_value = max(list)
# print(max_value)
 
# -----------Task 2--------------



# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result

# print(factorial(6)) 



# -------Task 3--------

# num=int(input("Enter a number to check : "))
# for i in range(2,num):
#     if num % i==0:
#         print("Not prime")
#         break
# else:
#     print("prime")



