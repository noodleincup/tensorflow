import kagglehub

# Specify the dataset handle and desired download path
handle = "shaunthesheep/microsoft-catsvsdogs-dataset"  # Replace with the actual dataset handle
download_path = r"D:\Project\Learning\TensorFlow_Files\dataset"


# Download latest version
path = kagglehub.dataset_download(handle, download_path)

print("Path to dataset files:", path)