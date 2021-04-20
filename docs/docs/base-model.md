# BaseModel

BaseModel es el modelo padre de tipo **Abstracto**, tiene una herencia de `models.Model`, es decir:

```python

from django.db import models

class BaseModel(models.Model):

    class Meta:
        abstract = True

```

Aquí es donde se han definido las características principales de Django Automatic CRUD, es el enlace con los modelos ya que, a través de la herencia, todo modelo obtendrá los siguientes campos:

```python
id = models.AutoField(primary_key = True)
model_state = models.BooleanField(default = True)
date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)
date_deleted = models.DateTimeField('Fecha de Eliminación', auto_now=True, auto_now_add=False)
```

> model_state_ es usado dentro de Django Automatic CRUD para la eliminación lógica.

Y los siguientes atributos:

    all_cruds_types = True
    normal_cruds = False
    ajax_crud = False
    server_side = False
    exclude_model = False
    login_required = False
    permission_required = ()
    model_permissions = False
    default_permissions = False
    exclude_fields = ['date_created','date_modified','date_deleted','state']

    success_create_message = "registrado correctamente!"
    success_update_message = "actualizado correctamente!"
    success_delete_message = "eliminado correctamente!"

    error_create_message = "no se ha podido registrar!"
    error_update_message = "no se ha podido actualizar!"
    non_found_message = "No se ha encontrado un registro con estos datos!"

    create_template = None
    update_template = None
    list_template = None
    detail_template = None

- **all_cruds_types** - si su valor es `True` generará CRUDS de tipo: Normales y AJAX, en `False` _no generará ningún CRUD.  
- **normal_cruds** - si _all_cruds_types_ es `True`, el valor de este campo no será tomado en cuenta, si _all_cruds_types_ es `False` y este campo es `True`, generará CRUDS de tipo `Normal`.    
- **ajax_crud** - si _all_cruds_types_ es `True`, el valor de este campo no será tomado en cuenta, si _all_cruds_types_ es `False` y este campo es `True`, generará CRUDS de tipo `AJAX`.  
- **server_side** - si su valor es `True` se realizará la paginación del lado del servidor, esto es válido sólo para _CRUDS de tipo AJAX_, retornará la siguiente estructura:

        {
            'length': # número de registros,
            'objects': # lista de datos por página
        }  

- **exclude_model** - si su valor es `True`, no se generarán CRUDS para el modelo, aún cuando *all_cruds_types* sea `True`.   
- **login_required** - si su valor es `True`, solicitará que un quien realice la petición haya iniciado sesión. Se recomiendo realizar un `login(user)` de Django en la implementación de su sistema de Login.
- **permission_required** - tupla de permisos a solicitarse para un usuario que realice la petición a cualquier ruta de Django Automatic CRUD sólo si *model_permission* es `True`.
- **model_permissions** - si su valor es `True`, solicitará permisos para el usuario que realice la petición.
- **default_permissions** -
- **exclude_fields** -

- **success_create_message** -
- **success_update_message** -
- **success_delete_message** -

- **error_create_message** -
- **error_update_message** -
- **non_found_message** -

- **create_template** -
- **update_template** -
- **list_template** -
- **detail_template** -
