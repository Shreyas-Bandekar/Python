# rock paper scissors game
# This is a simple rock-paper-scissors game where the user plays against the computer.

import random

computer = random.randint(0, 2)

user = input("Enter your choice (rock/paper/scissors): ").lower()

userDict = {"rock": 0, "paper": 1, "scissors": 2}
computerDict = {0: "rock", 1: "paper", 2: "scissors"}

if user not in userDict:
    print("Invalid choice!")
else:
    userChoice = userDict[user]
    print(f"Computer choice: {computerDict[computer]}")
    print(f"User choice: {user}")

    if computer == userChoice:
        print("Draw!")
    elif (computer == 0 and userChoice == 1) or \
         (computer == 1 and userChoice == 2) or \
         (computer == 2 and userChoice == 0):
        print("User wins!")
    else:
        print("Computer wins!")
