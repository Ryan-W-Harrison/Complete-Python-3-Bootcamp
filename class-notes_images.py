# Workingg with images
# pillow library
os.system("pip install Pillow")

from PIL import Image

dir_image = f'{os.getcwd()}/14-Working-with-Images'

mac = Image.open(f'{dir_image}/example.jpg')

type(mac)

mac
mac.show()
mac.size
mac.filename
mac.format_description

# Cropping images
mac.crop((0, 0, 100, 100))

pencils = Image.open(f'{dir_image}/pencils.jpg')
pencils
pencils.size

# Top left crop
# Start at top corner (0, 0)
x = 0
y = 0
# grab about 10% in y direction, and about 30% in x direction
w = 1950 / 3
h = 1300 / 10
pencils.crop((x, y, w, h))

# Bottom left crop
# Start at top corner (0, 0)
x = 0
y = 1100
# grab about 10% in y direction, and about 30% in x direction
w = 1950 / 3
h = 1300
pencils.crop((x, y, w, h))
