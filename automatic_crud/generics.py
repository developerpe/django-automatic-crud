from django.views.generic import View

class BaseCrud(View):
    model = None
    data = None

    def get_fields_for_model(self):
        """
        Return fields for model excluding exclude_fields of model
        """
        fields = [field.name for field in self.model._meta.get_fields()]
        for field in self.model.exclude_fields:            
            if field in fields:
                fields.remove(field)
        return fields