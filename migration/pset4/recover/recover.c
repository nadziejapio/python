#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    //check if 2 args
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    //check if file opens
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("File can't be open.\n");
        return 1;
    }
    // make buffer for name
    char buffer[8];
    // names counter
    int i = 0;
    // bytes array
    uint8_t bytes[512];
    FILE *output = NULL;
    //check if there are bytes left
    int readbytes = fread(bytes, sizeof(uint8_t), 512, file);
    int isjpg = 0;
    while (readbytes > 0)
    {
        // is jpg?
        if (bytes[0] == 0xff && bytes[1] == 0xd8 && bytes[2] == 0xff && (bytes[3] & 0xf0) == 0xe0)
        {
            //1st file
            if (i == 0)
            {
                sprintf(buffer, "%03i.jpg", i);
                output = fopen(buffer, "w");
                i++;
            }
            //next files
            else
            {
                fclose(output);
                sprintf(buffer, "%03i.jpg", i);
                output = fopen(buffer, "w");
                i++;
            }
            isjpg = 1;
        }
        //write those bytes
        if (isjpg == 1)
        {
            fwrite(bytes, sizeof(uint8_t), readbytes, output);
        }
        //read rest bytes
        readbytes = fread(bytes, sizeof(uint8_t), 512, file);
    }
    fclose(file);
    fclose(output);
}