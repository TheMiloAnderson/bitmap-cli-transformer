import cmd,sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

input_file_path = sys.argv[2]
output_file_path = sys.argv[3]
transform = sys.argv[4]