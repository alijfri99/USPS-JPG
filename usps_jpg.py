import numpy
from PIL import Image
import matplotlib.pyplot as plt

def read_dataset_images(path):
    images = ""
    with open(path, 'r') as file:
        images = file.read()
        images = images.split('\n')
    return images


def image_to_numpy_array(input_image):
    input_image = input_image.split(' ')
    output_image = numpy.zeros((16, 16), dtype=numpy.float32)
    output_class = input_image[0]
    
    for i in range(1, 257):
        current_pixel_value = float(input_image[i].split(':')[1])
        output_image[(i - 1) // 16][(i - 1) % 16] = float(current_pixel_value)

    return output_image, output_class