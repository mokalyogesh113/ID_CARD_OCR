from flask import Flask, request
from flask_cors import CORS

import io
from PIL import Image 
import numpy as np

import pan_ocr as po

app = Flask(__name__)
CORS(app)

@app.route("/get_pan_data",methods=['GET', 'POST'])
def get_pan_data():
    if(request.method  == 'POST'):

        if 'imageFile' not in request.files:
            return 'No file part in the request'
        
        file = request.files['imageFile']
        
        if file.filename == '':
            return 'No selected file'

        image = np.asarray(Image.open(io.BytesIO(file.read())))


        data = po.get_pan_data(image)
        return data

    return {"name" : "Yogesh Mokal"}


if __name__ == '__main__':
    app.run(debug=True)