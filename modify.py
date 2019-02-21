import struct
from PIL import Image


class Bitmap(object):
    def __init__(self, file_path):
        """
        Records original file path.
        """
        self.file_path = file_path
        """
        self.memory_view = memoryview(self.source)
        self.offset = struct.unpack('I', self.memory_view[10:14].tobytes())[0]
        self.color_table = self.memory_view[54:self.offset]
        self.pixel_array = self.memory_view[self.offset:]
        """

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


tiger = Bitmap('./assets/tiger.bmp')
tiger.make_grayscale()
tiger.flip_horizontal()
tiger.flip_vertical()
