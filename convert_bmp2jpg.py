import os
from PIL import Image

# Ask user for input and output folder paths
source_folder = input("Enter the source folder path (with .bmp files): ").strip()
destination_folder = input("Enter the destination folder path (to save .jpg files): ").strip()

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

i = 0
# Process each BMP file
for filename in os.listdir(source_folder):
    if filename.lower().endswith('.bmp'):
        bmp_path = os.path.join(source_folder, filename)
        
        # Open BMP image
        with Image.open(bmp_path) as img:
            # Remove .bmp extension and add .jpg
            jpg_filename = f"image_{i}" + '.jpg'
            jpg_path = os.path.join(destination_folder, jpg_filename)
            
            # Convert and save as JPG
            rgb_img = img.convert('RGB')
            rgb_img.save(jpg_path, 'JPEG')
            print(f"Converted: {filename} -> {jpg_filename}")
            i += 1

print("All BMP files have been converted to JPG.")