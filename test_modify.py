from modify import Bitmap

def test_new_file_path():
    """
    Can create new file path with mod type
    """
    mod_type = '_grayscale'
    tiger = Bitmap('./assets/tiger.bmp')
    actual = tiger.new_file_path(mod_type)
    expected = './assets/tiger_grayscale.bmp'
    assert expected == actual

def test_make_grayscale():
    """
    Can transform image with grayscale
    """
    tiger = Bitmap('./assets/tiger.bmp')
    actual = tiger.make_grayscale()
    expected_path = './assets/tiger_grayscale.bmp'

    assert actual[1] != tiger.img
    assert actual[0] == expected_path

def test_flip_horizontal():
    """
    Can transform image with flip horizontal
    """
    tiger = Bitmap('./assets/tiger.bmp')
    actual = tiger.flip_horizontal()
    expected_path = './assets/tiger_horizontal.bmp'

    assert actual[1] != tiger.img
    assert actual[0] == expected_path

def test_flip_vertical():
    """
    Can transform image with flip vertical
    """
    tiger = Bitmap('./assets/tiger.bmp')
    actual = tiger.flip_vertical()
    expected_path = './assets/tiger_vertical.bmp'

    assert actual[1] != tiger.img
    assert actual[0] == expected_path

def test_invert_colors():
    """
    Can transform image with invert colors
    """
    tiger = Bitmap('./assets/tiger.bmp')
    actual = tiger.invert_colors()
    expected_path = './assets/tiger_invert.bmp'

    assert actual[1] != tiger.img
    assert actual[0] == expected_path

def test_make_thumbnail():
    """
    Can transform image into a thumbnail
    """
    tiger = Bitmap('./assets/tiger.bmp')
    actual = tiger.make_thumbnail()
    expected_path = './assets/tiger_thumbnail.bmp'

    assert actual[1] != tiger.img
    assert actual[0] == expected_path
