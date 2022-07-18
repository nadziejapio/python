#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

int main(void)
{
    //get text
    string s = get_string("Text:");
    int c = 0;
    int w = 0;
    int p = 0;

    for (int i = 0; strlen(s) > i; i++)
    {
        // letters
        if ((s[i] < 91 && s[i] > 64) || (s[i] < 123 && s[i] > 96))
        {
            c++;
        }
        // words
        if (s[i] == ' ')
        {
            w++;
        }
        // sentences
        if (s[i] == '.' || s[i] == '?' || s[i] == '!')
        {
            p++;
        }

    }
    float x = 0;
    float L = (float)c / (float)(w + 1) * 100;
    float S = (float)p / (float)(w + 1) * 100;
    // index = 0.0588 * L - 0.296 * S - 15.8
    x = 0.0588 * L - 0.296 * S - 15.8;
    int g = round(x);
    if (x > 16)
    {
        printf("Grade 16+\n");
    }
    else if (x < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", g);
    }
}

