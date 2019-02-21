from PIL import Image

img = Image.open('./assets/tiger.bmp').convert('L')

img.show()

img.save('./assets/new_tiger.bmp', 'bmp')
