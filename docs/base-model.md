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

> model*state* es usado dentro de Django Automatic CRUD para la eliminación lógica.

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
    exclude_fields = ['date_created','date_modified','date_deleted','model_state']

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

## Atributos de modelos que hereden de BaseModel

- **all_cruds_types** - si su valor es `True` generará CRUDS de tipo: Normales y AJAX, en `False` no generará ningún CRUD.
- **normal_cruds** - si _all_cruds_types_ es `True`, el valor de este campo no será tomado en cuenta, si _all_cruds_types_ es `False` y este campo es `True`, generará CRUDS de tipo `Normal`.
- **ajax_crud** - si _all_cruds_types_ es `True`, el valor de este campo no será tomado en cuenta, si _all_cruds_types_ es `False` y este campo es `True`, generará CRUDS de tipo `AJAX`.
- **server_side** - si su valor es `True` se realizará la paginación del lado del servidor, esto es válido sólo para _CRUDS de tipo AJAX_, retornará la siguiente estructura:

        {
            'length': # número de registros,
            'objects': # lista de datos por página
        }

- **exclude_model** - si su valor es `True`, no se generarán CRUDS para el modelo, aún cuando _all_cruds_types_ sea `True`.
- **login_required** - si su valor es `True`, solicitará que un quien realice la petición haya iniciado sesión. Se recomiendo realizar un `login(user)` de Django en la implementación de su sistema de Login.
- **permission_required** - tupla de permisos a solicitarse para un usuario que realice la petición a cualquier ruta de Django Automatic CRUD sólo si _model_permission_ es `True`.
- **model_permissions** - si su valor es `True`, solicitará permisos para el usuario que realice la petición.
- **default_permissions** - si su valor es `True`, los permisos a solicitar serán los básicos de Django, es decir, add,change,view,delete.
- **exclude_fields** - lista de campos excluidos, estos campos no serán tomados en cuenta para listar, editar, crear o cuando se obtenga el detalle de un registro. Por defecto los campos excluidos son los campos: `date_created,date_modified,date_deleted,model_state`.

- **success_create_message** - mensaje por defecto mostrado cuando se realiza un nuevo registro del modelo. Este campo es concatenado con el nombre del modelo, es decir: `{model.__name__} success_create_message`, por ejemplo: `Persona registrada correctamente`. **Válido sólo para CRUDS AJAX**.
- **success_update_message** - mensaje por defecto mostrado cuando se realiza una edición de un registro del modelo. Este campo es concatenado con el nombre del modelo, al igual que _success_create_message_. **Válido sólo para CRUDS AJAX**.
- **success_delete_message** - mensaje por defecto mostrado cuando se realiza una eliminación de un registro del modelo, ya sea eliminación lógica o directa. Este campo es concatenado con el nombre del modelo, al igual que _success_create_message_. **Válido sólo para CRUDS AJAX**.

- **error_create_message** - mensaje por defecto mostrado cuando ocurre un error al realizarse un nuevo registro del modelo. Este campo es concatenado con el nombre del modelo, al igual que _success_create_message_. **Válido sólo para CRUDS AJAX**.
- **error_update_message** - mensaje por defecto mostrado cuando ocurre un error al realizarse una edición de un registro del modelo. Este campo es concatenado con el nombre del modelo, al igual que _success_create_message_. **Válido sólo para CRUDS AJAX**.
- **non_found_message** - mensaje por defecto mostrado cuando no se encuentra un obtjeto solicitado. **Válido sólo para CRUDS AJAX**.

- **create_template** - nombre de template de creación para los CRUDS Normales del modelo. Por defecto el sistema solicita un template llamado `{model.__name__}_create.html`.
- **update_template** - nombre de template de edición para los CRUDS Normales del modelo. Por defecto el sistema solicita un template llamado `{model.__name__}_update.html`.
- **list_template** - nombre de template de listado para los CRUDS Normales del modelo. Por defecto el sistema solicita un template llamado `{model.__name__}_list.html`.
- **detail_template** - nombre de template de detalle para los CRUDS Normales del modelo. Por defecto el sistema solicita un template llamado `{model.__name__}_detail.html`.


**NOTA**

El nombre solicitado de forma automática por los templates para  CRUDS Normales son generados por una función llamada build_template_name, puedes encontrar información en [build_template_name](extra-functions.md#build_template_name)