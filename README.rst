=====
Automatic Django Crud (CRUDS Automáticos en Django) para versiones de Django 2.2
=====

Automatic Django Crud ( CRUDS Automáticos en Django) es un proyecto que genera
URLS Automáticas y CRUDS Automáticos para cada modelo registrado, además tiene
la gestión de Usuarios modificada de manera general para su creación, edición,
listado y eliminación.

Los CRUDS son accesibles vía peticiones AJAX por ser generales y pensados en convertirse
en API. Además genera una URL para generar un reporte en Excel. Cabe resaltar que la
lógica aquí creada para los CRUDS es la básica, si se desea modificar la lógica
correspondiente se puede realizar sobreescribiendo los métodos get y post correspondientes
ubicados en las siguientes clases:

    BaseCrear,BaseListar,BaseActualizar,BaseEliminarLogico

Las cuales se puede importar de:
    from aplicaciones.base.base_crud.views_crud import BaseCrear,BaseListar,BaseActualizar,BaseEliminarLogico

Para redefinirlas se haría de la siguiente forma:

    class NuevaBaseCrear(BaseCrear):

        def post(self,request,*args,**kwargs):
            pass

Inicio
-----------

1. Clona o descarga este repositorio
2. Copia las carpetas aplicaciones, static y templates y el archivo requirements.txt a tu proyecto.
3. Añade "aplicaciones.base" y "aplicaciones.usuarios" a tu INSTALLED_APPS de esta manera:

    INSTALLED_APPS = [
        ...
        'aplicaciones.base',
        'aplicaciones.usuarios',
    ]

4. Incluye las URLconf de aplicaciones.usuarios y aplicaciones.base al archivo urls.py de tu proyecto:

    path('usuarios/', include(('aplicaciones.usuarios.urls','usuarios'))),
    path('base/', include(('aplicaciones.base.urls','base'))),

5. aplicaciones.base incluye las vistas necesarias para un Login y Logout, por ello su inclusión en el archivo urls.py.

6. Añade AUTH_USER_MODEL = 'usuarios.Usuario' a tu archivo settings de tu proyecto.

7. Ejecuta el comando pip install -r requirements.txt

8. Ejecuta el comando python manage.py makemigrations para crear las migraciones iniciales incluidas las del Usuario personalizado.

Creación de CRUDS
-----------

1. Crea una aplicación nueva dentro de la carpeta aplicaciones, la cuál contendrá los modelos de tu proyecto.

2. En tu archivo models.py importa:

    from aplicaciones.base.models import ModeloBase

  y haz que todos tus modelos hereden de este import, de la siguiente manera:

    Ejemplo:

    class Persona(ModeloBase):
        nombre = models.CharField(verbose_name = 'Nombre de Persona', max_length = 100)
        apellidos = models.CharField(verbose_name = 'Apellidos de Persona', max_length = 200)

        def __str__(self):
            return '{0},{1}'.format(self.apellidos,self.nombre)

3. Ahora crea un archivo urls.py dentro de tu nueva aplicación y coloca lo siguiente:

    from django.urls import path
    from .models import Persona

    urlpatterns = [

    ]

    urlpatterns += Persona().construir_URLS_genericas_de_CRUD('aplicacion_nueva','Persona')

  Los parámetros enviados a la función construir_URLS_genericas_de_CRUD son: Una cadena de texto con el nombre de la aplicación
  donde se encuentra el modelo y el segundo parámetro es una cadena de texto con el nombre del modelo.

4. Enlazalo las URLconf de tu nueva aplicación con con las urls de tu proyecto:

    path('aplicacion_nueva/',include(('aplicaciones.aplicacion_nueva.urls','aplicacion_nueva'))),

5. Ejecuta el comando python manage.py makemigrations

6. Ejecuta el comando python manage.py migrate

7. Inicia tu servidor con el comando python manage.py runserver

8. Accede a una ruta que no exista, por ejemplo: localhost:8000/aplicacion_nueva/ y le aparecerán todas las rutas generadas para
   el modelo indicado:

    aplicacion_nueva/ persona/ [name='aplicacion_nueva_persona_listar']

    aplicacion_nueva/ persona/<int:pk>/ [name='aplicacion_nueva_persona_absolute']

    aplicacion_nueva/ persona/crear/ [name='aplicacion_nueva_persona_crear']

    aplicacion_nueva/ persona/<int:pk>/actualizar/ [name='aplicacion_nueva_persona_actualizar']

    aplicacion_nueva/ persona/<int:pk>/eliminar/ [name='aplicacion_nueva_persona_eliminar']

    aplicacion_nueva/ persona/reporte_excel/ [name='aplicacion_nueva_persona_reporte_excel']
