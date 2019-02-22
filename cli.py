import cmd
import sys
from modify import Bitmap


print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

if len(sys.argv) < 3:
    print("""
    *************************************************
    ***    Not enough parameters. Please enter    ***
    ***  the file path and at least 1 transform.  ***
    *************************************************
    """)
else:
    input_file_path = sys.argv[1]
    transforms = sys.argv[2:]


bitmap = Bitmap(input_file_path)
bitmap.make_grayscale()
for transform in transforms:
    method = getattr(bitmap, transform)
    bitmap.save_new(method())

