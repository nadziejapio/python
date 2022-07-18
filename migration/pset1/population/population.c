#include <cs50.h>
#include <stdio.h>


int main(void)
{
    // TODO: Prompt for start size

    int n;
    do
    {
        n = get_int("Start size:");
    }
    while (n < 9);

    // TODO: Prompt for end size
    int m;
    do
    {
        m = get_int("End size:");
    }
    while (m < n);

    // TODO: Calculate number of years until we reach threshold
    int i = 0;
    for (; n < m; i++)
    {
        int born = n / 3;
        int dies = n / 4;
        n += born - dies;
    }
    // TODO: Print number of years
    printf("Years: %i\n", i);
}
