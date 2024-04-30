from flask import Flask, request, jsonify
from flask_cors import CORS
# from waitress import serve
import io
from PIL import Image 
import numpy as np

from pan_aadhar_ocr import get_aadhar_data , get_pan_data
import sql_crud as crud

app = Flask(__name__)
CORS(app)

@app.route("/pan/extract_data",methods=['GET', 'POST'])
def pan_extract_data():
    if(request.method  == 'POST'):
        if 'imageFile' not in request.files:
            return 'No file part in the request'
        file = request.files['imageFile']
        if file.filename == '':
            return 'No selected file'
        image = np.asarray(Image.open(io.BytesIO(file.read())))
        data = get_pan_data(image)
        return data
    return {"Error" : "Only POST METHODS ARE ALLOWED"}

@app.route("/pan/store_data",methods=['GET', 'POST'])
def pan_store_data():
    if request.is_json:
        data = request.get_json()
        flag = crud.insert_pan_data(data)
        return jsonify(sucess=flag) , 200
    return jsonify(error='Data was not in JSON format'), 400 

@app.route('/pan/get_all_data', methods=['GET', 'POST'])
def pan_get_all_data():  
    id = ""
    if request.method == 'GET':
        id = request.args.get('id')
    elif request.method == 'POST':
        id = request.get_json().get('id')        
    if(id):
        return crud.get_pan_data(id)
    return crud.get_pan_data()

@app.route("/aadhar/extract_data",methods=['GET', 'POST'])
def aadhar_extract_data():
    if(request.method  == 'POST'):
        if 'imageFile' not in request.files:
            return 'No file part in the request'
        file = request.files['imageFile']
        if file.filename == '':
            return 'No selected file'
        image = np.asarray(Image.open(io.BytesIO(file.read())))
        data = get_aadhar_data(image)
        return data
    return {"Error" : "Only POST METHODS ARE ALLOWED"}



if __name__ == '__main__': 
    app.run(debug=True,port = 5005)
    # serve(app , host ="0.0.0.0", port = 5000,url_prefix = "/flask-server")
