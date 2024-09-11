# Volume

## Overview

`volume.c` is a program designed to modify the volume of audio files in WAV format. WAV files store audio data as a sequence of 16-bit samples, each representing the value of the audio signal at a specific point in time. By scaling these samples by a specified factor, the volume of the audio can be adjusted—either increased or decreased.

This program reads an input WAV file, modifies its samples by a given factor, and writes the result to a new output WAV file.

## Problem to Solve

WAV files consist of a 44-byte header followed by audio samples, each represented as a 16-bit integer. By multiplying each sample value by a factor, the volume of the audio can be changed. For example:

- Multiplying by `2.0` doubles the volume.
- Multiplying by `0.5` halves the volume.

The goal is to modify the volume of an input audio file and save the changes in a new output file.

## Implementation Details

The program accepts three command-line arguments:

1. `input` - The name of the original audio file (WAV format).
2. `output` - The name of the new audio file to be generated.
3. `factor` - The scaling factor to adjust the volume.

### Program Workflow

1. The program reads the 44-byte header from the input file and writes it unchanged to the output file.
2. It reads each audio sample (16-bit signed integer) from the input file, scales it by the given factor, and writes the modified sample to the output file.

### Assumptions

- The WAV file uses 16-bit signed samples.
- The program correctly handles memory without leaks (no use of `malloc` that leads to memory leaks).

## Usage

### Compilation

To compile the program, navigate to the folder containing `volume.c` and run:

```bash
gcc -o volume volume.c -lm

Running the Program
To run the program, use the following command:

bash
./volume input.wav output.wav factor
input.wav: The path to the input WAV file.
output.wav: The path where the modified WAV file will be saved.
factor: The scaling factor for volume adjustment (e.g., 2.0 to double the volume, 0.5 to halve it).
Example
bash
./volume input.wav output.wav 2.0
This command doubles the volume of input.wav and saves the modified audio as output.wav.

Example Files
input.wav: Example input file with normal volume.
output.wav: Example output file with modified volume.