import numpy as np
import json
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.image import rgb_to_grayscale
from PIL import Image, ImageOps
import requests

# Defome the image file payh
imgfile = "D:\Project\Learning\TensorFlow_Files\image\digit\digit9.png"  # Replace with your image path
# Load the image
img = load_img(imgfile, target_size=(28, 28))
# Invert the image colors
img = ImageOps.invert(img)
# Transform to numpy array
img_arr = img_to_array(img)
# Convert to grayscale
img_arr = rgb_to_grayscale(img_arr)
# Normalize the image
img_arr = img_arr / 255.0

# Convert to list
img_lst = np.squeeze(img_arr).tolist()

# Convert to JSON
data = json.dumps({"img": img_lst})
# Define the URL of the server
url = 'http://127.0.0.1:5000/predict'

# Send the request to the server
res = requests.post(url, json=data)
# Print the response
print('Predict: ',res.text)
