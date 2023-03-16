import numpy
from PIL import Image

def read_dataset_images(path):
    with open(path, 'r') as file:
        images = file.read()
        images = images.split('\n')
    return images


x = read_dataset_images('usps_training.txt')
print(len(x))
print(x[10])