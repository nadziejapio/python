#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    //type
    float c;
    // get change
    do
    {
        c = get_float("Change owed: ");
    }
    while (c <= 0);
    c = round(c * 100);
    int q = c / 25;
    int d = (c - (q * 25)) / 10;
    int n = (c - (q * 25) - (d * 10)) / 5;
    int p = c - (q * 25) - (d * 10) - (n * 5);
    // how many coins you have to give
    printf("%i\n", q + d + n + p);
}