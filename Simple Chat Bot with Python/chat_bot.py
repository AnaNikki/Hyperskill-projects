def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")


def remind_name():
    print("Please, remind me your name.")
    # reading a name
    name = input()
    print(f"What a great name you have, {name}!")


def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    remainder3 = int(input())
    remainder5 = int(input())
    remainder7 = int(input())
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")


# read a number and count to it here
def count():
    print('Now I will prove to you that I can count to any number you want.')
    number = int(input("Tell me a number: "))
    counter = 0
    while counter <= number:
        print(f"{counter} !")
        counter += 1


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    question = "Why do we use methods?"
    answer1 = "1. To repeat a statement multiple times."
    answer2 = "2. To decompose a program into several small subroutines."
    answer3 = "3. To determine the execution time of a program."
    answer4 = "4. To interrupt the execution of a program."
    print(question)
    print(answer1)
    print(answer2)
    print(answer3)
    print(answer4)
    answer = input()
    while answer != answer2[0]:
        print("Please, try again.")
        answer = input()
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


# Now we can use these functions
greet("Astro", 2024)
remind_name()
guess_age()
count()
test()
end()

