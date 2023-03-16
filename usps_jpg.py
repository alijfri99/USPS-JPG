import numpy
from PIL import Image
import os

def read_dataset(path):
    images = ""
    with open(path, 'r') as file:
        images = file.read()
        images = images.split('\n')
    return images


def image_to_numpy_array(input_image):
    input_image = input_image.split(' ')
    output_image = numpy.zeros((16, 16), dtype=numpy.uint8)
    output_class = str(int(input_image[0]) - 1)
    
    for i in range(1, 257):
        current_pixel_value = float(input_image[i].split(':')[1])
        current_pixel_value = int((current_pixel_value + 1) * 255 / 2)
        output_image[(i - 1) // 16][(i - 1) % 16] = float(current_pixel_value)

    return output_image, output_class

def save_image(image, image_class, dataset_type, file_name):
    path = os.path.join('./Dataset', dataset_type, image_class, str(file_name) + '.jpg')
    image = Image.fromarray(image)
    image.save(path)

def extract_dataset(dataset_name):
    dataset = read_dataset(dataset_name)
    dataset_type = dataset_name.split('_')[1][:-4]
    print('Extracting ' + dataset_type + '.')

    for counter in range(len(dataset) - 1):
        image, image_class = image_to_numpy_array(dataset[counter])
        save_image(image, image_class, dataset_type, counter)

    print(dataset_type + ": " + str(counter))

extract_dataset('usps_training.txt')
extract_dataset('usps_testing.txt')
print("Done!")
