# Django Automatic CRUD (CRUD Automáticos con Django)

Django Automatic CRUD es un proyecto que genera CRUDS automáticos para cada modelo que tenga la herencia indicada mas adelante. Estos CRUDS y URLS pueden ser de 2 tipos: **Normales y AJAX**.

## Documentación

Para una documentación mas detallada visitar: [Documentación Django Automatic CRUD](https://django-automatic-crud.readthedocs.io/es/latest/index.html)

## Nota

**CRUDS Normales ** - Estos CRUDS son accesibles utilizando el Sistema de Plantillas de Django e incluyen validaciones de errores, existencia de templates, inicio de sesión y permisos.

**CRUDS AJAX ** - Estos CURDS son accesibles utilizando JavaScript o cualquier herramienta que permita realizar una petición a una URL indicada.

## Características

- CRUDS automáticos con sólo crear los modelos.
- URLS generadas automáticamente para cada tipo de CRUD de modelo.
- Ruta para generación automática de un Reporte en formato Excel.
- Validación de Inicio de Sesión.
- Validación de Permisos.
- CRUDS automáticos independientes, es decir, pueden generarse de los 2 tipos, sólo de uno o independiente.
- Campos a excluir para listado, registro, edición y detalle de modelo de forma dinámica.
- Mensajes de error automáticos y customizables.
- Nombre de templates para CRUDS customizables.
- Form de Django para CRUDS dinámico.
- Server-side.
- Paginación de datos.

## Pre-Requisitos

- Django >= 2.2
- Python >= 3.3

## Instalación Rápida

- Crea un entorno virtual e inicialo.
- Ejecuta el siguiente comando desde tu consola:

```
    pip install django-automatic-crud
```

- Agrega automatic_crud a tu INSTALLED_APPS:

```
    INSTALLED_APPS = [
        ...
        'automatic_crud',
        ...
    ]
```

## Generación de CRUDS

- Para cada modelo que desees generar los CRUDS, deben heredar de BaseModel, por ejemplo:

```python

    from automatic_crud.models import BaseModel

    class NewModel(BaseModel):
        ...

```

- Agrega la siguiente linea en tu archivo urls.py global:

```python
    path('automatic-crud/',include('automatic_crud.urls'))
```

- Ahora, ingresa a tu navegador y escribe una ruta que no exista para que Django pueda mostrarte todas las rutas existentes, te mostrará 14 rutas para cada modelo que herede de BaseModel, las cuales estarán dentro de la estructura de ruta: `http://localhost:8000/automatic-crud/` y tendrán el siguiente patrón:

```python

    automatic_crud/ app_name/ model_name / list / [name="app_name-model_name-list"]
    automatic_crud/ app_name/ model_name / create / [name="app_name-model_name-create"]
    automatic_crud/ app_name/ model_name / detail / <int:pk>/ [name="app_name-model_name-detail"]
    automatic_crud/ app_name/ model_name / update / <int:pk>/ [name="app_name-model_name-update"]
    automatic_crud/ app_name/ model_name / logic-delete / <int:pk>/ [name="app_name-model_name-logic-delete"]
    automatic_crud/ app_name/ model_name / direct-delete / <int:pk>/ [name="app_name-model_name-direct-delete"]
    automatic_crud/ app_name/ model_name / excel-report / [name="app_name-model_name-excel-report"]

    automatic_crud/ ajax-app_name/ model_name / list / [name="app_name-model_name-list-ajax"]
    automatic_crud/ ajax-app_name/ model_name / create / [name="app_name-model_name-create-ajax"]
    automatic_crud/ ajax-app_name/ model_name / detail / <int:pk>/ [name="app_name-model_name-detail-ajax"]
    automatic_crud/ ajax-app_name/ model_name / update / <int:pk>/ [name="app_name-model_name-update-ajax"]
    automatic_crud/ ajax-app_name/ model_name / logic-delete / <int:pk>/ [name="app_name-model_name-logic-delete-ajax"]
    automatic_crud/ ajax-app_name/ model_name / direct-delete / <int:pk>/ [name="app_name-model_name-direct-delete-ajax"]
    automatic_crud/ ajax-app_name/ model_name / excel-report / [name="app_name-model_name-excel-report-ajax"]

```

---

Si quieres apoyar realizando una donación, puedes hacerla a este enlace:

- [Donación al Proyecto](https://www.paypal.com/paypalme/oliversando)

## Redes Sociales

[Web](http://www.developerpe.com)

[Facebook](https://www.facebook.com/developerper​)

[Instagram](https://www.instagram.com/developer.pe/​)

[Twitter](https://twitter.com/Developerpepiur​)

[Youtube](Developer.pe)

**Correo: developerpeperu@gmail.com**
