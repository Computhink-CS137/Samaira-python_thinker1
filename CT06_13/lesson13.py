#Catolouge = []
#while True:
#    user_input = input("what do you want to buy?")
#    if user_input == "end":
#        break
#    Catolouge.append(user_input)
#print(Catolouge)

#ask = input("what are you looking for?")
#if ask in Catolouge:
#    print(f" yes we have {ask}")
#else:
#    print(f"we don't have {ask}")

# TAsk 5
#import random
#box = []
#for i in range(10):
#    num = random.randint(1, 999)
#    box.append(num)
#print(box)

#for i in range(len(box)):
#    print(f"Winner #{i + 1} = {box[i]}")

#Task 6
toppings = []
toppings.append("sauce")
toppings.append("Extra Cheese")
toppings.append("basil")
toppings.append("cucumber")
toppings.append("mushrooms")
toppings.append("carrots")
toppings.append("tomato")
toppings.append("corn")
toppings.append("olives")
toppings.append("garlic")
for i in range(len(toppings)):
    print(f" # { i + 1} = {toppings [i]}")
order_list = []
while True:
    ans = input(" CHoose your topping by number?")
    if ans == "end":
        break
    order_list.append(int(ans))


for i in range(len(order_list)):
    print(toppings[order_list[i] - 1])

