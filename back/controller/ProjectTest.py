from flask import Flask,request,send_from_directory
from flask_restplus import Namespace, Resource, fields
from service.computerService import ComService
from service.testService import TestService
import pandas as pd
from flask_cors import CORS

api = Namespace('projectTest', description='项目测试')


@api.route('/upload/<projectname>/<name>/<testmethod>', methods=['POST'])
@api.response(404, 'Method not found')
class ComUpload(Resource):
    @api.doc('测试数据上传')
    def post(self,projectname,name,testmethod):
        
        csv_data = pd.read_csv(request.files['file'],encoding='gbk')
        print(csv_data)
        accuracy= TestService.handlerData(TestService,csv_data,projectname,name,testmethod)
        return accuracy
        

@api.route('/download/<projectname>/<name>/<testmethod>')
@api.response(404, 'Method not found')
class ComCon(Resource):
    @api.doc('测试数据下载')
    def get(self,projectname,name,testmethod):
        # name = request.args.get("name")
        # testmethod = request.args.get("testmethod")
        return send_from_directory("./output"+"./"+projectname+"./"+name+"./"+testmethod,filename="output.csv",as_attachment=True)






@api.route('/getAccuracy/<projectname>/<name>/<testmethod>')
@api.response(404, 'Method not found')
class ComUpload(Resource):
    @api.doc('获取准确率')
    def get(self,projectname,name,testmethod):
        count=0
        csv_data = pd.read_csv('./csv/'+name+'/com/'+testmethod+"/output.csv")
        for index,row in csv_data.iterrows():
            if csv_data.at[index,'flag']==True:
                count+=1
        print(csv_data)       
        accurary=count/len(csv_data)
        return accurary 
