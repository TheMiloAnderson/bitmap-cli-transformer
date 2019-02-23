from modify import Bitmap


# def test_new_file_path():
#     actual = new_file_path('_grayscale')
#     expected = ''


def test_make_grayscale():
    tiger = Bitmap('./assets/tiger.bmp')
    actual = tiger.make_grayscale()
    expected_path = './assets/tiger_grayscale.bmp'

    assert actual[1] != tiger.img
    assert actual[0] == expected_path

def test_flip_horizontal():
    tiger = Bitmap('./assets/tiger.bmp')
    actual = tiger.flip_horizontal()
    expected_path = './assets/tiger_horizontal.bmp'

    assert actual[1] != tiger.img
    assert actual[0] == expected_path
def test_flip_vertical():
    tiger = Bitmap('./assets/tiger.bmp')
    actual = tiger.flip_vertical()
    expected_path = './assets/tiger_vertical.bmp'

    assert actual[1] != tiger.img
    assert actual[0] == expected_path

def test_invert_colors():
    tiger = Bitmap('./assets/tiger.bmp')
    actual = tiger.invert_colors()
    expected_path = './assets/tiger_invert.bmp'

    assert actual[1] != tiger.img
    assert actual[0] == expected_path

def test_make_thumbnail():
    tiger = Bitmap('./assets/tiger.bmp')
    actual = tiger.make_thumbnail()
    expected_path = './assets/tiger_thumbnail.bmp'

    assert actual[1] != tiger.img
    assert actual[0] == expected_path
