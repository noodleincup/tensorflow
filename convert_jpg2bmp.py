from PIL import Image
import os

# Set the folder containing the JPG files
input_folder = r'C:\Users\autoy\Downloads\bag_datasets'
output_folder = r'C:\Users\autoy\Downloads\bag_datasets\BMP'

number = 1
# Loop through all files in the folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.jpg'):
        # Define the full path to the input and output files
        jpg_path = os.path.join(input_folder, filename)

        filename = f"image{number}"
        number += 1
        bmp_filename = os.path.splitext(filename)[0] + '.bmp'
        bmp_path = os.path.join(output_folder, bmp_filename)

        # Open and convert the image
        with Image.open(jpg_path) as img:
            img.convert('RGB').save(bmp_path)

        print(f"Converted: {filename} -> {bmp_filename}")