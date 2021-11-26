import string
import json
import requests
import simplejson
#import threading

patentes = []

def post(patente):
    url= "http://localhost:5000/api/v1.0/patente/"
    payload = {"name": patente}
    headers = {'content-type': 'application/json',}
    r = requests.post(url,data=simplejson.dumps(payload),headers=headers)
    return r.text

def worker(patentes):
	for patente in patentes:
		msg = post(patente)
	return

def HilosWorker(nhilos,lista):
        cant_patentes = len(lista)
        aux = cant_patentes / nhilos
        patentes = lista

        threads = list()
        for i in range(nhilos):
                d = aux*(i+1)
                t = threading.Thread(target=worker, args=(patentes[d-aux:d],))
                threads.append(t)
                t.start()
        return {"code":200,"msg":"hilos creados"}

def iterar_num(letters):
	for i in range(0,10):
		patentes.append(letters + "00" + str(i))

	# En la DB no cargue los registros que siguen de 100 a 1000 porque me estaba congelando la maquina
	# De todas formas queda la lógica y una implementación por hilos para subir todos los registros más rápido
	for i in range(10,100):
		patentes.append(letters + "0" + str(i))

	for i in range(100,1000):
		patentes.append(letters + str(i))
	return


if __name__ == "__main__":
	# Generar alfabeto
	listAlphabet = list(string.ascii_uppercase)

	# Letras en orden de posición inicial
	l1 = l2 = l3 = l4 = 'A'

	# Se recorren las 4 letras según la secuencia
	for letter1 in list(listAlphabet):
		l1 = letter1
		for letter2 in list(listAlphabet):
			l2 = letter2
			for letter3 in list(listAlphabet):
				l3 = letter3
				for letter4 in list(listAlphabet):
					l4 = letter4
					aux = l1 + l2 + l3 + l4
					iterar_num(aux)			# Se agrega la parte númerica
	#print(patentes)
	print(len(patentes))

	for patente in patentes:
		post(patente)

	# Para hacer la carga de los registros por hilos toca instalar threading, descomentar el import y las siguientes líneas
	#nhilos = 150 				# Cantidad de hilos, debería ser un divisor de la cantidad de patentes
	#res = HilosWorker(nhilos,patentes)