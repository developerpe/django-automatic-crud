from django.db import models

from automatic_crud.models import BaseModel

class Category(BaseModel):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField('Nombre de Categoría', max_length=150)
    
    exclude_fields = ['date_created','date_modified','date_deleted']
    exclude_model = False
    server_side = False
    login_required = False
    model_permissions = False
    default_permissions = True
    all_cruds_types = True
    ajax_crud = True


    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Categoria'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

    def natural_key(self):
        return self.name

class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField('Nombre de Producto', max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
    


