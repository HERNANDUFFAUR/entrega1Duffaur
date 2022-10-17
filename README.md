
0- desde la carpeta RAIZ

1- Crear entorno virtual(python -m venv venv-django )

2- activar entorno virtual . venv-django/Scripts/activate

3- instalar django pip install Django

4- Para los siguientes comandos recordar estar en al terminal a la altura del archivo manage.py
Podemos revisarlo ejecutando el codigo "ls" estando en bash o el comando "dir" si utilizan powershell.
generar la base de datos con la config base de django: "py manage.py migrate"

5- python manage.py runserver

4- La web tiene Index - Ver-personas - Crear-personas

Es un desarrollo de carga de datos en una base de datos:
Nombre
Apellido
Edad
Fecha Alta

Y tiene su respectiva busqueda puntual o por contener la palabra clave en la busqueda.
