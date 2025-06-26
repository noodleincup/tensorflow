import os
from PIL import Image




def convert_bmp_to_jpg(source_folder, destination_folder):
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)
    # Process each BMP file
    i = 0
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

if __name__ == "__main__":
    
    # camNo = 1
    for camNo in range(1, 6):
        # source_path = 
        # destination_path = 
        convert_bmp_to_jpg(rf"D:\Project\Ajinomoto\Box_Project\Dataset\Sample Box Aji-KPP\5KG. WP\Good\Cam{camNo}",
                            rf"D:\Project\Ajinomoto\Box_Project\Dataset\Sample Box Aji-KPP\5KG. WP_jpg\Good\Cam{camNo}")
    print("All BMP files have been converted to JPG.")