#treasure island game

print("Welcome to Treasure İsland!\nYour mission is to find to treasure.")

first_answer= input("You are a cross road. Where do you want to go? 'left' or 'right' ").lower()

if first_answer == 'left':
    second_answer= input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if second_answer == 'wait':
        third_answer= input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and blue. Which colour do you choose? ").lower()
        if third_answer == 'yellow':
            print("Well done! You found the treasure!")
        elif third_answer == 'blue':
            print("You entered a room of flame. Game over.")
        else:
            print("You fall from the cliff. Game over.")
    else:
        print("You eaten by sharks. Game over.")
else:
    print("You are at unlucky day. Unfortunatelly game over.")            
 