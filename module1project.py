# Project: Module 1 (DNA Similarity)
# Name: Monique Parrish

# This is the main function and we are going to use this as the main menu
def main():
    # Introduction to the user
    introduction()

    # Input a menu to chose from which we will use a for
    UserInput = UserInputFunc()

    # While loop to keep running the menu
    while UserInput != 4:
        # This is the first option
        if UserInput == 1: 
            # We will get the sequence 1
            sequence1 = sequence_one()
        #This is the second option
        if UserInput == 2:
            # We will get the sequence 2
            sequence2 = sequence_two()

        # Get the new Input
        UserInput = UserInputFunc()

    # print both squences
    print(sequence1)
    print(sequence2)

    # We are going to compare the sequences before any shifts


    # Then we make an menu

def introduction():
    print("-------------------------")
    print("Welcome to DNA Similarity")
    print("-------------------------")
    print()
    print("In this program we are going to compare 2 sequences of DNA samples.")
    print("In addition we can shift either sequence to see if there are any DNA matches caused by the shift.")
    print()
    print("Please choose one of the following options from the menu:")
    print()

def sequence_one():
    #getting the input from the user (will move to file input)
    squence1 = input("Please input sequence 1: ")
    return squence1

def sequence_two():
    #getting the input from the user (will move to file input)
    squence2 = input("Please input sequence 2: ")
    return squence2

def UserInputFunc():
    print()
    print("1. Input sequence 1")
    print("2. Input sequence 2")
    print("3. Shift either sequence")
    print("4. Quit")
    print()
    UserInput = int(input("Option Selected: "))
    print()

    return UserInput

# run the main function
main()