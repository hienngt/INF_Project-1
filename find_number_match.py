def compare_2_sequence(sequence1: list[str], sequence2: list[str]) -> (int, list[str]):
    compare = []  # List to store comparison results
    count = 0     # Counter for matching elements

    # Determine the length to iterate over
    range_len = min(len(sequence1), len(sequence2))

    # Compare elements in both sequences
    for i in range(range_len):
        if sequence1[i] == sequence2[i] and sequence1[i] != 'x':
            compare.append(sequence1[i])  # Append matching elements
            count += 1                     # Increment match count
        else:
            compare.append('x')            # Append 'x' for non-matching

    return count, compare

def shift_sequence(sequence1: list[str], sequence2: list[str], max_shift: int = None) -> list[list[list[str]]]:
    lst_pair_sequence = []
    lst_pair_sequence.append([sequence1, sequence2])

    # Adjust max_shift if it exceeds the minimum length of the sequences
    min_length = min(len(sequence1), len(sequence2))
    if (max_shift is not None and max_shift > min_length) or max_shift is None:
        max_shift = min_length
        print('Max shift adjusted to minimum sequence length.')

    for i in range(max_shift):
        # Create a list with 'x' to shift
        add_in_sequence = ['x'] * (i + 1)

        # Shift sequence1 to the right, sequence2 to the left
        sequence1_new = sequence1 + add_in_sequence
        sequence2_new = add_in_sequence + sequence2
        lst_pair_sequence.append([sequence1_new, sequence2_new])

        # Shift sequence2 to the right, sequence1 to the left
        sequence1_new = add_in_sequence + sequence1
        sequence2_new = sequence2 + add_in_sequence
        lst_pair_sequence.append([sequence1_new, sequence2_new])

    return lst_pair_sequence

def find_match(sequence1: list[str], sequence2: list[str], shift_value: int=None):
    print('Find matches with shift value =', shift_value)

    lst_pair_sequence = shift_sequence(sequence1, sequence2, shift_value)

    max_matches, max_sequence1, max_sequence2, max_compare, max_shift = 0, [], [], [], 0

    for i in range(len(lst_pair_sequence)):
        print('Shift value =', i//2)
        sequence1 = lst_pair_sequence[i][0]
        sequence2 = lst_pair_sequence[i][1]
        count, compare = compare_2_sequence(sequence1, sequence2)

        if count > max_matches:
            max_matches, max_sequence1, max_sequence2, max_compare, max_shift = count, sequence1, sequence2, compare, i//2

        # Printing the results
        print('--------------------------------------------------------------------------------')
        print('---------- Sequence 1    :', sequence1)
        print('---------- Sequence 2    :', sequence2)
        print('---------- Compare result:', compare)
        print("---------- Number matches:", count)

    # Printing the max results
    print('********************************************************************************')

    print('********** Max matches:', max_matches)
    print('********** Shift value:', max_shift)

    print('********** Sequence 1    :', max_sequence1)
    print('********** Sequence 2    :', max_sequence2)
    print('********** Compare result:', max_compare)

def input_shift_value() -> int:
    choice_re_enter = 'y'
    while choice_re_enter == 'y':
        try:
            shift_value = int(input("Shift by this much: "))
            if shift_value < 0:
                print('Shift value must be greater than or equal to 0.')
                choice_re_enter = 'y'
            else:
                return shift_value
        except ValueError as e:
            print(f'{e}. You must enter a number.')
            print('Do you wanna re-enter? (y or n)')
            choice_re_enter = input("Option Selected: ").lower()

def find_max_match(sequence1, sequence2):
    print('Do you want to indicate how many times you want to shift the sequence by? (y or n)')
    while True:
        choice = input("Option Selected: ").lower()

        if choice == 'y':
            shift_value = input_shift_value()
            break  # Exit the loop after processing the shift value
        elif choice == 'n':
            shift_value = None
            break  # Exit the loop if the user does not want to shift
        else:
            print('Invalid input. Please enter "y" or "n".')

    find_match(sequence1, sequence2, shift_value)
