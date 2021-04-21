# CRUDS Normales

## BaseList

```python
class BaseList(BaseCrudMixin,ListView):
    pass
```

Vista Basada en Clase encargada de generar y retornar el listado de registros para el modelo que se le haya indicado de forma automática.

Recibe herencia de BaseCrudMixin, la cuál se encarga de realizar las validaciones correspondientes a permisos y login_required, y de la clase Genérica de Django, ListView.

El listado de registros obtenidos para el modelo indicado serán retornados al template bajo el nombre de `object_list`

## BaseCreate

```python
class BaseCreate(BaseCrudMixin,CreateView):
    pass
```

Vista Basada en Clase encargada de generar y retornar el Form de Django para el agregar registros del modelo que se le haya indicado de forma automática.

Al registrar correctamente la instancia, redireccionará automáticamente a la ruta de Listado de CRUDS Normales.

Recibe herencia de BaseCrudMixin, la cuál se encarga de realizar las validaciones correspondientes a permisos y login_required, y de la clase Genérica de Django, CreateView.

Retorna el form de Django para el modelo al template bajo el nombre de `form`.

## BaseDetail

```python
class BaseDetail(BaseCrudMixin,DetailView):
    pass
```

Vista Basada en Clase encargada de retornar la instancias del modelo que se le haya indicado de forma automática.

Recibe herencia de BaseCrudMixin, la cuál se encarga de realizar las validaciones correspondientes a permisos y login_required, y de la clase Genérica de Django, DetailView.

Retorna la instancia del modelo al template bajo el nombre de `object`.

## BaseUpdate

```python
class BaseUpdate(BaseCrudMixin,UpdateView):
    pass
```

Vista Basada en Clase encargada de generar y retornar el Form de Django para la edición de una instancia del modelo que se le haya indicado de forma automática.

Al editar correctamente la instancia, redireccionará automáticamente a la ruta de Listado de CRUDS Normales.

Recibe herencia de BaseCrudMixin, la cuál se encarga de realizar las validaciones correspondientes a permisos y login_required, y de la clase Genérica de Django, UpdateView.

Retorna el form de Django para el modelo al template bajo el nombre de `form`.

Retorna la instancia del modelo al template bajo el nombre de `object`.

## BaseDirectDelete

```python
class BaseDirectDelete(BaseCrudMixin,DeleteView):
    pass
```

Vista Basada en Clase encargada de eliminar directamente de la Base de Datos la instancia del modelo que se le haya indicado de forma automática.

Recibe herencia de BaseCrudMixin, la cuál se encarga de realizar las validaciones correspondientes a permisos y login_required, y de la clase Genérica de Django, DeleteView. 

Al eliminar correctamente la instancia, redireccionará automáticamente a la ruta de Listado de CRUDS Normales.

## BaseLogicDelete

```python
class BaseLogicDelete(BaseCrudMixin,DeleteView):
    pass
```

Vista Basada en Clase encargada de eliminar de forma lógica, es decir cambiando el campo `model_state` a `False` de la instancia del modelo que se le haya indicado de forma automática.

Recibe herencia de BaseCrudMixin, la cuál se encarga de realizar las validaciones correspondientes a permisos y login_required, y de la clase Genérica de Django, DeleteView. 

Al eliminar correctamente la instancia, redireccionará automáticamente a la ruta de Listado de CRUDS Normales.