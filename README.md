# bitmap-cli-transformer

**Author**: Jasime Arensdorf, Tim Schoen, Dan Le, Milo Anderson, Paul Williamsen, Chris Ball, Evy Haan, Andrew Helmer
**Version**: 1.0.0

## Overview
This application is a Bitmap transformer. It will read a Bitmap file in and run image transforms: grayscale, inverse colors, flip vertically, flip horizontally, and resize to thumbnail. The transformed image will be written to a new .bmp file.

## Getting Started
- When the user runs the program, they will see which transform options are available.
- The following arguments must be entered: input file path (required) and up to five transform options (at least one is required).
- The CLI will run the number of transformations the user requests and save the transformed image into new files.
- Either a message for a completed transform or an incorrect transform must be displayed.

## Architecture
Python, Cmd module, Pillow module, and Pytest.

## API
No APIs used.

## Attributions
https://www.tutorialspoint.com/python/python_command_line_arguments.htm
