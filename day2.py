#tip calculator  
   

total =int(input("Welcome to the tip calculator!\n What was the total bill? "))
tip= int(input("What percentage tip would you like to give? 10, 12 or 15 "))
people=int(input("How many people to split the bill? "))


total_tip=int(tip) * int(people)
tip_total=int(total_tip) + int(total)
per_person=int(tip_total)/int(people)
print(f"each person should pay: {per_person}")


