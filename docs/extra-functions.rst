Funciones Extra
===============

get\_model
----------

.. code:: python

    def get_model(__app_name:str,__model_name:str) -> Instance:
        # return the model corresponding to the application name and model name sent
        return apps.get_model(app_label = __app_name,model_name = __model_name)

-  **\_\_app\_name** - Nombre de la aplicación donde está el modelo en
   cadena de texto
-  **\_\_model\_name** - Nombre del modelo en cadena de texto

Retorna el modelo en cuestión para el nombre de la aplicación y modelo
indicados.

get\_object
-----------

.. code:: python

    def get_object(model: Instance,pk: int):
        # return the record for a pk sended
        instance = model.objects.filter(id = pk,model_state = True).first()
        if instance:
            return instance
        return None

-  **model** - Modelo a realizar la consulta.
-  **pk** - ID de registro a buscar.

Retorna la instancia del modelo perteneciente al pk enviado.

get\_model\_fields\_names
-------------------------

.. code:: python

    def get_model_fields_names(__model: Instance) -> List:
        # return a list of field names from a model
        return [name for name,_ in models.fields_for_model(__model).items()]

-  \*\*\_\_model\*\* - Modelo del cual se desea obtener los nombres de
   sus campos.

Retorna una lista con los nombres de los campos del modelo enviado.

get\_queryset
-------------

.. code:: python

    def get_queryset(__model:Instance) -> Dict:
        # returns all records in a dictionary for a model
        return __model.objects.all().values()

-  \*\*\_\_model\*\* - Modelo del cual se desea obtener los nombres de
   sus campos.

Retorna todos los datos registrados en la base de datos para el modelo
indicado. Esta función se utiliza en el Reporte en Excel generado
automáticamente.

get\_form
---------

.. code:: python

    def get_form(form: DjangoForm,model: Instance) -> DjangoForm:
        """
        Return a Django Form for a model, also a Django Form can be indicated
        by default the Django Form will exclude the 'state' field from the model

        """


        if form is not None:
            return models.modelform_factory(model = model,form = form)
        else:
            return models.modelform_factory(model = model,exclude = ('model_state',))

-  **model** - Modelo en el cual se desea basar el Form de Django a
   crearse.
-  **form** - Form de Django opcional a utilizarse en la creación de un
   Form de Django basado en modelo.

Retorna un Form de Django basado en el modelo indicado. Opcionalmente
recibe el parámetro form, el cuál se utilizará para generarlo el nuevo
Form en caso se desee utilizar uno personalizado. Para que el Form se
genere automáticamente sin necesidad de enviarle el parámetro ``form``,
este debe ser enviado como None.

build\_template\_name
---------------------

.. code:: python

    def build_template_name(template_name: str,model: Instance,action:str) -> str:
        """
        Build template name with app label from model, model name and action(list,create,update,detail)

        """


        if template_name == None:
            template_name = '{0}/{1}_{2}.html'.format(
                                            model._meta.app_label,
                                            model._meta.object_name.lower(),
                                            action
                                        )
        return template_name

-  **model** - Modelo del cuál se desea generar los nombres de templates
   solicitados en CRUDS Normales.
-  **template\_name** - Nombre del template a utilizarse en la vista de
   CRUDS Normales.

