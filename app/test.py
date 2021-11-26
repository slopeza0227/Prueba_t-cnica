import json
import requests
import simplejson

def post(patente):
    url= "http://localhost:5000/api/v1.0/patentes/"
    payload = {"name": patente}
    headers = {'content-type': 'application/json',}
    r = requests.post(url,data=simplejson.dumps(payload),headers=headers)
    return r.text

def get_by_id(id):
    url= "http://localhost:5000/api/v1.0/patentes/%s"%id
    r = requests.get(url)
    return r.text

def get_by_name(name):
    url= "http://localhost:5000/api/v1.0/patentes/%s"%name
    r = requests.get(url)
    return r.text

def get_sumamation(r=1,c=1,z=1,x=0,y=0):                # En esta prueba se pasan por defecto los valores mínimos pero en la lógica del resource ya toma todas las consideraciones.
    url= "http://localhost:5000/api/v1.0/sumatoria/"
    parametros = {'r':r, 'c':c, 'z':z, 'x':x, 'y':y}
    r = requests.get(url,params=parametros)
    return r.text


if __name__ == "__main__":
    print(get_by_id(12))                # Busqueda por ID de patente
    print(get_by_name('AAAB001'))       # Busqueda por name de patente
    print(get_sumamation(4,3,2,1,2))    # Sumatoria de ejemplo

    print(get_by_id(-12))               # Busqueda por ID de patente incorrecto
    print(get_by_name('AAAB001SD'))     # Busqueda por name de patente incorrecto
    print(get_sumamation(r=-4, c=3, z=2, x=1, y=2))    # Sumatoria sin cumplir requisitos
    print(get_sumamation(c=3, z=2, x=1, y=2))    # Sumatoria sin requisitos
    print(get_sumamation(r=4, c=3, z=0, x=1, y=2))    # Sumatoria sin cumplir requisitos