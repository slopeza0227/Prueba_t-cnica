# Prueba técnica Kibernum

Hola, estas son algunas recomendaciones para ejecutar el proyecto:

## Requeriments
* flask
* flask_restful
* flask_sqlalchemy
* flask_migrate
* flask_marshmallow
* marshmallow-sqlalchemy
* requests
* simplejson
* threading

## Setup

Clonar el proyecto
```
https://github.com/slopeza0227/Prueba_t-cnica.git
```

Activar el entorno virtual creado con python3.8
```
source venv/bin/activate
```

Instalar todas las librerías requeridas con
```
pip install -r requeriments.txt
```

Generar SECRET_KEY y agregarla en config.default.py
```
import secrets
secrets.token_hex(20)
```

La DB se llama patente.sqlite y agregue 32.905 registros por el tema del tiempo pero deje toda la lógica para implementarlos en su totalidad en el archivo fillDB.py

Configurar Flask
```
export FLASK_APP="entrypoint:app"
export FLASK_DEB=1
export APP_SETTINGS_MODULE="config.default"
```

Ejecutar Flask
```
flask run
```

Se pueden realizar todas las pruebas por Postman o también deje un script llamado test.py con algunas pruebas listas.

Saludos.
