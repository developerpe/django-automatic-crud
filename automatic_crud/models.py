from django.db import models
from django.urls import path
from django.contrib.auth.decorators import login_required

from automatic_crud.utils import get_model
from automatic_crud.data_types import *
from automatic_crud.base_report import GetExcelReport
from automatic_crud.views_crud import *
from automatic_crud.views_crud_ajax import *

class BaseModel(models.Model):
    """Model definition for BaseModel."""

    # TODO: Define fields here
    id = models.AutoField(primary_key = True)
    model_state = models.BooleanField(default = True)
    date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
    date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)
    date_deleted = models.DateTimeField('Fecha de Eliminación', auto_now=True, auto_now_add=False)  
    
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

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True

    def build_message(self,message:str,custom_message = False):
        if custom_message:
            return "{0}".format(message)
        return "{0} {1}".format(self._meta.verbose_name,message)

    def get_create_url(self):
        return "{0}/create/".format(self._meta.object_name.lower())
    
    def get_list_url(self):
        return "{0}/list/".format(self._meta.object_name.lower())
    
    def get_direct_delete_url(self):
        return "{0}/direct-delete/<int:pk>/".format(self._meta.object_name.lower())

    def get_logic_delete_url(self):
        return "{0}/logic-delete/<int:pk>/".format(self._meta.object_name.lower())

    def get_update_url(self):
        return "{0}/update/<int:pk>/".format(self._meta.object_name.lower())
    
    def get_detail_url(self):
        return "{0}/detail/<int:pk>/".format(self._meta.object_name.lower())
    
    def get_excel_report_url(self):
        return "{0}/excel-report/".format(self._meta.object_name.lower())
    
    def get_alias_create_url(self):
        return "{0}-{1}-create".format(self._meta.app_label,self._meta.object_name.lower())

    def get_alias_list_url(self):
        return "{0}-{1}-list".format(self._meta.app_label,self._meta.object_name.lower())

    def get_alias_logic_delete_url(self):
        return "{0}-{1}-logic-delete".format(self._meta.app_label,self._meta.object_name.lower())

    def get_alias_direct_delete_url(self):
        return "{0}-{1}-direct-delete".format(self._meta.app_label,self._meta.object_name.lower())

    def get_alias_update_url(self):
        return "{0}-{1}-update".format(self._meta.app_label,self._meta.object_name.lower())

    def get_alias_detail_url(self):
        return "{0}-{1}-detail".format(self._meta.app_label,self._meta.object_name.lower())

    def get_alias_excel_report_url(self):
        return "{0}-{1}-excel-report".format(self._meta.app_label,self._meta.object_name.lower())

    def build_generics_urls_crud(self,__list_url : str,       
                                    __form: DjangoForm,                                                                 
                                    __list_template_name: str,
                                    __create_template_name: str) -> URLList:
        
        __model = get_model(self._meta.app_label,self._meta.object_name)

        urlpatterns = [
            path(
                "{0}/{1}".format(__app_name,self.get_list_url()),
                login_required(BaseList.as_view(
                    template_name = __list_template_name,model = __model
                )),
                name = self.get_alias_list_url()
            ),
            path(
                "{0}/{1}".format(__app_name,self.get_create_url()),
                login_required(BaseCreate.as_view(
                    template_name = __list_template_name,model = __model,
                    form_class = __form,success_url = reverse_lazy("{0}:{1}".format(__app_name,__list_url))
                )),
                name = self.get_alias_create_url()
            ),
            path(
                "{0}/{1}".format(__app_name,self.get_detail_url()),
                login_required(BaseDetail.as_view(model = __model)),
                name = self.get_alias_detail_url()
            ),
            path(
                "{0}/{1}".format(__app_name,self.get_update_url()),
                login_required(BaseUpdate.as_view(
                    template_name = __create_template_name,model = __model,
                    form_class = __form,success_url = reverse_lazy("{0}:{1}".format(__app_name,__list_url))
                )),
                name = self.get_alias_update_url()
            ),
            path(
                "{0}/{1}".format(__app_name,self.get_logic_delete_url()),
                login_required(BaseLogicDelete.as_view(
                    model = __model,
                    success_url = reverse_lazy("{0}:{1}".format(__app_name,__list_url))
                )),
                name = self.get_alias_logic_delete_url()
            ),
            path(
                "{0}/{1}".format(__app_name,self.get_direct_delete_url()),
                login_required(BaseDirectDelete.as_view(
                    model = __model,
                    success_url = reverse_lazy("{0}:{1}".format(__app_name,__list_url))
                )),
                name = self.get_alias_direct_delete_url()
            ),
            path(
                "{0}/{1}".format(__app_name,self.get_excel_report_url()),
                login_required(GetExcelReport.as_view()),{'__app_name':__app_name,'__model_name':__model_name},
                name = self.get_alias_excel_report_url()
            ),
        ]
        return urlpatterns

    def build_generics_urls_ajax_crud(self, __form = None) -> URLList:
        __app_name = self._meta.app_label
        __model_name = self._meta.object_name
        __model = get_model(__app_name,__model_name)
        __model_context = {
            'model':__model
        }
        __model_form_context = {
            'model':__model,
            'form':__form
        }

        urlpatterns = [
            path(
                "ajax-{0}/{1}".format(__app_name,self.get_list_url()),
                BaseListAJAX.as_view(),__model_context,
                name = "{0}-ajax".format(self.get_alias_list_url())
            ),
            path(
                "ajax-{0}/{1}".format(__app_name,self.get_create_url()),
                BaseCreateAJAX.as_view(),__model_form_context,
                name = "{0}-ajax".format(self.get_alias_create_url())
            ),
            path(
                "ajax-{0}/{1}".format(__app_name,self.get_detail_url()),
                BaseDetailAJAX.as_view(),__model_context,
                name = "{0}-ajax".format(self.get_alias_detail_url())
            ),
            path(
                "ajax-{0}/{1}".format(__app_name,self.get_update_url()),
                BaseUpdateAJAX.as_view(),__model_form_context,
                name = "{0}-ajax".format(self.get_alias_update_url())
            ),
            path(
                "ajax-{0}/{1}".format(__app_name,self.get_logic_delete_url()),
                BaseLogicDeleteAJAX.as_view(),__model_context,
                name = "{0}-ajax".format(self.get_alias_logic_delete_url())
            ),
            path(
                "ajax-{0}/{1}".format(__app_name,self.get_direct_delete_url()),
                BaseDirectDeleteAJAX.as_view(),__model_context,
                name = "{0}-ajax".format(self.get_alias_direct_delete_url())
            ),
            path(
                "ajax-{0}/{1}".format(__app_name,self.get_excel_report_url()),
                GetExcelReport.as_view(),{'_app_name':__app_name,'_model_name':__model_name},
                name = "{0}-ajax".format(self.get_alias_excel_report_url())
            ),
        ]

        return urlpatterns
