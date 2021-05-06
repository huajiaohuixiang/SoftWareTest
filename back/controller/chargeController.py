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
        return send_from_directory("./csv/com/",filename="charge.csv",as_attachment=True)


# @api.route('/charge/<method_type>')
# @api.param('method_type', 'boundary | equivalence | decision | final')
# @api.response(404, 'Method not found')
# class Calendar(Resource):
#     @api.doc('Charge Problem')
#     def get(self, method_type):
#         """
#         电信收费问题
#         """
#         return question6_service.charge(method_type)
#
#
# @api.route('/charge/')
# class CalenderBasic(Resource):
#     @api.doc('Charge Problem Basic Method')
#     @api.expect(model)
#     def post(self):
#         """
#         电信收费问题的基础实现
#         """
#         return question6_service.charge_method_test(api.payload)
#
#
# @api.route('/charge/<code_version>')
# @api.param('code_version', 'v1 | v2')
# class CalenderBasic(Resource):
#     @api.doc('Charge Problem Basic Method')
#     @api.expect(model)
#     def post(self, code_version):
#         """
#         版本-电信收费问题的基础实现
#         """
#         return question6_service.charge_method_test(api.payload, code_version)
#
#
# @api.route('/charge/<method_type>/<code_version>')
# @api.param('method_type', 'boundary | equivalence | decision')
# @api.param('code_version', 'v1 | v2')
# @api.response(404, 'Method not found')
# class Calendar(Resource):
#     @api.doc('Charge Problem')
#     def get(self, method_type, code_version):
#         """
#         版本-电信收费问题
#         """
#         return question6_service.charge(method_type, code_version)
