from flask import Flask,request,send_from_directory
from flask_restplus import Namespace, Resource, fields
from service.triangleService import TriService
import pandas as pd
from flask_cors import CORS

api = Namespace('question1', description='三角形')

@api.route('/download')

@api.response(404, 'Method not found')
class TriCon(Resource):
    @api.doc('download csv1')
    def get(self):
        return send_from_directory("./csv/triangle/",filename="output.csv",as_attachment=True)




@api.route('/upload', methods=['POST'])
@api.response(404, 'Method not found')
class TriUpload(Resource):
    def post(self):
        csv_data = pd.read_csv(request.files['file'])
        print(csv_data)
        TriService.handlerData(TriService,csv_data)
        return 'ok'  
