# num = int(input(" can you give me a number that is divisible by 3 and 5? \n"))
# if num % 3 == 0 and num % 5 == 0:
#     print(f" {num} is divisible by 3 and 5 ")
# else:
#     print(f" {num} is not divisible by both three and 5") 

# task 1(while loop)  (repeat until)
# visitors = 18
# while visitors < 30:
#     visitors += 1
#     print(visitors)


# forever loop(task 2)(control c stops forever loops)
# "break" stops a loop
# while True:
#     print("hi")
#     break

#  task 2
# forever loops are better when there are more conditions, 
# # because you can make multiple conditions to exit
# visitors = 0
# while True:
#     visitors += 1 
#     print(visitors)

#     if visitors >= 50:
#          break


# order = input(" what do you want to order? \n")
# while True:
#     ans = input(" what do you want to order? \n") 

#     if ans == "end" or ans == "done":
#         break
#     order = order + " , " + ans 

# print(f" Your Order: {order}.")


# # else inside while loops 
# # task 4
# counter = 10
# while not counter <= 0:
#     print(counter)
#     counter -= 1
# else:
#     print("Happy New Year!!!")
# # when the loop condition is false 
# # (when the loop ends)
# # if the while loop is stoped earlier eg. "break" the condition hear will not happen
    
import random
score = 0
while score < 20:
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    operator = random.randint(1, 3)
    if operator == 1:
        ans = num1 + num2
        operator_sign = "+"
    elif operator == 2:
        ans = num1 - num2
        operator_sign = "-" 
    else:
        ans = num1 * num2
        operator_sign = "*"

    inp = int(input(f" what is {num1} {operator_sign} {num2}? \n"))
    if inp == ans:
        print("thats right :)") 
        score = score + 2
        print(f"your current score is {score}")
    else:
        print("thats wrong :(")
        print(f"the answer is {ans}")
        score = score - 1
        print(f"your current score is {score}")
        


   




