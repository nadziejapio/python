#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

// is argument a digit
bool isint(string wyraz)
{
    for (int i = 0; strlen(wyraz) > i; i++)
    {
        if (!isdigit(wyraz[i]))
        {
            return false;
        }
    }
    return true;
}

int main(int argc, string argv[])
{


    if (argc == 2 && isint(argv[1]) && atoi(argv[1]) > 0)
    {
        // get plaintext
        string input = get_string("plaintext: ");
        string output = input;
        //printing outtext
        printf("ciphertext: ");
        // char by char
        for (int i = 0; strlen(input) > i; i++)
        {
            if (input[i] < 91 && input[i] > 64)
            {
                char c = input[i] - 65;
                c = (c + atoi(argv[1])) % 26;
                c = c + 65;
                printf("%c", c);
            }
            else if (input[i] < 123 && input[i] > 96)
            {
                char c = input[i] - 97;
                c = (c + atoi(argv[1])) % 26;
                c = c + 97;
                printf("%c", c);
            }

            else
            {
                printf("%c", input[i]);
            }
        }
        printf("\n");
        // good
        return 0;
    }

    else
    {
        printf("Usage: ./caesar key\n");
        //error
        return 1;
    }
}

