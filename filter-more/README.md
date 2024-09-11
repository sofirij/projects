Filter-More
Overview
This project allows you to apply various image filters to 24-bit BMP files. The filters implemented include grayscale, reflection, blur, and edge detection. The program works by manipulating the RGB values of each pixel in the BMP file to produce the desired visual effect.

Problem to Solve
Images are essentially grids of pixels, each with a specific color represented by values for red, green, and blue (RGB). By manipulating these RGB values, different filters can be applied to an image, creating effects such as grayscale, reflection, blurring, and edge detection.

Supported Filters:
Grayscale: Converts the image to black and white by setting each pixel’s RGB values to the average of the original RGB values, giving a uniform gray shade.

Reflection: Reflects the image horizontally, creating a mirror effect.

Blur: Applies a box blur effect by averaging the RGB values of each pixel’s surrounding pixels in a 3x3 grid.

Edges: Detects edges in the image using the Sobel operator, highlighting boundaries between objects.

Project Structure
The project is composed of the following key files:

bmp.h: Defines data structures for BMP headers and pixel data.
filter.c: Contains the main function and command-line parsing logic.
helpers.c: Contains the implementation of the filters (functions for grayscale, reflection, blur, and edge detection).
helpers.h: Provides prototypes for the filter functions.
Makefile: Specifies how to compile the program.
Implementation Details
Grayscale Filter
The grayscale filter sets each pixel’s RGB values to the average of its original RGB values, converting it to a shade of gray.
Reflection Filter
The reflection filter swaps pixels horizontally within each row of the image to achieve a mirror effect.
Blur Filter
The blur filter computes the average RGB values of each pixel’s neighboring pixels within a 3x3 grid, applying a softening effect.
Edges Filter
The edges filter uses the Sobel operator to detect edges by calculating the gradient in both horizontal (Gx) and vertical (Gy) directions. It combines these gradients to determine the final edge intensity.
Compilation and Usage
Compilation
To compile the project, navigate to the project directory and run:

bash
make filter
Usage
To apply a filter to an image, use the following command syntax:

bash
./filter -[filter] [input.bmp] [output.bmp]
Replace [filter] with one of the following options:

-g for grayscale
-r for reflection
-b for blur
-e for edge detection
Replace [input.bmp] with the path to the input BMP file, and [output.bmp] with the desired output file name.

Example Commands
Grayscale an image:

bash
./filter -g images/yard.bmp out.bmp
Reflect an image:

bash
./filter -r images/yard.bmp out.bmp
Blur an image:

bash
./filter -b images/yard.bmp out.bmp
Detect edges in an image:

bash
./filter -e images/yard.bmp out.bmp
Assumptions and Constraints
The input images are 24-bit BMP files.
The filters operate directly on RGB values as defined by the BMP format.
Images are represented as 2D arrays of pixels, allowing easy manipulation of pixel data.
Edge pixels are handled as if surrounded by a black border (0 RGB values) during blur and edge detection calculations.
Hints
Ensure values for RGB channels are integers, rounding any calculations where necessary.
Be mindful of edge and corner cases, particularly for blur and edge detection filters.
Conclusion
This project demonstrates the fundamental principles of image processing using low-level pixel manipulation in C. By implementing grayscale, reflection, blur, and edge detection filters, the program showcases how images can be transformed using basic computational technique