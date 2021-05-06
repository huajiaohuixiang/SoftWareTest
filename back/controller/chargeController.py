from flask_restplus import Namespace, Resource, fields
from back.service.chargeService import CharService
from flask import Flask,request,send_from_directory
import pandas as pd
from flask_cors import CORS

api = Namespace('question6', description='电信收费问题')


@api.route('/upload', methods=['POST'])
@api.response(404, 'Method not found')
class ComUpload(Resource):
    def post(self):
        csv_data = pd.read_csv(request.files['file'])
        print(csv_data)
        CharService.handlerData(CharService,csv_data)
        return 'ok'

@api.route('/download')
@api.response(404, 'Method not found')
class ComCon(Resource):
    @api.doc('download csv2')
    def get(self):
        return send_from_directory("./csv/charge/",filename="output.csv",as_attachment=True)


