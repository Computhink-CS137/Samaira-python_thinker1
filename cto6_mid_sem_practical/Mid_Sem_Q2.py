# 
starting = int(input("How much money did you start with? "))
days = int(input(" How many days are there? "))
adding = 1
for i in range(days):
    starting = starting + adding
    adding = adding + 1
print("the total amount saved is $" + str(starting))

