// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef uint8_t byte;
typedef int16_t byte_2;

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    byte *buffer1 = malloc(HEADER_SIZE);
    if (buffer1 == NULL)
    {
        return 1;
    }

    if (fread(buffer1, HEADER_SIZE, 1, input))
    {
        fwrite(buffer1, HEADER_SIZE, 1, output);
    }

    free(buffer1);

    // TODO: Read samples from input file and write updated data to output file
    byte_2 *buffer2 = malloc(2);
    if (buffer2 == NULL)
    {
        return 1;
    }

    while (fread(buffer2, 2, 1, input))
    {
        *buffer2 *= factor;
        fwrite(buffer2, 2, 1, output);
    }
    free(buffer2);

    // Close files
    fclose(input);
    fclose(output);
}
