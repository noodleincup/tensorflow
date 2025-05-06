import numpy as np
import json
from flask import Flask, request
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

model_path = "D:\Project\Learning\TensorFlow_Files\model\handwrite_number_model.h5"
model = load_model(model_path)

# Show input shape
print('model:', model.get_config()['layers'][0]['config']['batch_shape'])

app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def run_model():
    # Get request data
    req_data = request.get_json(force=True)
    
    print('req_data type :', type(req_data))

    if isinstance(req_data, str):
        req_data = json.loads(req_data)

    try:
        img_data = req_data['img']
    except Exception as e:
        print('Error:', e)
        return str(1)

    # print('img_data:', img_data)
    
    # Reshape the image data
    img_data = np.array(img_data).reshape(28, 28, 1)
    img_data = np.expand_dims(img_data, axis=0)

    # Predict the digit
    pred = model.predict(img_data)

    digit = np.argmax(pred, axis=1)[0]

    return str(digit)

if __name__ == "__main__":
    app.run()

