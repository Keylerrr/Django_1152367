Biblioteca API (Django REST Framework)

Este proyecto es una API para gestionar una biblioteca con autores, libros y reseñas.
Permite registrar autores, agregar libros relacionados con cada autor y escribir reseñas con calificaciones.
También incluye una función para consultar el promedio de calificaciones de cada libro.

Requisitos

Antes de comenzar asegúrate de tener instalado Python 3.8 o superior, pip y Django.
También se usan las librerías Django REST Framework y django-filter.

Instalación

Crea un entorno virtual:

python -m venv env
.\env\Scripts\activate     # En Windows
source env/bin/activate  # En Linux o macOS

Instala las dependencias:

pip install -r requirements.txt

Si no tienes ese archivo, puedes instalar manualmente:

pip install django djangorestframework django-filter


Aplica las migraciones para crear la base de datos:

python manage.py makemigrations
python manage.py migrate


Crea un superusuario para acceder al panel de administración:

python manage.py createsuperuser


(Opcional) Pobla la base de datos con datos de ejemplo:

python manage.py shell
>>> exec(open('poblar_datos.py', encoding='utf-8').read())


Ejecuta el servidor:

python manage.py runserver

Uso

Abre tu navegador y entra a:

http://127.0.0.1:8000/admin/ para el panel de administración.

http://127.0.0.1:8000/api/ para acceder a los endpoints de la API.

Puedes realizar operaciones como listar, crear, editar y eliminar autores, libros y reseñas.
También puedes filtrar, buscar u ordenar resultados desde la URL.
Por ejemplo:

/api/books/?autor=1
/api/books/?search=Soledad
/api/books/?ordering=-fecha_publicacion
