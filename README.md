# INF_Project-1 (INF502)
## Team Members
Monique Parrish 

Hien Nguyen


## DNA Similarity Analysis Project
### Approach to Solving the Problem
Our approach to solving the DNA similarity analysis problem involved breaking down the task into several key components:

- Input Handling: We created a module (input_sequence.py) to manage DNA sequence input, including validation and error handling.

- Sequence Comparison: We developed algorithms for comparing DNA sequences, including shifting and finding matches (find_number_match.py).

- User Interface: We implemented a menu-driven interface in the main program (module1project.py) to guide users through the analysis process.

- Modular Design: We separated functionality into different modules for better organization and maintainability.

### Key Components
1. input_sequence.py

This module handles the input and validation of DNA sequences. It includes:
- A custom InvalidNucleotideError exception for handling invalid nucleotides.
- Functions to validate DNA sequences, ensuring they contain only valid nucleotides (A, T, G, C).
- Methods to input sequences from either console or file, with appropriate error handling.

2. find_number_match.py

This module contains functions for comparing and analyzing DNA sequences:
- A function to compare two sequences and count matching nucleotides.
- An algorithm to shift sequences and generate all possible alignments up to a specified maximum shift.
- Methods to find and display the maximum number of matches between two sequences, considering various shifts.

3. module1project.py

This is the main program that provides the user interface and orchestrates the DNA similarity analysis:
- An introduction function to display program details.
- A menu system allows users to input sequences, compare them, and find maximum matches.
- The main loop drives the program, handling user inputs and calling appropriate functions.
### Example Usage and Results
The program allows users to:
- Input DNA sequences via console or file.
- Compare sequences without shifts.
- Find maximum matches by shifting sequences.
- View current sequences.
- An example run might involve inputting two sequences ("ATCG" and "TCGA"), comparing them without shifts, and then finding maximum matches with automatic shifting.
### Hurdles and Benefits
#### Hurdles
- Input Validation: Ensuring robust input validation for DNA sequences was challenging. We created a custom exception and used a set of valid nucleotides to handle this.
- Shift Algorithm: Developing an efficient algorithm to shift sequences and compare them required careful consideration.
- User Interface: Creating a user-friendly interface that guided users through the process while handling potential errors was complex.
- File Handling: Implementing file input requires error handling for various scenarios such as a file not being found or an incorrect file format.
#### Benefits
- Modularity: Separating the code into different modules improved maintainability and readability.
- Flexibility: The program allows users to input sequences through a console or file, providing flexibility in data input methods.
- Error Handling: Comprehensive error handling with specific exception types ensures the program behaves predictably even with invalid inputs.
- Scalability: The modular design allows for easily adding new features or improvements to existing functionality.
- Educational Value: This project provides practical experience in bioinformatics concepts and Python programming, including file I/O, error handling, and algorithm design.

By addressing these challenges and leveraging the benefits of our approach, we created a robust and user-friendly tool for DNA similarity analysis, demonstrating the application of programming concepts to real-world scientific problems.
