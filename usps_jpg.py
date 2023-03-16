import numpy
from PIL import Image

def read_dataset_images(path):
    with open(path, 'r') as file:
        images = file.read()
        images = images.split(' ')
    return images


