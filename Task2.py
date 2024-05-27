# Author: An Cheng
# Date: 27/05/24
# -----------------------------
# Description: A game where the user must correctly guess a randomly generated integer between 1 and 100.
# The program will generates a random integer number and stores it to let the user guess
# It will keep asking the user to enter a correct format of number to guess
# If the guess is right or the user enter nothing, the program will exit
# If get wrong answer, the program will continue until the user give correct answer
# This program utilize loop to continuously ask for input until get ideal input

import random

def generate_random_number():
    """
    Generaates a random integer between 1 and 100

    :return:
        int: A randomly generated integer
    """
    # generate a random int between 1 and 100
    random_number =  random.randint(1, 100)
    print("A random number is generated.")
    return random_number

def prompt():
    """
    Prints the instructions for the user
    """
    print("(To exit the game, press ENTER directly)")
    print("Enter a integer number between 1 and 100 to guess:")

def validate_input(user_input):
    """
    Validates whether the user's input is an integer within (1, 100)

    :param user_input: str, input string from the user
    :return:
        bool: True if the input is valid, False if invalid
    """
    if user_input.isdigit():
        if int(user_input) > 100 or int(user_input) < 1:
            return False
        return True
    else:
        return False

def result(target, user_input):
    """
    Check the user's input with the target and print feedback

    :param target: int, the target value
    :param user_input: int, user's input in int format
    :return:
        bool: True if the guess is correct, False if incorrect
    """
    if user_input == target:
        print(f"The random number is {target}.")
        print("Congraduation! You got the right number!")
        return True
    elif user_input > target:
        print("Your number is larger than the generated number.")
    else:
        print("Your number is smaller than the generated number.")
    return False
def guess(target):
    """
    Get the guess from the user and check whether the guess is correct

    :param target: int, the random number to be guessed
    :return:
        bool: True if the game need to continue, False to end the game
    """
    # print prompt for the game
    prompt()
    # Get input
    user_input = input("Your Guess: ")
    # if no input, stop the loop and exit the game
    if user_input == "":
        print("-" * 20)
        print("You didn't enter anything, exiting the game...")
        print("Thank you for playing!")
        return False

    # Validate the input to be a integer between 1 and 100
    if validate_input(user_input):
        user_input_int = int(user_input)
        correct = result(target, user_input_int)
        # if get correct answer, stop the loop and exit the game
        if correct: return False
    else:
        # prompt to get a valid input
        print("Your input is invalid! ")
        print("Please enter an integer between 1 and 100! [Example: 88]")
    # let the user wait and read instructions for next step
    wait = input("Press Enter to Continue... ")
    # This true value will continue the loop to continue the game
    return True


# main function of the game
def main():
    # initiate the value
    if_cont = True
    # generate a random int
    target = generate_random_number()
    # loop until guess correctly or user want to exit
    while if_cont:
        print("-"*20)
        if_cont = guess(target)

# when running this file, this will call the main function
if __name__ == "__main__":
    main() # call the main function