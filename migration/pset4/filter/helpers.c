#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;
            // average
            int avg = round((red + green + blue) / 3);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;
            // sepia red
            int sred = round(0.393 * red + 0.769 * green + 0.189 * blue);
            if (sred > 255)
            {
                sred = 255;
            }
            // sepia green
            int sgreen = round(0.349 * red + 0.686 * green + 0.168 * blue);
            if (sgreen > 255)
            {
                sgreen = 255;
            }
            // sepia blue
            int sblue = round(0.272 * red + 0.534 * green + 0.131 * blue);
            if (sblue > 255)
            {
                sblue = 255;
            }
            image[i][j].rgbtRed = sred;
            image[i][j].rgbtGreen = sgreen;
            image[i][j].rgbtBlue = sblue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        // new last pixel pointer
        int last = width - 1;
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE buffer = image[i][j];
            image[i][j] = image [i][last];
            image[i][last] = buffer;
            last--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE buffer[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //making blurred pixels
            buffer[i][j] = image[i][j];
            float avgRed = 0;
            float avgBlue = 0;
            float avgGreen = 0;
            //divider
            float dzielnik = 0;
            for (int k = -1; k < 2; k++)
            {
                for (int l = -1; l < 2; l++)
                {
                    // not taking pixels out of range
                    if (i + k != -1 && j + l != -1 && i + k != height && j + l != width)
                    {
                        avgRed += image[(i + k)][(j + l)].rgbtRed;
                        avgBlue += image[(i + k)][(j + l)].rgbtBlue;
                        avgGreen += image[(i + k)][(j + l)].rgbtGreen;
                        dzielnik++;
                    }
                }
            }
            buffer[i][j].rgbtRed = round(avgRed / dzielnik);
            buffer[i][j].rgbtBlue = round(avgBlue / dzielnik);
            buffer[i][j].rgbtGreen = round(avgGreen / dzielnik);
        }
    }
    // making new image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = buffer[i][j];
        }
    }
    return;
}
