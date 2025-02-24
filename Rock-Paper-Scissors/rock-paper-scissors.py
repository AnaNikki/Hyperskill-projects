# Stage 1 - Unfair computer
# Stage 2 - Equalizing chances

import random

if user_option == "rock" or user_option == "paper" or user_option == "scissors":
    if user_option == random_option:
        print(f"There is a draw ({random_option})")
    elif user_option == "rock" and random_option == "paper":
        print(f"Sorry, but the computer chose {random_option}")
    elif user_option == "rock" and random_option == "scissors":
        print(f"Well done. The computer chose {random_option} and failed")
    elif user_option == "paper" and random_option == "rock":
        print(f"Well done. The computer chose {random_option} and failed")
    elif user_option == "paper" and random_option == "scissors":
        print(f"Sorry, but the computer chose {random_option}")
    elif user_option == "scissors" and random_option == "rock":
        print(f"Sorry, but the computer chose {random_option}")
    elif user_option == "scissors" and random_option == "paper":
        print(f"Well done. The computer chose {random_option} and failed")
else:
    print("Please choose between rock, paper, or scissors!")
