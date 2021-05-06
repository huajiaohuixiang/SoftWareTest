from flask import Flask,request,send_from_directory
from flask_restplus import Namespace, Resource, fields
from back.service.computerService import ComService
import pandas as pd
from flask_cors import CORS

api = Namespace('question2', description='佣金问题')

@api.route('/download')
@api.response(404, 'Method not found')
class ComCon(Resource):
    @api.doc('download csv2')
    def get(self):
        return send_from_directory("./csv/com/",filename="output.csv",as_attachment=True)




@api.route('/upload', methods=['POST'])
@api.response(404, 'Method not found')
class ComUpload(Resource):
    def post(self):
        csv_data = pd.read_csv(request.files['file'],encoding='gbk')
        print(csv_data)
        ComService.handlerData(ComService,csv_data)
        return 'ok'  

