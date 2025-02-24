# Stage 1 - Unfair computer

user_option = input("Choose rock, paper, or scissors: ")

computer_option = ""

if user_option == 'rock':
    computer_option = 'paper'
    print(f"Sorry, but the computer chose {computer_option}")
elif user_option == 'paper':
    computer_option = 'scissors'
    print(f"Sorry, but the computer chose {computer_option}")
elif user_option == 'scissors':
    computer_option = 'rock'
    print(f"Sorry, but the computer chose {computer_option}")
