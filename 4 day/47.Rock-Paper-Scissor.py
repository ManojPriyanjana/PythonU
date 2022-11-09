import random

#normaly input getin as String,then we have to convert it to int
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "));
computer_choice=random.randint(0,2)
print(f"Computer chose{ computer_choice}")

if user_choice == 0 and computer_choice ==2:
    print("you win!")
elif computer_choice > user_choice:

    print("you lost")
else:
    print("You typed an invalid number,you lose!")


