Inheritance
Overview
The inheritance project simulates the genetic inheritance of blood types over multiple generations. Each person’s blood type is determined by two alleles, inherited from their parents. This program creates a family tree of a specified number of generations, assigns blood type alleles, and outputs the family tree.

Problem to Solve
The blood type of an individual is determined by their alleles, with possible alleles being A, B, or O. Each person inherits one allele from each parent. The goal is to simulate this inheritance across multiple generations and generate a family tree showing the blood types of each family member.

Blood Type Combinations
The possible blood type combinations are:

OO, OA, OB
AO, AA, AB
BO, BA, BB
Example
If one parent has the blood type AO and the other has BB, the possible blood types for their child could be AB and OB. If one parent has AO and the other OB, the child could potentially have any of the combinations: AO, OB, AB, or OO.

Implementation Details
Functions
create_family:

Purpose: Creates a family tree with a given number of generations and assigns blood type alleles to each member.
Parameters: An integer generations representing the number of generations.
Returns: A pointer to the person structure in the youngest generation.
Details:
Allocates memory for a new person structure.
Recursively creates two parents if generations > 1.
Randomly assigns alleles for the current person based on their parents' alleles.
If generations == 1, randomly assigns alleles and sets parents to NULL.
random_allele:

Purpose: Randomly generates a blood type allele.
Returns: A character representing one of the alleles ('A', 'B', or 'O').
free_family:

Purpose: Frees the memory allocated for the family tree.
Parameters: A pointer to the person structure in the youngest generation.
Details:
Recursively frees the memory for each person's parents.
Frees the memory for the current person.
print_family:

Purpose: Prints the family tree and blood types for each person.
Parameters: A pointer to the person structure and an integer generation indicating the current generation level.
Details:
Prints each family member's blood type with appropriate indentation based on their generation.

Data Structures
person:
Fields:
alleles[2]: An array of two characters representing the blood type alleles.
parents[2]: An array of pointers to person structures representing the parents.
Example of create_family Function
Allocates memory for a new person.
Recursively creates two parents if there are more generations to simulate.
Sets the parent pointers and randomly assigns alleles based on parents' alleles.
If the current generation is the oldest, sets parent pointers to NULL and randomly assigns alleles.
Example of free_family Function
Handles the base case where the pointer is NULL.
Recursively frees the parents before freeing the current person.
Usage
Compilation
To compile the program, navigate to the inheritance directory and run:

bash
make inheritance
Running the Program
To run the program and simulate the inheritance, use:

bash
./inheritance
Output
The program will generate and print a family tree with the specified number of generations, showing the blood type of each family member.

Example Output
For GENERATIONS = 3, the output might look like:

bash
Child (Generation 0): blood type AO
    Parent (Generation 1): blood type AB
        Grandparent (Generation 2): blood type OO
        Grandparent (Generation 2): blood type BB
    Parent (Generation 1): blood type OA
        Grandparent (Generation 2): blood type OO
        Grandparent (Generation 2): blood type AA
Additional Notes
Ensure that the GENERATIONS constant is defined as needed. In the provided code, it's set to 3.
Proper memory management is crucial to avoid memory leaks. Ensure that all allocated memory is freed by calling free_family.
Conclusion
The inheritance program effectively simulates the genetic inheritance of blood types over multiple generations, creates a family tree, and prints the blood types for each family member. Accurate implementation of the create_family, random_allele, free_family, and print_family functions is essential for the correct execution of the program.

