def compare_2_sequence(sequence1: list[str], sequence2: list[str]) -> (int, list[str]):
    """Compares two DNA sequences and returns the count of matching elements and a comparison list."""
    compare = []  # List to store comparison results
    count = 0     # Counter for matching elements

    # Determine the length to iterate over based on the shorter sequence
    range_len = min(len(sequence1), len(sequence2))

    # Compare elements in both sequences
    for i in range(range_len):
        # Check if elements match and are not 'x'
        if sequence1[i] == sequence2[i] and sequence1[i] != 'x':
            compare.append(sequence1[i])  # Append matching elements
            count += 1                     # Increment match count
        else:
            compare.append('x')            # Append 'x' for non-matching

    return count, compare  # Return the total count of matches and the comparison list

def shift_sequence(sequence1: list[str], sequence2: list[str], max_shift: int = None) -> list[list[list[str]]]:
    """Generates shifted versions of two sequences up to a specified maximum shift."""
    shifted_sequences = []
    shifted_sequences.append([sequence1, sequence2])  # Add original sequences to the list

    # Determine the minimum length of the sequences to set the max_shift
    min_length = min(len(sequence1), len(sequence2))
    if (max_shift is None) or (max_shift > min_length):
        max_shift = min_length  # Adjust max_shift to the minimum length if necessary
        print('Max shift adjusted to minimum sequence length.')

    # Generate shifted sequences
    for shift in range(max_shift):
        # Create a padding list to represent the shift
        padding = ['x'] * (shift + 1)

        # Shift sequence1 to the right and sequence2 to the left
        shifted_seq1 = sequence1 + padding
        shifted_seq2 = padding + sequence2
        shifted_sequences.append([shifted_seq1, shifted_seq2])  # Add to the list of shifted pairs

        # Shift sequence2 to the right and sequence1 to the left
        shifted_seq1 = padding + sequence1
        shifted_seq2 = sequence2 + padding
        shifted_sequences.append([shifted_seq1, shifted_seq2])  # Add to the list of shifted pairs

    return shifted_sequences  # Return all pairs of sequences

def find_match(sequence1: list[str], sequence2: list[str], shift_value: int = None):
    """Finds and displays matches between two sequences, considering a specific shift."""
    print('Finding matches with shift value =', shift_value)

    # Generate shifted pairs of sequences
    shifted_pairs = shift_sequence(sequence1, sequence2, shift_value)

    # Initialize variables to track the maximum matches found
    max_matches = 0
    max_sequence1 = []
    max_sequence2 = []
    max_compare = []
    max_shift = 0

    # Iterate over the list of shifted sequences
    for index, (seq1, seq2) in enumerate(shifted_pairs):
        current_shift = index // 2  # Calculate the current shift value
        print('Shift value =', current_shift)

        count, comparison = compare_2_sequence(seq1, seq2)  # Compare the sequences

        # Update maximum matches if the current count exceeds previous max
        if count > max_matches:
            max_matches = count
            max_sequence1 = seq1
            max_sequence2 = seq2
            max_compare = comparison
            max_shift = current_shift

        # Print the results for the current comparison
        print('--------------------------------------------------------------------------------')
        print('---------- Sequence 1    :', seq1)
        print('---------- Sequence 2    :', seq2)
        print('---------- Compare result:', comparison)
        print("---------- Number matches:", count)

    # Print the overall max results
    print('********************************************************************************')
    print('********** Max matches:', max_matches)
    print('********** Shift value:', max_shift)
    print('********** Sequence 1    :', max_sequence1)
    print('********** Sequence 2    :', max_sequence2)
    print('********** Compare result:', max_compare)

def input_shift_value() -> int:
    """Prompts the user for a shift value, ensuring valid input."""
    while True:  # Loop until a valid input is received
        try:
            shift_value = int(input("Shift by this much: "))  # Prompt for shift value
            if shift_value < 0:
                print('Shift value must be greater than or equal to 0.')  # Validate input
                continue  # Continue prompting for a valid value
            return shift_value  # Return the valid shift value
        except ValueError:
            print('You must enter a valid number.')  # Handle non-integer input
            reenter_choice = input('Do you want to re-enter? (y or n): ').lower()  # Ask if the user wants to re-enter
            if reenter_choice != 'y':
                print('Exiting input prompt.')
                break  # Exit if the user does not want to re-enter

def find_max_match(sequence1: list[str], sequence2: list[str]):
    """Prompts the user to determine if they want to specify a shift value and finds matches accordingly."""
    while True:
        choice = input('Do you want to specify how many times to shift the sequence? (y or n): ').lower()  # User prompt

        if choice == 'y':
            shift_value = input_shift_value()  # Get a valid shift value
            break  # Exit loop after getting the shift value
        elif choice == 'n':
            shift_value = None  # No shift specified
            break  # Exit loop
        else:
            print('Invalid input. Please enter "y" or "n".')  # Handle invalid input

    find_match(sequence1, sequence2, shift_value)  # Call find_match with the specified shift value