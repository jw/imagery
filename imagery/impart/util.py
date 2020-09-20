from PIL import Image


def square(image_file, x, y, size):
    im = Image.open(image_file)
    box = (x, y, x + size, y + size)
    im.crop(box)
    im.save(image_file + ".square", "JPEG")


def shrink(image_file, percentage=0.50):
    im = Image.open(image_file)
    size = tuple([int(z * percentage) for z in im.size])
    im.thumbnail(size)
    im.save(image_file + ".shrink", "JPEG")


def thumbnail(image_file, width=None, height=None):
    if width is None and height is None:
        raise AssertionError
    im = Image.open(image_file)
    size = im.size
    if width is not None:
        size[0] = width
    if width is not None:
        size[1] = height
    im.thumbnail(size)
    im.save(image_file + "." + size[0] + "x" + size[1], "JPEG")
