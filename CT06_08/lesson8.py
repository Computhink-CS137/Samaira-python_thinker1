# print("Hello from lesson 8")
# for loops 
# for i in range(start, stop, step)
# i = counter variable
# you can use any letter, we usually start on i the godown(j,k, l, etc.)
# if it's in the same loop then use a different letter starting with i
# but if its a compleatly different for loop then you start with i again

# for i in range(5, 
# variables 
# Rules
# 1. no special symbols!@#$%^&*()_ under score is allowed
# 2. cant start with numbers
# 3.can have numbers in it though

# Data types
# integer(whole numbers)

# flaot(decimals)

# string(text or words)

# you can add a float with an integer
# num1 = 3
# num2 = 4.5
# ans = num1 + num2
# print(ans)
# srting concatenation
# adding to strings together

# Type casting 
# changing something temporarly  
# num1 = "10"
# num1 = int(num1)
# print("My number is " + str(num1))

# Boolean - true or false(a data point)

# Recap 1
# total = 1
# for i in range(1, 6):
#     ans1 = int(input("What is number #" + str(i) + "? "))
# # with input the answer is allways a string origanally3
#     total = total * ans1
# print("the product is " + str(total))

# python libraries(like scratches extentions eg. the pen, or functuions)
#  to add a library you need to import
## task 1a
# import time

# for i in range(10, 1, -1):
#     print(i)
#     time.sleep(1)
#  time.sleep is like the scratch wait block

# # task 1b add input
# import time
# seconds = int(input("how many seconds will your count down last? "))
# for i in range(seconds, 0, -1):
#     print(i)
#     time.sleep(1)

# new library called random
# random library can give you a random number 
# task 2a
# import random

# rand_num = random.randint(1, 6)# in random it is inclusive of both munbers on the ends
# # randint stands for random integer(only chooses integers)
# print(rand_num)

# task 2b
# import random
# for i in range(20):
#     rand_num = random.randint(0, 999)
#     print(rand_num)

# boolean decisions(yes or no)(True or False)
# true or false starts with a capital letter for a boolean, if no capital then its a regular variable
# comparison symbols 
# hello = 1 (equals as variables)
# 1 == 1 (equals in comparison)

# true_or_false = 1 == 1
# print(true_or_false)

# task 3
# boolean1 = True
# boolean2 = False
# print(boolean1 == boolean2)

# task5
# import random
# num1 = random.randint(1, 10)
# guess = int(input("what do you think my number from 1-10 is? "))
# print(guess == num1)
# print("my number is " + str(num1))

# task 6

# import random
# questions = int(input("how many questions do you want to answer? "))
# for i in range(questions):
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)
#     answer = num1 * num2
#     inpUt = int(input("what is " + str(num1)  + " times " + str(num2) + " ?"))
#     print(inpUt == answer )
#     print("the answer is " + str(answer))






