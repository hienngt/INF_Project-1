class InvalidNucleotideError(Exception):
    """Custom exception for invalid nucleotide errors."""
    pass


# Set of valid nucleotides
valid_nucleotides = {'A', 'T', 'G', 'C'}


def __validate_sequence(sequence):
    """Validates the DNA sequence and returns True if valid, False otherwise."""

    # Ensure the input is a string
    if not isinstance(sequence, str):
        raise ValueError("Error: Input must be a string.")

    # Check if the sequence is not empty
    if len(sequence) == 0:
        raise ValueError("Error: DNA must have at least 1 string.")

    # Check each nucleotide in the sequence for validity
    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            raise ValueError(f"Error: Invalid nucleotide found: '{nucleotide}'")


def validate_sequence(sequence: str) -> list[str] | None:
    """Validates the DNA sequence and returns it as a list of uppercase nucleotides if valid, None otherwise."""
    try:
        sequence = sequence.upper()  # Convert sequence to uppercase for standardization
        __validate_sequence(sequence)  # Validate the sequence
    except Exception as e:
        print(f"{e}. Please re-enter the target sequence.")
        return None  # Return None if validation fails
    return list(sequence)  # Return the valid sequence as a list of characters


def input_single_sequence():
    """Prompts the user for a DNA sequence either from console input or a file."""
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
                sequence = file.read().strip()  # Read and strip whitespace from the file
                return sequence  # Return the sequence read from the file
        except FileNotFoundError:
            print("File not found. Please check the file path and try again.")
            return None  # Return None if the file is not found
        except Exception as e:
            print(f"An error occurred: {e}")
            return None  # Handle other exceptions

    else:
        print("Invalid option. Please select 1 or 2.")
        return None  # Return None for invalid options


def input_sequence():
    """Collects two valid DNA sequences from the user, ensuring they are validated."""
    sequence1 = None
    sequence2 = None

    # Loop until a valid sequence1 is entered
    while sequence1 is None:
        print('Input sequence 1:')
        sequence1 = input_single_sequence()  # Get the first sequence
        if sequence1 is not None:
            sequence1 = validate_sequence(sequence1)  # Validate the first sequence

    # Loop until a valid sequence2 is entered
    while sequence2 is None:
        print('Input sequence 2:')
        sequence2 = input_single_sequence()  # Get the second sequence
        if sequence2 is not None:
            sequence2 = validate_sequence(sequence2)  # Validate the second sequence

    return sequence1, sequence2  # Return both validated sequences