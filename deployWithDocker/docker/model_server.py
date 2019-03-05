from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
from flask import Flask, request, jsonify
from io import BytesIO

PORT='5000'
HOSTNAME='0.0.0.0'

class PredictorServer:
    
    app = Flask(__name__)

    def __init__(self):
        self.model = ResNet50(weights='imagenet')

    @app.route('/health')
    def health():
        return 'ok'
    
    @app.route('/predict', methods=['POST'])
    def predict():
        data = {'success': False}
        if request.method == 'POST' and request.files.get('image'):
            image = request.files['image'].read()
            image = Image.open(BytesIO(image))
            if image.mode != 'RGB':
                image = image.convert('RGB')
            image = image.resize((224, 224))
            image = img_to_array(image)
            image = np.expand_dims(image, axis=0)
            image = imagenet_utils.preprocess_input(image)

            preds = self.model.predict(image)
            results = imagenet_utils.decode_predictions(preds)
            data["predictions"] = [
                {
                    'label': label,
                    'probability': float(prob)
                }
                for _, label, prob in results[0]
            ]
            data['success'] = True
        return jsonify(data)

if __name__ == '__main__':
    predictorServer = PredictorServer()
    predictorServer.app.run(HOSTNAME, PORT)
