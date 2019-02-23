import struct
from PIL import Image, ImageOps


class Bitmap(object):
    def __init__(self, file_path):
        """
        Records original file path.
        """
        self.file_path = file_path
        self.img = Image.open(self.file_path)
        """
        self.memory_view = memoryview(self.source)
        self.offset = struct.unpack('I', self.memory_view[10:14].tobytes())[0]
        self.color_table = self.memory_view[54:self.offset]
        self.pixel_array = self.memory_view[self.offset:]
        """

    def new_file_path(self, mod_type):
        split_name = self.file_path.split('.')
        split_name[1] += f'{mod_type}'
        return '.'.join(split_name)

    def make_grayscale(self, img='self.img'):
        new_path = self.new_file_path('_grayscale')
        img = self.img.convert('L')
        return [new_path, img]

    def flip_horizontal(self, img='self.img'):
        new_path = self.new_file_path('_horizontal')
        img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        return [new_path, img]

    def flip_vertical(self, img='self.img'):
        new_path = self.new_file_path('_vertical')
        img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        return [new_path, img]

    def invert_colors(self, img='self.img'):
        new_path = self.new_file_path('_invert')
        img = ImageOps.invert(self.img)
        return [new_path, img]

    def make_thumbnail(self, img='self.img'):
        new_path = self.new_file_path('_thumbnail')
        size = 128, 128
        img = self.img.copy()
        img.thumbnail(size)
        return [new_path, img]

    def save_new(self, lst):
        lst[1].save(lst[0], 'bmp')

if __name__ == "__main__":

    tiger = Bitmap('./assets/tiger.bmp')

    tiger.save_new(tiger.make_grayscale())
    tiger.save_new(tiger.flip_horizontal())
    tiger.save_new(tiger.flip_vertical())
    tiger.save_new(tiger.make_thumbnail())
    tiger.save_new(tiger.invert_colors())