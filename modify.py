from PIL import Image, ImageOps


class Bitmap(object):
    
    def __init__(self, file_path):
        """
        Records original file path.
        """
        self.file_path = file_path
        self.img = Image.open(self.file_path)
        with open(file_path, 'rb') as file:
            self.bin_img = bytearray(file.read())

    def new_file_path(self, mod_type):
        """
        Create a new file path with the mod type
        """
        split_name = self.file_path.split('.')
        split_name[1] += f'{mod_type}'
        return '.'.join(split_name)

    def make_grayscale(self, img='self.img'):
        """
        Modify the input image with grayscale  and returns the new path with the new image
        """
        new_path = self.new_file_path('_grayscale')
        img = self.img.convert('L')
        return [new_path, img]

    def _make_bi_int(self, byts):
        return int.from_bytes(byts, byteorder='little')

    def custom_grayscale(self, img='self.img'):
        new_path = self.new_file_path('_grayscale')

        file_header = self.bin_img[:14]
        img_header_size = self._make_bi_int(self.bin_img[14:18])
        img_header = self.bin_img[14:14 + img_header_size]
        img_pix_location = self._make_bi_int(file_header[10:])
        img_pix = self.bin_img[img_pix_location:]
        img_width = self._make_bi_int(img_header[4:6])
        img_height = self._make_bi_int(img_header[8:10])
        img_bpp = self._make_bi_int(img_header[14:16])
        img_cols = img_width * 3
        img_cols_pad = ((img_cols + 3) & ~0x03) - img_cols

        counter = 0
        for i in range(0, len(img_pix) - 1):
            if counter < img_cols and counter % 3 == 0:
                b = img_pix[i]
                g = img_pix[i + 1]
                r = img_pix[i + 2]
                avg = int(round((r + g + b) / 3))
                img_pix[i] = avg
                img_pix[i + 1] = avg
                img_pix[i + 2] = avg
            if counter == img_cols + img_cols_pad:
                counter = 0
            else:
                counter += 1

        new_bitmap = file_header + img_header + img_pix
        return [new_bitmap, new_path]


    def flip_horizontal(self, img='self.img'):
        """
        Modify the input image with flip horizontal  and returns the new path with the new image
        """
        new_path = self.new_file_path('_horizontal')
        img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        return [new_path, img]

    def flip_vertical(self, img='self.img'):
        """
        Modify the input image with flip vertical  and returns the new path with the new image
        """
        new_path = self.new_file_path('_vertical')
        img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        return [new_path, img]

    def invert_colors(self, img='self.img'):
        """
        Modify the input image with invert colors  and returns the new path with the new image
        """
        new_path = self.new_file_path('_invert')
        img = ImageOps.invert(self.img)
        return [new_path, img]

    def make_thumbnail(self, img='self.img'):
        """
        Modify the input image into a thumbnail  and returns the new path with the new image
        """
        new_path = self.new_file_path('_thumbnail')
        size = 128, 128
        img = self.img.copy()
        img.thumbnail(size)
        return [new_path, img]

    def save_new(self, lst):
        """
        Save the modified image into the folder
        """
        lst[1].save(lst[0], 'bmp')

    def save_custom(self, img_path):
        with open(img_path[1], 'wb') as file:
            file.write(img_path[0])

if __name__ == "__main__":

    test = Bitmap('./assets/spock.bmp')
    test.custom_grayscale()
