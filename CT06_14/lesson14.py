# # task 1a recap
# import random
# rolls = [] 
# for i in range(5):
#     num = random.randint(1, 6)
#     rolls.append(num)
# print(rolls)
# # task 1b
# roll_sum = 0
# for i in range(len(rolls)):
#     roll_sum = rolls[i] + roll_sum
# print(roll_sum)
# # parallel lists
# # task 1a
# fruits = ["strawberries", "apples", "mangos", "bananas" ]
# prices = [10, 7, 9, 6]
# for i in range(len(prices)):
#     print(f"{fruits[i]} is ${prices[i]:.2f}")
# # task 2
# items = ["Apple", "Milk", "Bread", "Egg", "Chocolate"]
# stock = [15, 0, 8, 25, 3]
# for i in range(len(items)):
#     # check stock status
#     if stock[i] == 0:
#         status = "out of stock"
#     elif stock[i] < 10:
#         status = "low stock"
#     else:
#         status = "well stocked"
#     print(f"item: {items[i]} | Qty: {stock[i]} | status: {status}")
# ans = input("what do you want to buy?"\n).capitalize()
# if ans in items:
#     print(f"we have {ans}")
#     print(f"{stock[items.index(ans)]} {ans}s remaining")
# else:
#     print(f" we dont have {ans}")

import random
moves = ["scissors", "paper", "stone"]
player_score = 0
computer_score = 0
while player_score < 3 and computer_score < 3:
    computer_choice = random.choice(moves) #computer choose random item in list
    player_choice = input("Choose Scissors, Paper, or Stone: ").lower()
    
                          
    if player_choice in moves:
        print(f"Computer Chose: {computer_choice} ")
        #win conditions
        if(player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "stone") or (player_choice == "stone" and computer_choice == "scissors"):
            player_score += 1
            print("You won this round:)")
        elif player_choice == computer_choice:
            print("this rounds a tie?")
        else:
            computer_score += 1
            print("computer wins this round:(")
        print(f"Score - player: {player_score} | Computer: {computer_score}")
    else:
        print(" Invalid Move")
if player_score == 3:
    print(" Final Result: you win :)")
else:
    print("Final Result: computer wins :(")

    
        
                          
                          



