#  
total_bill = int(input("how many dollers does your meal cost? "))
total_people = int(input("how many people are there? "))
cost_per_person = total_bill / total_people
cost_per_person = round(cost_per_person, 2)
print("Each person has to pay $" + str(cost_per_person))