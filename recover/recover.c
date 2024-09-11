#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t byte;

int main(int argc, char *argv[])
{
    //a block is 512 bytes
    //a jpeg starts with 0xff 0xd8 0xff then the first 4 bits of the fourth byte are 1110
    //where a photo ends another begins

    if (argc != 2)
    {
        printf("Improper command line arguments\n");
        return 1;
    }

    FILE *input = fopen(argv[1], "rb");
    if (input == NULL)
    {
        printf("File cannot be opened\n");
        return 1;
    }

    byte *block = malloc(512);
    if (block == NULL)
    {
        return 1;
    }

    int count = 0;
    FILE *output = NULL;

    while (fread(block, 512, 1, input))
    {
        if(block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff)
        {
                if (output != NULL)
                {
                    fclose(output);
                }

                char filename[8];
                sprintf(filename, "%03i.jpg", count);
                output = fopen(filename, "wb");
                count++;
                if (output == NULL)
                {
                    free(block);
                    fclose(input);
                    return 1;
                }
        }

        if (output != NULL)
        {
            fwrite(block, 512, 1, output);
        }
    }

    if (output != NULL)
    {
        fclose(output);
    }
    fclose(input);
    free(block);
    printf("%d\n", count);


}
