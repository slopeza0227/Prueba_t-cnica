Hola, algunas recomendaciones para ejecutar el proyecto:

activar el entorno virtual creado con python3.8
	source venv/bin/activate

Instalar todas las librerías requeridas con
	pip install -r requeriments.txt

Generar SECRET_KEY
	import secrets
	secrets.token_hex(2)

Agregar SECRET_KEY en config.default.py

La DB se llama patente.sqlite y agregue 32.905 registros por el tema del tiempo pero deje toda la lógica para implementarlos en su totalidad

Configurar Flask
	export FLASK_APP="entrypoint:app"
	export FLASK_DEB=1
	export APP_SETTINGS_MODULE="config.default"

Ejecutar Flask
	flask run

Se pueden realizar todas las pruebas por Postman o también deje un script llamado test.py con algunas pruebas listas.

Saludos.