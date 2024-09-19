# Project: Module 1 (DNA Similarity)
# Name: Monique Parrish
# This should be in moniques branch

# This is the main function and we are going to use this as the main menu
def main():
    # Introduction to the user
    introduction()

    # Input a menu to chose from which we will use a for
    UserInput = UserInputFunc()

    # While loop to keep running the menu
    while UserInput != 5:
        # This is the first option
        if UserInput == 1: 
            # We will get the sequence 1
            sequence1 = sequence_one()
            # print squence 1
            print("Sequence 1: ", sequence1)

        # This is the second option
        if UserInput == 2:
            # We will get the sequence 2
            sequence2 = sequence_two()
            # print sequence 2
            print("Sequence 2: ", sequence2)

        # We are going to compare the sequences before any shifts
        # But this can be a function if need be
        if UserInput == 3:
            # This is the list that we will use to print
            compare = []
            # This is the count that will keep count of the number of matches
            count = 0
            # This is the for loop that will do the comparsion for seqence 1
            for i in range(0, len(sequence1)):
                # This is the for loop for seqence 2
                for j in range(0, len(sequence2)):
                    # If statement if the indexes matches
                    if sequence1[i] == sequence2[j]:
                        # append the matches
                        compare.append(sequence1[i])
                        # increment the count
                        count += 1
            # This if for not having any matches
            if compare == []:
                print("There are no matches,", count)
            # This is for having matches
            else:
                # Printing how many matches 
                print(compare)
                print("This is how many DNAs are the same:", count)

        # This option is for shifting the sequence but not yet comparing 

        # Get the new Input
        UserInput = UserInputFunc()



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
    print("3. Compare the sequence")
    print("4. Shift the sequence")
    print("5. Quit")
    print()
    UserInput = int(input("Option Selected: "))
    print()

    return UserInput

# run the main function
main()