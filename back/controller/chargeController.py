from flask_restplus import Namespace, Resource, fields
from service.chargeService import CharService
from flask import Flask,request,send_from_directory
import pandas as pd
from flask_cors import CORS

api = Namespace('question6', description='电信收费问题')


@api.route('/upload/<name>/<testmethod>', methods=['POST'])
@api.response(404, 'Method not found')
class ComUpload(Resource):
    def post(self,name,testmethod):
        csv_data = pd.read_csv(request.files['file'],encoding='gbk')
        print(csv_data)
        accuracy=CharService.handlerData(CharService,csv_data,name,testmethod)
        return accuracy

@api.route('/getAccuracy/<name>/<testmethod>')
@api.response(404, 'Method not found')
class ComUpload(Resource):
    def get(self,name,testmethod):
        count=0
        csv_data = pd.read_csv('./csv/'+name+'/charge/'+testmethod+"/output.csv")
        for index,row in csv_data.iterrows():
            if csv_data.at[index,'flag']==True:
                count+=1
        print(csv_data)
        accurary=count/len(csv_data)
        return accurary

@api.route('/download/<name>/<testmethod>')
@api.response(404, 'Method not found')
class ComCon(Resource):
    @api.doc('download csv2')
    def get(self,name,testmethod):
        return send_from_directory("./csv/" + name + "/charge/" + testmethod, filename="output.csv", as_attachment=True)


