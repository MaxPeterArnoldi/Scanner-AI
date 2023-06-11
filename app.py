from PIL import Image
import numpy as np


def compare_images(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Resize the images to the same dimensions for comparison
    image1 = image1.resize(image2.size)

    # Convert the images to numpy arrays
    array1 = np.array(image1)
    array2 = np.array(image2)

    # Calculate the percentage difference
    diff = np.abs(array1 - array2)
    percent_diff = np.mean(diff) / 255.0 * 100.0

    return percent_diff


# Specify the paths to the images you want to compare
image1_path = ""
image2_path = "haus003.jpg"

# Call the compare_images function with the image paths
percent_diff = compare_images(image1_path, image2_path)
print("Difference:", percent_diff, "%")
