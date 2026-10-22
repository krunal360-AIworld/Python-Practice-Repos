import random

Rock = 0
Paper = 1
scissor = 2
user_input = int(input("Enter Your Choice. 1 for Rock, 2 for Paper and 3 for Scissor : "))
if user_input < 0 or user_input > 2:
    print("Invalid Input Try Again ! ")
else:
    computer_choice = random.randint(0,2)
    print("Computer Choses ",computer_choice)

    if computer_choice == user_input :
        print(" It's Draw ")

    elif user_input == 0 and computer_choice == 2:
        print("Hurray! You Win This Game")

    elif user_input ==2 and computer_choice == 0:
        print("Oh! You Lost This Game")

    elif user_input > computer_choice :
         print("Hurray! You Win This Game")

    elif user_input < computer_choice :
            print("Oh! You Lost This Game")
    
print("Game Finished")
