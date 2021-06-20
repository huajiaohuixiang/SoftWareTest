from flask import Flask,request,send_from_directory
from flask_restplus import Namespace, Resource, fields
from service.computerService import ComService
import pandas as pd
from flask_cors import CORS

api = Namespace('project', description='项目管理')


@api.route('/getAllProject')
@api.response(404, 'Method not found')
class ProjectCon(Resource):
    @api.doc('获取所有项目')
    def get(self):
        project_data = pd.read_csv('./project/projectInfo.csv',sep=';')
        array=[]
        for index,row in project_data.iterrows():
            array.append(row['projectName'])
        return array

@api.route('/createNewProject',methods=["POST"])
@api.response(404, 'Method not found')
class createNewProject(Resource):
    @api.doc('创建新项目')
    def post(self):
        print(request.get_json())
        data=request.get_json()['form']
        projectName=data['projectName']
        funcName=data['funcName']
        func=data['func']
        inputParam=data['inputParam']
        outputParam=data['outputParam']
        inputParams=inputParam.split("\n")
        outputParams=outputParam.split("\n")
        print(inputParams)
        print(outputParams)
        with open("./project/"+projectName+".py",'w+',encoding="utf-8")as profile:
            profile.write(func+"\n")
        with open("./service/"+"testService.py",'a+',encoding="utf-8")as profile:
            profile.write(func+"\n")
        with open("./project/"+"projectInfo.csv",'a+')as proInfofile:
            proInfofile.write(projectName+";"+funcName+";"+str(inputParams)+";"+str(outputParams)+"\n")
        return "success"



@api.route('/getProjectFunc/<ProjectName>')
@api.response(404, 'Method not found')
class getProjectFunc(Resource):
    @api.doc('获取项目代码')
    def get(self,ProjectName):
        func=""
        with open('./project/'+ProjectName+".py",'r',encoding='utf-8') as profile:
            func=profile.read()
        return func
