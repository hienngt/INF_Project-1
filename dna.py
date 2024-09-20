class InvalidNucleotideError(Exception):
    pass

class DNA:
    valid_nucleotides = {'A', 'T', 'G', 'C'}

    def __init__(self, sequence: str):
        self.sq = sequence
        try:
            self.__validate_sequence()
        except (InvalidNucleotideError, ValueError) as e:
            self.sq = -1
            print(f"{e}. Please re-enter the target sequence.")


    def __validate_sequence(self) -> bool:
        """Validates the DNA sequence and returns True if valid, False otherwise."""
        if not isinstance(self.sq, str):
            raise ValueError("Error: Input must be a string.")

        if len(self.sq) == 0:
            raise ValueError("Error: DNA must have at least 1 string.")

        self.sq = self.sq.upper()
        for nucleotide in self.sq:
            if nucleotide not in self.valid_nucleotides:
                raise ValueError(f"Error: Invalid nucleotide found: '{nucleotide}'")


