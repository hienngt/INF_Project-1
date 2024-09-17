# Project: Module 1 (DNA Similarity)
# Name: Monique Parrish

# This is the main function and we are going to use this as the main menu
def main():
    # Introduction to the user
    introduction()

    # We will get the sequence 1
    sequence1 = sequence_one()

    # We will get the sequence 2
    sequence2 = sequence_two()

    # print both squences
    print(sequence1)
    print(sequence2)

def introduction():
    print("Welcome to DNA Similarity")
    print("In this program we are going to compare 2 sequences of DNA samples.")
    print("In addition we can shift either sequence to see if there are any DNA matches caused by the shift.")
    print()

def sequence_one():
    #getting the input from the user (will move to file input)
    squence1 = input("please input sequence 1: ")
    return squence1

def sequence_two():
    #getting the input from the user (will move to file input)
    squence2 = input("please input sequence 2: ")
    return squence2

# run the main function
main()