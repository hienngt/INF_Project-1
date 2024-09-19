# Project: Module 1 (DNA Similarity)
# Name: Monique Parrish
# This should be in moniques branch

# This is the main function and we are going to use this as the main menu
def main():
    # Introduction to the user
    introduction()

    # Input a menu to chose from which we will use a for
    UserInput = UserInputFunc()
    sequence1 = ""
    sequence2 = ""

    # While loop to keep running the menu
    while UserInput != 5:
        # print the following sequences
        if UserInput == 0:
            if sequence1 == "" or sequence2 == "":
                print("ERROR, please input sequences first")
            else:
                print(sequence1)
                print(sequence2)
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
            if sequence1 == "":
                print("Please insert Sequence 1")
            elif sequence2 == "":
                print("Please insert Sequence 2")
            else:
                compareFunc(sequence1, sequence2)

        # This option is for shifting the sequence but not yet comparing
        if UserInput == 4:
            # First we get the direction we want to shift the sequence
            print("To shift a sequence please indicate Left or Right with L or R.")
            direction = input("Left(L) or Right(R): ")
            print()
            # The User will indicate which sequence will be shifted
            print("Now please choose which sequence that you want to shift, either 1 or 2")
            ShiftSequence = int(input("Sequence (1) or Sequence (2): "))
            print(ShiftSequence)
            print()
            # Then we get the number of shifts to do
            print("Please Indicate how many times do you want to shift the sequence by?")
            NumShift = int(input("Shift by this much: "))
            # This is the space that needed to be added to the seqences
            ShiftSpaces = NumShift * "*"
            # If the Left direction is chosen
            if direction.upper() == "L":
                if ShiftSequence == 1:
                   sequence1 = ShiftSpaces + sequence1
                   sequence2 = sequence2 + ShiftSpaces
                elif ShiftSequence == 2:
                    sequence2 = ShiftSpaces + sequence2
                    sequence1 = sequence1 + ShiftSpaces
                else:
                    print("ERROR")
                    break
                # Now we comapre the shift sequences 
                compareFunc(sequence1, sequence2)
            elif direction.upper() == "R":
                if ShiftSequence == 1:
                   sequence1 = sequence1 + ShiftSpaces
                   sequence2 = ShiftSpaces + sequence2
                elif ShiftSequence == 2:
                    sequence2 = sequence2 + ShiftSpaces
                    sequence1 = ShiftSpaces + sequence1
                else:
                    print("ERROR")
                    break
                # Now we comapre the shift sequences 
                compareFunc(sequence1, sequence2)
            else:
                print("ERROR")
                break 

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
    print("0. Print current sequences")
    print("1. Input sequence 1")
    print("2. Input sequence 2")
    print("3. Compare the sequence")
    print("4. Shift the sequence")
    print("5. Quit")
    print()
    UserInput = int(input("Option Selected: "))
    print()

    return UserInput

def compareFunc(sequence1, sequence2):
    # This is the list that we will use to print
    compare = []
    # This is the count that will keep count of the number of matches
    count = 0
    # This is the for loop that will do the comparsion for seqence 1
    for i in range(len(sequence1)):
            # If statement if the indexes matches
            if sequence1[i] == sequence2[i]:
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

# run the main function
main()