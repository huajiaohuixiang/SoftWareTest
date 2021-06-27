from flask_restplus import Api
from controller.chargeController import api as charge_api
from controller.triangleController import api as tri_api
from controller.computerController import api as com_api
from controller.ProjectController import api as project_api
from controller.ProjectTest import api as project_test
from controller.JavaController import api as java_controller

api= Api(
    title='Software Testing Visual Platform',
    version='v1.0',
    description='Software Testing Visual Platform Api'
)

api.add_namespace(tri_api, path='/question1')
api.add_namespace(com_api, path='/question2')
api.add_namespace(charge_api, path='/question6')
api.add_namespace(project_api,path='/project')
api.add_namespace(project_test,path='/projecttest')
api.add_namespace(java_controller,path='/java')