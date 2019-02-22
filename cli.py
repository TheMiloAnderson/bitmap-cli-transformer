import cmd,sys
from modify import Bitmap

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

input_file_path = sys.argv[1]
transforms = sys.argv[2:]

bitmap = Bitmap(input_file_path)
bitmap.make_grayscale()
for transform in transforms:
    method = getattr(bitmap, transform)
    method()
