from dna import DNA
import os


def is_valid_file(file_path: str) -> bool:
    """Check if the provided path is a valid file."""
    return os.path.isfile(file_path)


def input_sequence():
    input_value = input("Enter a sequence (or file path): ")
    if is_valid_file(input_value):
        with open(input_value, 'r') as file:
            sequence = file.read().strip()
        print(f"Sequence from file: {sequence}")
    else:
        sequence = input_value.strip()
        print(f"Sequence entered: {sequence}")


def UserInputFunc():
    while True:
        print()
        print("0. Print current sequences")
        print("1. Input sequence 1 (string or file path)")
        print("2. Input sequence 2 (string or file path)")
        print("3. Compare the sequences")
        print("4. Shift the sequence")
        print("5. Quit")
        print()

        try:
            UserInput = int(input("Option Selected: "))
            print()

            # Check if the input is within the valid range
            if UserInput not in range(6):
                print("Error: Please select a valid option (0-5).")
                continue

            # Handle input for sequences if option 1 or 2 is selected
            if UserInput in [1, 2]:
                input_value = input("Enter a sequence (or file path): ")
                if is_valid_file(input_value):
                    with open(input_value, 'r') as file:
                        sequence = file.read().strip()
                    print(f"Sequence from file: {sequence}")
                else:
                    sequence = input_value.strip()
                    print(f"Sequence entered: {sequence}")

                return UserInput, sequence

            return UserInput

        except ValueError:
            print("Error: Invalid input. Please enter a number between 0 and 5.")


# Example usage
if __name__ == "__main__":
    selected_option, sequence = UserInputFunc()
    print(f"You selected option: {selected_option}")
    if selected_option in [1, 2]:
        print(f"Sequence: {sequence}")