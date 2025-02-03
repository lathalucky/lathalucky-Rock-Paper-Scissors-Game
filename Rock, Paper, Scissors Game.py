
import numpy.random as r


# Function Definition
def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    your_choice = input("enter your choice (Rock/Paper/Scissors):").lower()
    if your_choice in choices:

        computer_choice = r.choice(choices)
        print("computer_choice :",computer_choice)
        print("your_choice :",your_choice)
        print("")
        if your_choice == computer_choice:
            print("It's a tie!")
        elif (your_choice == "rock" and computer_choice == "scissors") or (
                your_choice == "scissors" and computer_choice == "paper") or (
                your_choice == "paper" and computer_choice == "rock"):
            print("You win! 🎉")
        else:
            print("Computer wins! 😢")
    else:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")

# Function Calling
rock_paper_scissors()