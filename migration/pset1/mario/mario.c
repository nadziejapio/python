#include <stdio.h>
#include <cs50.h>
// #maker
void hash(int i)
{

    for (int j = 0; j < i; j++)
    {
        printf("#");
    }

}

int main(void)
{
    int n;
    // getting height
    do
    {
        n = get_int("Height: \n");
    }
    while (n < 1 || n > 8);
    //loop
    for (int i = 1; i < n + 1 ; i++)
    {
        for (int k = n; k > i; k--)
        {
            printf(" ");
        }
        hash(i);
        printf("\n");
    }
}