CRUDS AJAX
==========

BaseListAJAX
------------

.. code:: python

    class BaseListAJAX(BaseCrud):
        pass

Vista Basada en Clase encargada de generar y retornar el listado de
registros para el modelo que se le haya indicado de forma automática.

Recibe herencia de ``BaseCrud``, la cuál se encarga de realizar las
validaciones correspondientes a permisos y login\_required.

El listado de registros obtenidos para el modelo será retornado en
formato JSON y puede ser de 2 tipos:

**SERVER SIDE**

Retornará los datos paginados y sólo aquellos cuyo campo ``model_state``
sea ``True`` con la siguiente estructura por página:

::

    {
        'length': # número de registros,
        'objects': # listado de registros
    }

    Ejemplo:
        
        {
            "length": 6,
            "objects": [
                {
                    "pk": 1,
                    "fields":{
                        "name": "abarrote",
                        "modal_state": true,
                    },
                    "index": 1
                },
                {
                    "pk": 1,
                    "fields":{
                        "name": "carro",
                        "modal_state": true,
                    },
                    "index": 1
                }
            ]
        }

El campo ``index`` es la numeración para la tabla que se utilizará en
caso desee enumerar cada item.

Y deben ser enviados en el request.GET los parámetros:

-  **start** : número de elemento donde la página iniciará.

-  **end** : número de elemento donde la página terminará.

-  **order\_by** : campo por el cuál los datos se ordenarán.

Por defectos estos valores serán 0, 10, id respectivamente.

Los campos que se hayan colocado como excluidos en el modelo, es decir
en el campo ``exclude_fields`` del modelo no serán tomados en cuenta
para el listado de datos

Para activar Server Side, revisar el apartado
`BaseModel <base-model.md#atributos-de-modelos-que-hereden-de-basemodel>`__

Para mas información o información aún mas detallada, revisar el
siguiente vídeo `Server Side con
Django <https://www.youtube.com/watch?v=89Ur7GCyLxI>`__

**NO SERVER SIDE**

Retornará todos los registros del modelo que se encuentren en la Base de
Datos cuyo campo ``model_state`` sea ``True``.

::

    Ejemplo:

        [
            {
                "pk": 1,
                "fields": {
                    "model_state": true,
                    "name": "abarrote"
                }
            },
            {
                "pk": 2,
                "fields": {
                    "model_state": true,
                    "name": "carro"
                }
            }
        ]

Para desactivar Server Side, revisar el apartado
`BaseModel <base-model.md#atributos-de-modelos-que-hereden-de-basemodel>`__

BaseCreateAJAX
--------------

.. code:: python

    class BaseCreateAJAX(BaseCrud):
        pass

Vista Basada en Clase encargada de realizar un nuevo registro para el
modelo indicado automáticamente.

Recibe herencia de ``BaseCrud``, la cuál se encarga de realizar las
validaciones correspondientes a permisos y login\_required.

Los nombres de los campos que deben ser enviados en la petición,
request.POST, deben tener el mismo nombre que tienen estos en el modelo.

Al registrar correctamente la instancia o haber problemas al
registrarla, retornará una respuesta de tipo JSON de la siguiente
manera:

::

    Registro Correcto

        {
            "message": "Categoria registrado correctamente!",
            "error": "Ninguno"
        }

    Registro Incorrecto

        {
            "message": "Categoria no se ha podido registrar!",
            "error": {
                        "name": [
                            "This field is required."
                        ]
                     }
        }

Los errores retornados son por campo y por defecto retornará los que
Django haya reconocido automáticamente de los modelos, si desea utilizar
errores personalizados deberá utilizar un Form de Django personalizado,
el cual debe indicarlo en el modelo.

**FORM PERSONALIZADO**

Si se desea utilizar un Form de Django personalizado para el registro o
edición de un modelo deberá sobreescribir los siguientes métodos en su
modelo:

.. code:: python

    EJEMPLO

    # form para crear
    def get_create_form(self,form = None):
        from test_app.forms import CategoryForm
        self.create_form = CategoryForm
        return self.create_form 

    # form para actualizar
    def get_update_form(self,form = None):
        from test_app.forms import CategoryForm
        self.update_form = CategoryForm
        return self.update_form

Siempre deberá importar el form personalizado **dentro de la función**,
nunca fuera de ella, esto para evitar un error conocido como
``Importación Circular``.

BaseDetailAJAX
--------------

.. code:: python

    class BaseDetailAJAX(BaseCrud):
        pass

Vista Basada en Clase encargada de retornar la instancia del modelo que
se le haya indicado de forma automática.

Recibe herencia de ``BaseCrud``, la cuál se encarga de realizar las
validaciones correspondientes a permisos y login\_required.

Retorna la información del objeto en formato JSON.

::

    Ejemplo

        {
            "pk": 1,
            "fields": {
                "model_state": true,
                "name": "abarrote"
            }
        }

Los campos retornados son aquellos que no estén incluidos en el atributo
del modelo ``exclude_fields``

BaseUpdateAJAX
--------------

.. code:: python

    class BaseUpdateAJAX(BaseCrud):
        pass

Vista Basada en Clase encargada de realizar la actualización de un
registro para el modelo indicado automáticamente.

Recibe herencia de ``BaseCrud``, la cuál se encarga de realizar las
validaciones correspondientes a permisos y login\_required.

Los nombres de los campos que deben ser enviados en la petición,
request.POST, deben tener el mismo nombre que tienen estos en el modelo.

Al actualizar correctamente la instancia o haber problemas al
actualizar, retornará una respuesta de tipo JSON de la siguiente manera:

::

    Actualización Correcto

        {
            "message": "Categoria actualizada correctamente!",
            "error": "Ninguno"
        }

    Actualización Incorrecto

        {
            "message": "Categoria no se ha podido actualizar!",
            "error": {
                        "name": [
                            "This field is required."
                        ]
                     }
        }

Los errores retornados son por campo y por defecto retornará los que
Django haya reconocido automáticamente de los modelos, si desea utilizar
errores personalizados deberá utilizar un Form de Django personalizado,
el cual debe indicarlo en el modelo.

**FORM PERSONALIZADO**

Si se desea utilizar un Form de Django personalizado para el registro o
edición de un modelo deberá sobreescribir los siguientes métodos en su
modelo:

.. code:: python

    EJEMPLO

    # form para crear
    def get_create_form(self,form = None):
        from test_app.forms import CategoryForm
        self.create_form = CategoryForm
        return self.create_form 

    # form para actualizar
    def get_update_form(self,form = None):
        from test_app.forms import CategoryForm
        self.update_form = CategoryForm
        return self.update_form

Siempre deberá importar el form personalizado **dentro de la función**,
nunca fuera de ella, esto para evitar un error conocido como
``Importación Circular``.

BaseDirectDeleteAJAX
--------------------

.. code:: python

    class BaseDirectDeleteAJAX(BaseCrud):
        pass

Vista Basada en Clase encargada de realizar la eliminación directa en la
Base de Datos de un registro para el modelo indicado automáticamente.

Recibe herencia de ``BaseCrud``, la cuál se encarga de realizar las
validaciones correspondientes a permisos y login\_required.

La respuesta dependerá de si se encontró o no el objeto que se desea
eliminar.

::

    Objeto encontrado

        {
            "message": "Categoria eliminado correctamente!",
            "error": "Ninguno"
        }

    Objeto no encontrado

        {
            "error": "No se ha encontrado un registro con estos datos."
        }

BaseLogicDeleteAJAX
-------------------

.. code:: python

    class BaseLogicDeleteAJAX(BaseCrud):
        pass

Vista Basada en Clase encargada de realizar la eliminación lógica de un
registro para el modelo indicado automáticamente, es decir, colocará el
campo ``model_state`` en ``False``.

Recibe herencia de ``BaseCrud``, la cuál se encarga de realizar las
validaciones correspondientes a permisos y login\_required.

La respuesta dependerá de si se encontró o no el objeto que se desea
eliminar.

::

    Objeto encontrado

        {
            "message": "Categoria eliminado correctamente!",
            "error": "Ninguno"
        }

    Objeto no encontrado

        {
            "error": "No se ha encontrado un registro con estos datos."
        }

