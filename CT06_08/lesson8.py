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

# # task 2b
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
#     inpUt = input("what is " + str(num1)  + " times " + str(num2) + " ?")
#     inpUt = int(inpUt)
#     if inpUt == answer:
#         print("correct")
#     else:
#         print("wrong")
#     print("the right answer is " + str(answer))


# # if else function
# example
# if 1 == 1:
#     print("correct")
# else:
#     print("worng")

# modulous
# using the percent sign just like divide but its taking the remainder instead of quotiont

#  task 7
# number = int(input("enter a number and I will tell you if its even or odd \n"))
# remainder = number % 2
# if remainder == 1:
#     print("your number is odd")
# if remainder == 0:
#     print("your number is even")

#  task 8
# num1 = int(input("can you type a number \n"))
# num2 = int(input("can you type a second smaller number \n"))
# remainder = num1 % num2
# if remainder == 0:
#     print(str(num1) + " is a multiple of " + str(num2) )
# else:
#     print(str(num1) + " is not a multiple of " + str(num2) )

#  task"9" extension(Gk quiz)
# score = 0
# ans1 = input("what is the capital of Haiti \n").lower()
# if ans1 == "port au prince":
#     print("correct") 
#     score = score + 1 
# else:
#     print("wrong")
#     print("The answer is Port Au Prince")
# ans2 = input(" what is the country with the most timezones? \n").lower()
# if ans2 == "france":
#     print("correct")
#     score = score + 1
# else:
#     print("wrong")
#     print(" the answer is France")
# ans3 = input(" what is the capital of equador \n").lower()
# if ans3 == "quito":
#     print("correct")
#     score = score + 1 
# else:
#     print("wrong")
#     print("the answer is Quito")
# print(" your final score is " + str(score) + "/3")

#  task 10 extension guess the number game
import random
number = random.randint(1, 100)
print(" guess my random number with 5 attempts, it is between 1 and 100")
attempts = 5
for i in range(attempts):
    guess = int(input("what do you guess? \n"))
    if guess > number:
        print("wrong")
        print(" you need to go lower")
    if guess < number:
        print("wrong")
        print("you need to go higher")
    if guess == number:
        print(" correct you are right ")
        break
    attempts = attempts - 1









