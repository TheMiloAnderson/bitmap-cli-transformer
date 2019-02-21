import struct
from PIL import Image


# img = Image.open('./assets/tiger.bmp').convert('L')

# img.show()

# img.save('./assets/new_tiger.bmp', 'bmp')


class Bitmap(object):
    def __init__(self, file_path):
        """
        Reads original image based on filepath.
        """
        # self.img = Image.open(file_path)
        self.file_path = file_path
        """
        self.memory_view = memoryview(self.source)

        self.offset = struct.unpack('I', self.memory_view[10:14].tobytes())[0]
        self.color_table = self.memory_view[54:self.offset]
        self.pixel_array = self.memory_view[self.offset:] """

    @classmethod
    def read_file(cls, origin):
        """Class Method which consumes a file path as input, and returns a Bitmap instance.
        """
        pass

    def new_file_path(self, mod_type):
        self.split_name = self.file_path.split('.')
        self.split_name[1] += f'{mod_type}'
        self.dot = '.'
        return self.dot.join(self.split_name)

    def make_grayscale(self):
        self.new_path = self.new_file_path('_grayscale')
        self.img = Image.open(self.file_path).convert('L')
        self.img.save(self.new_path, 'bmp')

    def flip_horizontal(self):
        self.new_path = self.new_file_path('_horizonal')
        self.img = Image.open(self.file_path).transpose(Image.FLIP_LEFT_RIGHT)
        self.img.save(self.new_path, 'bmp')

    def flip_vertical(self):
        self.new_path = self.new_file_path('_vertical')
        self.img = Image.open(self.file_path).transpose(Image.FLIP_TOP_BOTTOM)
        self.img.save(self.new_path, 'bmp')

    # def make_(self):
    #     self.img = Image.open(self.file_path).convert('L')
    #     self.img.save('./assets/new_tiger.bmp', 'bmp')

    # def write_file(self, target):
    #     """Instance Method which accepts a target file path and writes the instance source data to target path.
    #     """
    #     with open(target, 'wb') as file:
    #         file.write(self.source)

    # def get_headers(self):
    #     """Instance Method which provides instance source data as readable output to std out.
    #     """
    #     import struct as s
    #     result = f'''
    #         Type: {s.unpack('I', self.memory_view[0:2].tobytes())[0]}
    #         Size: {s.unpack('I', self.memory_view[2:6].tobytes())[0]}
    #         Reserved 1: {s.unpack('H', self.memory_view[6:8].tobytes())[0]}
    #         Reserved 2: {s.unpack('H', self.memory_view[8:10].tobytes())[0]}
    #         Offset: {s.unpack('I', self.memory_view[10:14].tobytes())[0]}
    #         DIB Header Size: {s.unpack('I', self.memory_view[14:18].tobytes())[0]}
    #         Width: {s.unpack('I', self.memory_view[18:22].tobytes())[0]}
    #         Height: {s.unpack('I', self.memory_view[22:26].tobytes())[0]}
    #         Colour Planes: {s.unpack('H', self.memory_view[26:28].tobytes())[0]}
    #         Bits per Pixel: {s.unpack('H', self.memory_view[28:30].tobytes())[0]}
    #         Compression Method: {s.unpack('I', self.memory_view[30:34].tobytes())[0]}
    #         Raw Image Size: {s.unpack('I', self.memory_view[34:38].tobytes())[0]}
    #         Horizontal Resolution: {s.unpack('I', self.memory_view[38:42].tobytes())[0]}
    #         Vertical Resolution: {s.unpack('I', self.memory_view[42:46].tobytes())[0]}
    #         Number of Colours: {s.unpack('I', self.memory_view[46:50].tobytes())[0]}
    #         Important Colours: {s.unpack('I', self.memory_view[50:54].tobytes())[0]}
    #     '''
    #     return result

    # TODO: Write your instance methods for transformations here as part of the Bitmap class.


tiger = Bitmap('./assets/tiger.bmp')

tiger.make_grayscale()
tiger.flip_horizontal()
tiger.flip_vertical()
