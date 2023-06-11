import os
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


def find_best_match(input_image_path, image_folder):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert("RGB")

    best_match = None
    best_match_percent = float('inf')

    for file_name in os.listdir(image_folder):
        file_path = os.path.join(image_folder, file_name)
        if os.path.isfile(file_path):
            percent_diff = compare_images(input_image_path, file_path)
            if percent_diff < best_match_percent:
                best_match_percent = percent_diff
                best_match = file_name

    return best_match, best_match_percent


# Specify the path to the input image and the folder containing the images to compare
input_image_path = input("image path")
image_folder = input("folder path")

# Call the find_best_match function with the input image path and the image folder
best_match, best_match_percent = find_best_match(input_image_path, image_folder)

print("Best match:", best_match)
print("Matching percentage:", best_match_percent, "%")
