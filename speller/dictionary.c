// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
#include <stdio.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 1001;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);
    node *pointer = table[index];

    while (pointer != NULL)
    {
        if (!strcasecmp(word, pointer->word))
        {
            return true;
        }
        pointer = pointer->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    if (strlen(word) > 1 && isalpha(word[strlen(word) - 1]))
    {
        return (((toupper(word[0]) - 'A') + (toupper(word[strlen(word) - 1]) - 'A')) / 50.0) * 1000;
    }
    else
    {
        return ((toupper(word[0]) - 'A') / 50.0) * 1000;
    }
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    int index;
    //open the file that contains the words to be hashed
    FILE *input = fopen(dictionary, "r");
    if (input == NULL)
    {
        return false;
    }

    //create the buffer that will store the read words
    char buffer[LENGTH + 1];

    //keep reading till the end of the file
    while(fscanf(input, "%s", buffer) != EOF)
    {
        //hash and add to the hash table
        node *new_word = malloc(sizeof(node));
        if (new_word == NULL)
        {
            unload();
            fclose(input);
            return false;
        }

        index = hash(buffer);
        new_word->next = table[index];
        strcpy(new_word->word, buffer);
        table[index] = new_word;
    }

    fclose(input);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    int count = 0;
    node *pointer;
    for (int i = 0; i < 1001; i++)
    {
        pointer = table[i];
        while (pointer != NULL)
        {
            count++;
            pointer = pointer->next;
        }
    }
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *pointer;
    node *temp;
    for (int i = 0; i < 1001; i++)
    {
        pointer = table[i];

        while (pointer != NULL)
        {
            temp = pointer->next;
            free(pointer);
            pointer = temp;
        }
    }

    return true;
}
