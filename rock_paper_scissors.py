import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

images = [rock, paper, scissor]
game_names = ["Rock","Paper","Scissor"]

user_input = int(input("Enter Your Choice. 0 for Rock, 1 for Paper and 2 for Scissor : "))
if user_input < 0 or user_input > 2:
    print("Invalid Input Try Again ! ")
else:
    print(f"You Chose :{game_names[user_input]}")
    print(images[user_input])
    
    computer_choice = random.randint(0,2)
    print(f"Computer Choses :{game_names[computer_choice]}")
    print(images[computer_choice])

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
