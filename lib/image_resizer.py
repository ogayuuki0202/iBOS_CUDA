from PIL import Image
import numpy as np

def resize_image(input_image_array, size):
    original_image = Image.fromarray(input_image_array)
    resized_image = original_image.resize(size)
    resized_image_array=np.array(resized_image)
    return resized_image_array