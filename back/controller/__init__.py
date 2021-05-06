from flask_restplus import Api
from controller.triangleController import api as tri_api
from controller.computerController import api as com_api

api= Api(
    title='Software Testing Visual Platform',
    version='v1.0',
    description='Software Testing Visual Platform Api'
)

api.add_namespace(tri_api, path='/question1')
api.add_namespace(com_api, path='/question2')
