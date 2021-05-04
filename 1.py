from flask import Flask,request,send_from_directory
import xlrd
from flask_cors import CORS
import pandas as pd
app=Flask(__name__)
CORS(app, resources=r'/*')	# 注册CORS, "/*" 允许访问所有api


@app.route('/')
def hell_world():
    return 'Hello World'

@app.route('/a')
def a():
    return 'a'
    
@app.route("/download")
def index():
    return send_from_directory("./csv/triangle/",filename="test.csv",as_attachment=True)

@app.route('/upload', methods=['POST'])
def his_upload_clinic_detail():


    csv_data = pd.read_csv(request.files['file'])
    print(csv_data)
    return 'ok'    






if __name__=='__main__':
    app.run()