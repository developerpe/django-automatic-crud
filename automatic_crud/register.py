from django.apps import apps

def register_models():
    """
    Register models with automatic cruds excluding models with exclude_model = True
    Return urlspatterns with automatic cruds
    """

    urlpatterns = []
    exclude_models = ['ContentType','LogEntry','Session','Permission','Group']
    models = apps.get_models()
    
    for model in models:
        try:
            if model.__name__ not in exclude_models:
                if not model.exclude_model:            
                    urlpatterns += model().build_generics_urls_ajax_crud()
        except:
            pass
    
    return urlpatterns