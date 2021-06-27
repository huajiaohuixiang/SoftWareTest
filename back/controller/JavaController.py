import os
from flask import Flask,request,send_from_directory
from flask_restplus import Namespace, Resource, fields
from service.JavaProjectService import JavaProjectService
import pandas as pd
from flask_cors import CORS

api = Namespace('JavaController', description='Java项目管理')


@api.route('/getAllJavaProject')
@api.response(404, 'Method not found')
class ProjectCon(Resource):
    @api.doc('获取所有项目')
    def get(self):
        path=JavaProjectService.getAllJavaPRoject(JavaProjectService)        
        return path

@api.route('/getAllJavaProjectFiles/<name>')
@api.response(404, 'Method not found')
class ProjectConFiles(Resource):
    @api.doc('获取项目所有文件')
    def get(self,name):
        path=JavaProjectService.getAllProjectFile(JavaProjectService,name)        
        return path[::-1]


import subprocess
@api.route('/testOneService/<projectname>/<name>')
@api.response(404, 'Method not found')
class TestServiceController(Resource):
    @api.doc('对某个类进行测试')
    def post(self,projectname, name):  
        print(name)  
        cmd=' java -jar '+'./JavaProject/'+projectname+'/target/meethere-0.0.1-SNAPSHOT-fat-tests.jar'+' com.meethere.testService.'+name[0:len(name)-5]+'Test'
        print(cmd)
        r = os.popen(cmd)
        print(r.read())
        return name
