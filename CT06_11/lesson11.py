##print("Hello from lesson 11")
# ********* task 1 ***********
#rider1 = 120
#rider2 = 150
#if rider1 >= 120 and rider1 >= 120:
#    print(" you both can go on the ride!")
#else:
#    print(" you both can't go on the ride")
#******* task 2 *********
#num = int(input(" can you enter a number?\n"))
#if num % 3 == 0 and num % 7 == 0:
#    print(f"{num} is divisable by 3 and 7")
#else:
#    print(f"{num} isn't divisable by 3 and 7")
#******** task 3 *********
#name1 = input("what is your first name?").lower()
#name2 = input(" what is you last name?").lower()
#if name1 == "james" and name2 == "leong":
#    print(" you are wanted!!!!")
#else:
#    print(" your safe")
# ******** task 4 **********
#rider1 = int(input(" how old are you?"))
#rider2 = int(input(" how old is your partner"))
#if rider1 >= 18 or rider2 >= 18:
#    print(" you can go on this ride")
#else:
#    print(" sorry you're to young")
# ********** task 5 ************
#age = int(input("how old are you?"))
#if age < 12 or age > 64:
#    print(" your ticket costs $15")
#else:
#    print(" your ticket costs $20")
# *********** task 6 ***********
#gender = input("what is your gender").lower()
#if gender == "female" or gender == "male":
#    print(" valid gender")
#else:
#    print(" invalid response")
# ********* task 9 ********
#ans = input("what is the password?")
#if not ans == "python123":
#    print("acsess denied")
#else:
#    print("acsess granted")
#********* task 11 **********
username = "Jhon123"
password = "pw123"
user_input = input(" what is your username?")
pass_input = input("what is your password?")
if user_input == username and pass_input == password:
    print(" acsess granted")
elif user_input == username or pass_input == password:
    print(" either username or password is incorect")
else:
    print(" accses denied")
