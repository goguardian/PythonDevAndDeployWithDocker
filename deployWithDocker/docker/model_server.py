import os
import base64
import json
import falcon
import numpy as np
from io import BytesIO
from PIL import Image, ImageOps

from keras.models import load_model


def convert_image(image):
    img = Image.open(image).convert('L')
    inverted_img = ImageOps.invert(img)
    data = np.asarray(inverted_img, dtype='int32')
    rescaled_data = (data / 255).reshape(1, 28, 28, 1)
    return rescaled_data

class HealthResource():
    def __init__(self):
        pass
    
    def on_get(self, req, resp):
        """
        Health resource receives a GET request to confirm that the server is healthy and returns "I'm alive."
        """
        resp.status = falcon.HTTP_200
        resp.body = 'I\'m alive.'

class PredictResource():

    def __init__(self, model):
        self.model = model

    def on_post(self, req, resp):
        """
        Prediction resource receives a POST request with an image payload and returns a prediction.
        """
        image = json.loads(req.stream.read())
        decoded_image = base64.b64decode(image.get('image'))
        data = convert_image(BytesIO(decoded_image))
        predicted_data = self.model.predict_classes(data)[0]

        output = {'prediction': str(predicted_data)}
        resp.status = falcon.HTTP_200
        resp.body = json.dumps(output, ensure_ascii=False)


# Load Model
mnistModel = load_model('model.h5')
mnistModel._make_predict_function()

# Create Resources for API
healthResource = HealthResource()
predictResource = PredictResource(mnistModel)

# Create API and attach resources to endpoints
api = falcon.API()
api.add_route('/health', healthResource)
api.add_route('/predict', predictResource)
