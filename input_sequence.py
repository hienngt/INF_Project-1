class InvalidNucleotideError(Exception):
    pass

valid_nucleotides = {'A', 'T', 'G', 'C'}


def __validate_sequence(sequence):
    """Validates the DNA sequence and returns True if valid, False otherwise."""
    if not isinstance(sequence, str):
        raise ValueError("Error: Input must be a string.")

    if len(sequence) == 0:
        raise ValueError("Error: DNA must have at least 1 string.")

    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            raise ValueError(f"Error: Invalid nucleotide found: '{nucleotide}'")

def validate_sequence(sequence: str) -> list[str] | None:
    try:
        sequence = sequence.upper()
        __validate_sequence(sequence)
    except Exception as e:
        print(f"{e}. Please re-enter the target sequence.")
        return None
    return list(sequence)

def input_single_sequence():
    print('-------------What type of input do you want?')
    print('-------------1: Using console')
    print('-------------2: Using file')

    choice = input("Please select an option (1 or 2): ")

    if choice == '1':
        # Input from console
        sequence = input("Please input sequence: ")
        return sequence

    elif choice == '2':
        # Input from file
        file_path = input("Please input the full file path: ")
        try:
            with open(file_path, 'r') as file:
                sequence = file.read().strip()
                return sequence
        except FileNotFoundError:
            print("File not found. Please check the file path and try again.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    else:
        print("Invalid option. Please select 1 or 2.")
        return None

def input_sequence():
    # We will get the sequences 1, 2
    sequence1 = None
    sequence2 = None
    while sequence1 is None:
        print('Input sequence 1:')
        sequence1 = input_single_sequence()
        if sequence1 is not None:
            sequence1 = validate_sequence(sequence1)

    while sequence2 is None:
        print('Input sequence 2:')
        sequence2 = input_single_sequence()
        if sequence2 is not None:
            sequence2 = validate_sequence(sequence2)

    return sequence1, sequence2
