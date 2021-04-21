# Resgistro de Modelos

La magia de la automatización de Django Automatic CRUD recae en esta funcionalidad, dentro de la instalación del paquete, es necesario incluir las rutas del paquete como tal en el archivo urls.py del proyecto donde se vaya a utilizar, esto se realiza por un motivo en específico que en si, es el motivo principal.

Cuando nosotros vinculamos estas rutas, lo que hacemos en si es llamar a la función `register_models` ya que el archivo urls de Django Automatic CRUD lo que contiene es:

```python
from automatic_crud.register import register_models

urlpatterns = []

urlpatterns += register_models()
```

Esta función lo que realiza es una iteración de todos los modelos que existen dentro de las aplicaciones registradas en el proyecto donde se esté utilizando, excluyendo los modelos: `ContentType,LogEntry,Session,Permission,Group`.

Las validaciones que se hacen es que si o si el modelo debe ser de tipo `BaseModel` o que tenga los atributos de este tipo de modelos, se valida que el modelo tenga el atributo `exclude_model` en `True` y para agregar las URLS de cada tipo de CRUD que Django Automatic CRUD permite, es decir, tomando en cuenta los atributos del modelo `all_cruds_types, ajax_crud y normal_cruds`.

Finalmente se retornan las rutas generadas para cada modelo ya que en cada iteración por cada modelo se agregan las rutas a un listado de rutas que estarán en la variable `urlpatterns`.