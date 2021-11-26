from flask import request, Blueprint
from flask_restful import Api, Resource
from app.common.error_handling import ObjectNotFound, AppErrorBaseClass
from .schemas import PatenteSchema
from ..models import Patente

patente_v1_0_bp = Blueprint('patente_v1_0_bp', __name__)

patente_schema = PatenteSchema()

api = Api(patente_v1_0_bp)

class PatenteListResource(Resource):
    def get(self):
        patentes = Patente.get_all()
        result = patente_schema.dump(patentes, many=True)
        return result

    def post(self):
	    data = request.get_json()
	    patente_dict = patente_schema.load(data)
	    patente = Patente(name=patente_dict['name'])
	    patente.save()
	    resp = patente_schema.dump(patente)
	    return resp, 201

class PatenteResourceId(Resource):
    def get(self, patente_id):
        patente = Patente.get_by_id(patente_id)
        if patente is None:
            raise ObjectNotFound('El ID %s de la patente no existe'%patente_id)
        resp = patente_schema.dump(patente)
        del resp['id']		# El ejercicio indica solo devolver el Name
        return resp

class PatenteResourceName(Resource):
    def get(self, patente_name):
        patente = Patente.get_by_name(patente_name)
        if patente is None:
            raise ObjectNotFound('El name %s de la patente no existe'%patente_name)
        resp = patente_schema.dump(patente)
        del resp['name']	# El ejercicio indica solo devolver el ID
        return resp

class SumamationResource(Resource):
    def get(self):
        flag = True

        r = str(request.args.get('r'))
        c = str(request.args.get('c'))
        z = str(request.args.get('z'))
        x = str(request.args.get('x'))
        y = str(request.args.get('y'))

        if (r == 'None' or c == 'None' or z == 'None' or x == 'None' or y == 'None'):
            raise ObjectNotFound('Por favor agregue todos los parámetros: filas (r), columnas (c), coordenadas(x,y) y z')

        if not (c.isnumeric() and int(c) > 0): flag = False
        if not (r.isnumeric() and int(r) > 0): flag = False
        if not (z.isnumeric() and int(z) > 0 and int(z) <= 1000000): flag = False
        if not (x.isnumeric() and int(x) < int(c)): flag = False
        if not (y.isnumeric() and int(y) < int(r)): flag = False
    	
        if flag:
            summation = 0
        
            for row in range(1,int(y)+2):	# Es +2 porque el range no toma el último valor y el +1 del Y y R
                summation += (int(z)+row-1)*(int(x)+1)	# Se recorren las filas y se multiplica el valor por la cantidad de columnas

            resp = {"summation": summation}
            return resp
        else:
            raise ObjectNotFound("""Las filas (r) y columnas (c) deben ser enteros mayores a 0
                La zeta (z) debe cumplir que 0 < z <= 1.000.000
                Las coordenadas (x,y) deben ser enteros positivos menores a (c,r) respectivamente""")

api.add_resource(PatenteListResource, '/api/v1.0/patentes/', endpoint='patente_list_resource')
api.add_resource(PatenteResourceId, '/api/v1.0/patentes/<int:patente_id>', endpoint='patente_resource_id')
api.add_resource(PatenteResourceName, '/api/v1.0/patentes/<string:patente_name>', endpoint='patente_resource_name')
api.add_resource(SumamationResource, '/api/v1.0/sumatoria/', endpoint='summation_resource')