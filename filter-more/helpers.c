#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //for each pixel the new rgb value is the average of the previous rgb values
    //if above 255 round to 255
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);

            if (average > 255)
            {
                average = 255;
            }

            image[i][j].rgbtRed = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtBlue = average;
        }
    }

}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp;
    //for each row just reverse the array of pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width/2; j++)
        {
            temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //create the temp pixel values
    int tempRed;
    int tempBlue;
    int tempGreen;
    int count;

    //create a copy of the image that will be used to calculate the values
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tempRed = 0;
            tempGreen = 0;
            tempBlue = 0;
            count = 0;

            for (int k = i-1; k <= i+1; k++)
            {
                for (int l = j-1; l <= j+1; l++)
                {
                    if ((k >= 0 && k < height) && (l >= 0 && l < width))
                    {
                        tempRed += copy[k][l].rgbtRed;
                        tempGreen += copy[k][l].rgbtGreen;
                        tempBlue += copy[k][l].rgbtBlue;
                        count++;
                    }
                }
            }

            tempRed = round(tempRed / (float)count);
            tempGreen = round(tempGreen / (float)count);
            tempBlue = round(tempBlue / (float)count);

            if (tempRed > 255)
            {
                tempRed = 255;
            }
            if (tempGreen > 255)
            {
                tempGreen = 255;
            }
            if (tempBlue > 255)
            {
                tempBlue = 255;
            }


            image[i][j].rgbtRed = tempRed;
            image[i][j].rgbtGreen = tempGreen;
            image[i][j].rgbtBlue = tempBlue;
        }
    }
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    float redGx, greenGx, blueGx;
    float redGy, greenGy, blueGy;

    int arrayGx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int arrayGy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    int tempRed, tempGreen, tempBlue;

    int indexX, indexY;

    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            redGx = 0, greenGx = 0, blueGx = 0;
            redGy = 0, greenGy = 0, blueGy = 0;

            indexX = 0, indexY = 0;

            for (int k = i - 1; k <= i + 1; k++)
            {
                for (int l = j - 1; l <= j + 1; l++)
                {
                    if ((k >= 0 && k < height) && (l >= 0 && l < width))
                    {
                        redGx += copy[k][l].rgbtRed * arrayGx[indexY][indexX];
                        greenGx += copy[k][l].rgbtGreen * arrayGx[indexY][indexX];
                        blueGx += copy[k][l].rgbtBlue * arrayGx[indexY][indexX];
                        redGy += copy[k][l].rgbtRed * arrayGy[indexY][indexX];
                        greenGy += copy[k][l].rgbtGreen * arrayGy[indexY][indexX];
                        blueGy += copy[k][l].rgbtBlue * arrayGy[indexY][indexX];
                    }
                    else
                    {
                        redGx += 0 * arrayGx[indexY][indexX];
                        greenGx += 0* arrayGx[indexY][indexX];
                        blueGx += 0 * arrayGx[indexY][indexX];
                        redGy += 0 * arrayGy[indexY][indexX];
                        greenGy += 0 * arrayGy[indexY][indexX];
                        blueGy += 0 * arrayGy[indexY][indexX];
                    }
                    indexX++;
                }
                indexY++;
                indexX = 0;
            }

            tempRed = round(sqrt(pow(redGx, 2) + pow(redGy, 2)));
            tempGreen = round(sqrt(pow(greenGx, 2) + pow(greenGy, 2)));
            tempBlue = round(sqrt(pow(blueGx, 2) + pow(blueGy, 2)));

            if (tempRed > 255)
            {
                tempRed = 255;
            }
            if (tempGreen > 255)
            {
                tempGreen = 255;
            }
            if (tempBlue > 255)
            {
                tempBlue = 255;
            }

            image[i][j].rgbtRed = tempRed;
            image[i][j].rgbtGreen = tempGreen;
            image[i][j].rgbtBlue = tempBlue;
        }
    }

}



