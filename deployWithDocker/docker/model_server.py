import os
import io
import json
import falcon
from falcon_multipart.middleware import MultipartMiddleware
import numpy as np
from PIL import Image
from keras.models import load_model

class HealthResource():
    """
    A resource that provides a health check for the model server
    """
    def __init__(self):
        pass
    
    def on_get(self, req, resp):
        """
        Health resource receives a GET request to confirm that the server is healthy and returns "I'm alive."
        """
        resp.status = falcon.HTTP_200
        resp.body = 'I\'m alive.'

class PredictResource():
    """
    A resource that provides prediction service
    """
    def __init__(self, model):
        self.model = model

    def on_post(self, req, resp):
        """
        Prediction resource receives a POST request with an image payload and returns a prediction.
        """
        image = req.get_param('image')
        img_bytes = image.file.read()
        img = Image.open(io.BytesIO(img_bytes))
        data = np.asarray(img, dtype='int32')
        data = (data / 255).reshape(1, 28, 28, 1)
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

# Create API and attach resources to endpoints; we attach middleware to allow Falcon to handle POST-ed image files
api = falcon.API(
    middleware = [
        MultipartMiddleware()
    ]
)
api.add_route('/health', healthResource)
api.add_route('/predict', predictResource)
