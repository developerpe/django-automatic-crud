from automatic_crud.register import register_models
from test_app.models import Category

urlpatterns = []

urlpatterns += register_models()
