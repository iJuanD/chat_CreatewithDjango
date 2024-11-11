Chat Backend con Next.js y Django

Este repositorio contiene el backend de una aplicación de chat que guarda los comentarios de los usuarios haciendo uso de LocalStorage en el navegador. La aplicación está construida utilizando Next.js en el frontend y Django en el backend para manejar las solicitudes y persistir los comentarios en la base de datos.

Características:\
Comentarios almacenados en LocalStorage: Los comentarios que los usuarios escriben se almacenan en el LocalStorage del navegador para mantener la persistencia durante la sesión.\
Backend en Django: Utiliza Django con Django REST Framework para gestionar las API que permiten la interacción entre el frontend y el almacenamiento de datos.\
Soporte para múltiples bases de datos: Puede conectarse a bases de datos como MySQL o PostgreSQL.\
CORS configurado: Se ha configurado django-cors-headers para permitir solicitudes de diferentes orígenes, facilitando la interacción entre el backend y el frontend en desarrollo.

Dependencias
Este proyecto utiliza las dependencias que se encuentran en el archivo requirements.txt 

Django: Framework web para Python.\
Django REST Framework: Conjunto de herramientas para construir APIs RESTful.\
django-cors-headers: Middleware para habilitar solicitudes entre orígenes cruzados (CORS).\
MySQLclient o psycopg2: Conectores para bases de datos MySQL y PostgreSQL, respectivamente.\
asgiref, certifi, charset-normalizer, idna, requests: Dependencias para la gestión de solicitudes HTTP y seguridad.\
whitenoise: Para servir archivos estáticos en producción.

Requisitos
Python y pip para instalar las dependencias.
Node.js y Next.js para el frontend.
Base de datos MySQL o PostgreSQL configurada.

Instalación
1. Clona este repositorio:
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

2. Configura un entorno virtual para Python:

python3 -m venv venv
source venv/bin/activate   # En Linux/macOS
venv\Scripts\activate      # En Windows

3. Instala las dependencias del backend:
pip install -r requirements.txt

4. Configura tu base de datos en el archivo settings.py de Django.

5. Ejecuta las migraciones para preparar la base de datos:
python manage.py migrate

6. Corre el servidor de desarrollo de Django:
python manage.py runserver

Uso del Proyecto
El backend de este proyecto gestiona las siguientes funcionalidades:

Enviar un comentario: Los usuarios pueden enviar comentarios, que se almacenan en el LocalStorage y se envían al servidor para su almacenamiento persistente.\
Recuperar comentarios: Los comentarios guardados se pueden recuperar desde el backend, lo que permite a los usuarios ver mensajes previos.
