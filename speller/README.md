Spell Checker
Overview
This project implements a spell checker using a hash table. It allows you to load a dictionary of words and check the spelling of words in a text file. The spell checker reports misspelled words and provides performance benchmarks for loading the dictionary, checking words, determining the dictionary's size, and unloading the dictionary.

Files
speller.c: Main program to perform spell checking.
dictionary.h: Header file declaring the dictionary's functions.
dictionary.c: Contains the implementation of the dictionary functions.
Makefile: Automates the build process.
Installation
To compile the spell checker, ensure you have a C compiler installed (e.g., gcc) and execute the following command:

bash
make speller
This will compile speller.c and dictionary.c into an executable named speller.

Usage
To run the spell checker, use the following command:

bash
./speller [DICTIONARY] text
DICTIONARY (optional): Path to the dictionary file containing a list of words, one per line. If omitted, the default dictionary located at dictionaries/large will be used.
text: Path to the text file to be spell-checked.
Example usage:

bash
./speller dictionaries/large text.txt
This command will load the dictionary from dictionaries/large and check the spelling of words in text.txt.

Implementation
Dictionary Functions
bool check(const char *word);
Checks if the word is in the dictionary.
unsigned int hash(const char *word);
Hashes the word to a bucket index in the hash table.
bool load(const char *dictionary);
Loads the dictionary from the file into memory.
unsigned int size(void);
Returns the number of words in the dictionary.
bool unload(void);
Unloads the dictionary from memory, freeing up all allocated memory.
Hash Table
The hash table uses chaining for collision resolution. Each bucket in the hash table points to a linked list of nodes, where each node represents a word in the dictionary.

Hash Function
The current hash function is a basic example. It computes a bucket index based on the first and last characters of the word. This can be improved for better distribution.

Performance Metrics
The program measures and reports the following timings:

TIME IN load: Time taken to load the dictionary.
TIME IN check: Time taken to check all words in the text.
TIME IN size: Time taken to determine the size of the dictionary.
TIME IN unload: Time taken to unload the dictionary from memory.
TIME IN TOTAL: Total time taken for all operations.
Testing
You can test the spell checker with various texts and dictionaries provided in the texts directory. The dictionaries/small file contains a smaller dictionary for easier testing.

Memory Management
The implementation ensures no memory leaks by properly freeing allocated memory in the unload function. Use valgrind to check for memory leaks:

bash
valgrind --leak-check=full ./speller dictionaries/large text.txt