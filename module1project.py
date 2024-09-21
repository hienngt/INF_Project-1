# Project: Module 1 (DNA Similarity)
# Name: Monique Parrish and Hien
# This should be in main branch
# This is the main function and we are going to use this as the main menu
from find_number_match import find_max_match, find_match
from input_sequence import input_sequence


def introduction():
    print('--------------------------------------------------------------------------------')
    print("Welcome to DNA Similarity")
    print('--------------------------------------------------------------------------------')
    print()
    print("In this program we are going to compare 2 sequences of DNA samples.")
    print("In addition we can shift either sequence to see if there are")
    print("any DNA matches caused by the shift.")
    print()
    print("Please choose one of the following options from the menu:")
    print()

def user_inputs():
    print()
    print("-------------0. Print current sequences")
    print("-------------1. Input sequences")
    print("-------------2. Compare the sequence")
    print("-------------3. Find max matches")
    print("-------------4. Quit")
    print()

    user_input = int(input("Option Selected: "))
    print()

    return user_input

def main():
    # Introduction to the user
    introduction()

    # Initialize parameters
    sequence1 = []
    sequence2 = []
    shift_value = 0

    # Input a menu to choose from
    user_input = user_inputs()

    # While loop to keep running the menu
    while user_input != 4:
        # Print the following sequences
        if user_input == 0:
            print("Sequence 1:", sequence1)
            print("Sequence 2:", sequence2)


        if user_input == 1:
            sequence1, sequence2 = input_sequence()

        # Compare the sequences before any shifts
        if user_input == 2:
            find_match(sequence1, sequence2, 0)


        if user_input == 3:
            find_max_match(sequence1, sequence2)

        # Prompt user for next input
        user_input = user_inputs()  # Get the next user input

    print("Exiting the program. Thank you!")


if __name__ == "__main__":
    main()  # Call the main function