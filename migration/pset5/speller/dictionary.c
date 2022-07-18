// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <string.h>
#include <ctype.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

//number of words
int count = 0;
// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    if (word == NULL)
    {
        return false;
    }
    for (int i = 0; i < N; i++)
    {
        node *p = table[i];
        while (hash(word) == i && p != NULL)
        {
            if (strcasecmp(p->word, word) == 0)
            {
                return true;
            }
            p = p->next;
        }

    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    if (word == NULL)
    {
        return 27;
    }
    return tolower(word[0]) % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    FILE *input = fopen(dictionary, "r");
    if (input != NULL)
    {
        char word[LENGTH + 1];
        int k = 0;
        while (fscanf(input, "%s", word) != EOF)
        {
            node *n = malloc(sizeof(node));
            if (n == NULL)
            {
                return false;
            }
            strcpy(n->word, word);
            n->next = NULL;
            if (table[hash(word)] == NULL)
            {
                table[hash(word)] = n;
                count++;
            }
            else
            {
                node *tmp = table[hash(word)]->next;
                table[hash(word)]->next = n;
                n->next = tmp;
                count++;
            }
            for (int i = 0; i < LENGTH; i++)
            {
                word[i] = 0;
            }
            if (hash(word) == 2)
            {
                k++;
            }
        }
        fclose(input);
        return true;
    }
    fclose(input);
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        node *p = table[i];
        node *tmp = NULL;
        while (p != NULL)
        {
            tmp = p;
            p = p->next;
            free(tmp);
        }
    }
    return true;
}
