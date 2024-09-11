Recover
Overview
The goal of this project is to recover JPEG images from a forensic image of a memory card. The forensic image, named card.raw, is a binary file that contains the raw bytes from the memory card. The task is to identify and extract JPEG files from this image based on specific byte patterns and save them as separate JPEG files.

Problem to Solve
JPEG files have a distinctive signature in their byte sequence. The first four bytes of a JPEG file are:

0xff 0xd8 0xff followed by
0xe0, 0xe1, 0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xeb, 0xec, 0xed, 0xee, or 0xef in hexadecimal notation.
To recover JPEG files, we need to:

Read the forensic image (card.raw) in blocks of 512 bytes.
Detect the start of JPEG files based on their signature.
Write the detected JPEG data to separate files.
Ensure that JPEG files are contiguous and write each one sequentially.
Implementation Details
Reading the Forensic Image
The program reads the forensic image in chunks of 512 bytes.
Each chunk is processed to check for the JPEG signature.
JPEG Detection
The JPEG signature is checked in the first four bytes of each 512-byte block.
When a JPEG signature is detected, a new file is created to write the JPEG data.
The JPEG file is written until the next JPEG signature is detected or the end of the forensic image is reached.
File Naming
Files are named ###.jpg, where ### is a three-digit number starting from 000 and incrementing for each recovered image.
Memory Management
The program must manage memory efficiently and avoid memory leaks.
Proper error handling is included to manage file operations and memory allocation.
Specifications
The program must be implemented in recover.c.
It should accept exactly one command-line argument: the name of the forensic image file.
The program should handle errors gracefully, such as incorrect usage or inability to open the forensic image.
Usage
Compilation
To compile the program, navigate to the recover directory and run:

bash
make recover
Running the Program
To run the program and recover JPEG files from card.raw, use the following command:

bash
./recover card.raw
Replace card.raw with the path to the forensic image file if it is located elsewhere.

Error Handling
If no command-line argument is provided, the program will display usage information and return 1.
If the forensic image cannot be opened, the program will inform the user and return 1.
Example
bash
./recover card.raw
This command will read card.raw, recover JPEG files, and save them as 000.jpg, 001.jpg, 002.jpg, etc., in the current directory.

Additional Notes
The forensic image may contain slack space filled with zeros, which may appear in the recovered JPEG files but should not affect their viewability.
The program assumes that JPEGs are stored contiguously and that any slack space will be filled with zeros.
Conclusion
The recover program is designed to identify and extract JPEG files from a forensic image of a memory card by detecting specific byte patterns and handling the recovered data efficiently. This approach allows for the recovery of lost photos from a memory card using basic file I/O operations and memory management in C.
