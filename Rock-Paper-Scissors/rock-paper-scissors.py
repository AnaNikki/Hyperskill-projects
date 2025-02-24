# Stage 1 - Unfair computer
# Stage 2 - Equalizing chances
# Stage 3 - Endelss game

import random

while True:
    # Get the user's input and convert it to lowercase for case-insensitive comparison
    user_option = input("Choose rock, paper, scissors, or '!exit' for exiting the game: ").lower()

    # Define valid options for the game
    computer_option = ["rock", "paper", "scissors"]

    # Randomly choose the computer's option
    random_option = random.choice(computer_option)

    # Check if the user input is valid
    if user_option == "rock" or user_option == "paper" or user_option == "scissors":

        # Define dictionary with the outcomes
        # First key = user input
        outcomes = {
            "rock": {
                "rock": f"There is a draw (rock)",
                "paper": f"Sorry, but the computer chose paper",
                "scissors": f"Well done. The computer chose scissors and failed"
            },
            "paper": {
                "rock": f"Well done. The computer chose rock and failed",
                "paper": f"There is a draw (paper)",
                "scissors": f"Sorry, but the computer chose scissors"
            },
            "scissors": {
                "rock": f"Sorry, but the computer chose rock",
                "paper": f"Well done. The computer chose paper and failed",
                "scissors": f"There is a draw (scissors)",
            }
        }

        # Get the result from the dictionary from the user input and the computer choice
        result = outcomes[user_option].get(random_option)
        print(random_option)
        print(result)

    # Check if the user input is !exit
    elif user_option == "!exit":
            print("Bye!")
            break

    else:
        print("Invalid input")
        print("Please choose between rock, paper, or scissors! Or '!exit' for exiting the game!")
