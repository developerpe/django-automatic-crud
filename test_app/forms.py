from django import forms
from test_app.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('model_state',)
    
    def clean_name(self):
        data = self.cleaned_data['name']
        if data != '' or data is not None:
            print("Hola desde form personalizado")
        return data

