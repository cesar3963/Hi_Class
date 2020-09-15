# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

print("Computer picked " + computer_choice)

# Run Conditionals
if user_choice == computer_choice:
    print("Tied")
elif user_choice == "r":
    if computer_choice == "p":
        print("computer won")
    else:
        print("you won")
elif user_choice == "p":
    if computer_choice == "r":
        print("you won")
    else:
        print("computer won")
elif user_choice == "s":
    if computer_choice == "r":
        print("computer won")
    else:
        print("you won")
else:
    print("you picked the wrong letter")
