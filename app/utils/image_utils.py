from PIL import Image

def load_image(image_file):
    img = Image.open(image_file)
    return img
