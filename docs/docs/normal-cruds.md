# CRUDS Normales

## BaseList

```python
class BaseList(BaseCrudMixin,ListView):
    pass
```

## BaseCreate

```python
class BaseCreate(BaseCrudMixin,CreateView):
    pass
```

## BaseDetail

```python
class BaseDetail(BaseCrudMixin,DetailView):
    pass
```

## BaseUpdate

```python
class BaseUpdate(BaseCrudMixin,UpdateView):
    pass
```

## BaseDirectDelete

```python
class BaseDirectDelete(BaseCrudMixin,DeleteView):
    pass
```

## BaseLogicDelete

```python
class BaseLogicDelete(BaseCrudMixin,DeleteView):
    pass
```
