# ModelsProjectDjango

Este proyecto tiene como objetivo practicar lo aprendido en OpenBootcamp (https://open-bootcamp.com/), sobre creación de modelos haciendo uso del framework Django y el lenguaje Python, y al mismo tiempo servir de guía para aquellos desarrolladores que también están interesados en practicar y aprender sobre estas tecnologías.

Se trata de un proyecto que contiene una aplicación para la gestión de empleados en una compañía.

Cabe destacar que es un proyecto bastante sencillo y relativamente básico por lo que si eres un desarrollador avanzado en este entorno quizás no te sea de tanta utilidad.

# Pasos a seguir

## Entorno Virtual

Creamos el Entorno Virtual:

```bash
$ python -m venv venv
```

Activamos el Entorno Virtual:

```bash
$ source venv/Scripts/activate
```

Instalar Django en un entorno virtual:

```bash
$ pip install Django
```

## Inicializamos el proyecto

- En primer lugar debemos iniciar el proyecto (models_project), para ello escribimos lo siguiente en la terminal:

```bash
$ django-admin startproject models_project
```

- Posteriormente debemos crear una aplicación que llamaremos company, la cual contendrá los modelos y rutas necesarias para implementar las funcionalidades relacionadas a la gestión de usuarios de la compañía. Trabajar con aplicaciones nos permite modularizar para que si quisieramos trabajar en otro proyecto con una aplicación similar de gestión de usuarios, nos permita copiar esta misma y hacerle pequeñas modificaciones. Además nos permite trabajar de una manera mucho más ordenada y mantenible

```bash
$ cd models_project
$ python manage.py startapp company
```

- Incorporamos en el settings.py de nuestro proyecto la aplicación company dentro de las aplicaciones instaladas, como se muestra a continuación:

```Python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'company',
]
```

- Podemos corroborar que ha sido instalada correctamente con el siguiente comando:

```bash
$ python manage.py check company # System check identified no issues (0 silenced).
```

## Creamos la Base de Datos:

- En este proyecto utilizaremos PostgreSQL como sistema de permanencia de datos. Para configurar la conexión a la misma debemos dirigirnos nuevamente a settings.py para configurar las variables de entorno (Documentación: https://docs.djangoproject.com/en/4.1/ref/databases/)

Creamos un archivo .env en la raíz del proyecto, donde colocaremos las variables de entorno para luego llamarlas dentro de settings.py

```bash
# Settings.py
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# -----------------------------
# .env:
SECRET_KEY='******'
DB_NAME='company',
DB_USER='postgres',
DB_PASSWORD='********',
```

- Vinculamos la BD con nuestro proyecto en django:

```bash
$ python manage.py migrate
```

Para este punto deberíamos poder ver en PgAdmin las bases de datos creadas por defecto por Django:

<img src='./public/defaultBD.png'>


## Creamos los modelos

- Nos dirigimos a la aplicación company y allí creamos un archivo models.py, donde escribiremos las clases que seran nuestros modelos.

- Luego de crear las clases debemos relacionar dichos modelos, haciendo uso de claves foraneas.

- Comprobamos que las migraciones ocurren de manera correcta a través de la migración de los modelos:

```bash
$ python manage.py makemigrations
# config django-insecure-=4atx&+8wp45!%884vf5u70p7_ufv(5go7p#c)4mees_qby9r1
# ←[36;1mMigrations for 'company':←[0m
#   ←[1mcompany\migrations\0001_initial.py←[0m
#     - Create model Country
#     - Create model Location
#     - Create model Salary
#     - Create model Place
#     - Create model Job
#     - Create model Employee
```

```bash
$ python manage.py migrate
# config django-insecure-=4atx&+8wp45!%884vf5u70p7_ufv(5go7p#c)4mees_qby9r1
# ←[36;1mOperations to perform:←[0m
# ←[1m  Apply all migrations: ←[0madmin, auth, company, contenttypes, sessions
# ←[36;1mRunning migrations:←[0m
#   Applying company.0001_initial...←[32;1m OK←[0m
```

## Estructura de la Base de Datos:

<img src='https://raw.githubusercontent.com/JuanDls01/ModelsProjectDjango/main/public/ModelsDjango.drawio.png' height="300px" width="530px">
