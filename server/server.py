from flask import Flask, request, jsonify
from flask_cors import CORS

import io
from PIL import Image 
import numpy as np

import pan_ocr as po
import sql_crud as crud

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

@app.route("/store_form_data",methods=['GET', 'POST'])
def store_form_data():
    if request.is_json:
        data = request.get_json()
        
        crud.insert(data)



        return jsonify(success=True), 200
    
    return jsonify(error='Data was not in JSON format'), 400 


if __name__ == '__main__':
    app.run(debug=True)