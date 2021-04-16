from django.shortcuts import render,redirect
from django.forms.models import modelform_factory
from django.views.generic import (
    CreateView,DeleteView,UpdateView,DetailView,
    ListView,View
)

from automatic_crud.generics import BaseCrudMixin
from automatic_crud.utils import get_object,get_form

class BaseList(BaseCrudMixin,ListView):
    
    def get_queryset(self):
        return self.model.objects.filter(model_state = True)

class BaseCreate(BaseCrudMixin,CreateView):
    
    def dispatch(self, request, *args, **kwargs):
        # login required validation
        validation_login_required,response = self.validate_login_required()
        if validation_login_required:
            return response
        
        # permission required validation
        validation_permissions,response = self.validate_permissions()
        if validation_permissions:
            return response

        return super().dispatch(request, *args, **kwargs)    

    def post(self,request,form = None,*args,**kwargs):
        form = get_form(self.model,form)        
        form = self.form_class(request.POST,request.FILES)        
        if form.is_valid():
            form.save()
            url = self.succes_url
            return redirect(url)
        else:
            form = self.form_class()
            context = {
                'form':form
            }
            return render(request,self.template_name, context)

class BaseDetail(BaseCrudMixin,DetailView):
    def dispatch(self, request, *args, **kwargs):
        # login required validation
        validation_login_required,response = self.validate_login_required()
        if validation_login_required:
            return response
        
        # permission required validation
        validation_permissions,response = self.validate_permissions()
        if validation_permissions:
            return response

        return super().dispatch(request, *args, **kwargs)    


class BaseUpdate(BaseCrudMixin,UpdateView):

    def dispatch(self, request, *args, **kwargs):
        # login required validation
        validation_login_required,response = self.validate_login_required()
        if validation_login_required:
            return response
        
        # permission required validation
        validation_permissions,response = self.validate_permissions()
        if validation_permissions:
            return response

        return super().dispatch(request, *args, **kwargs)   

    def put(self,request,model,form = None,*args,**kwargs):
        form = get_form(self.model,form)
        
        instance = get_object(self.model,self.kwargs['pk'])
        if instance is not None:
            form = self.form_class(request.POST,request.FILES, instance = instance)        
            if form.is_valid():
                form.save()
                url = self.succes_url
                return redirect(url)
            else:
                form = self.form_class()
                context = {
                    'form':form
                }
                return render(request,self.template_name, context)
        else:
            return redirect(url)

class BaseDirectDelete(BaseCrudMixin,DeleteView):
    def dispatch(self, request, *args, **kwargs):
        # login required validation
        validation_login_required,response = self.validate_login_required()
        if validation_login_required:
            return response
        
        # permission required validation
        validation_permissions,response = self.validate_permissions()
        if validation_permissions:
            return response

        return super().dispatch(request, *args, **kwargs)    

class BaseLogicDelete(BaseCrudMixin,DeleteView):
    model = None

    def dispatch(self, request, *args, **kwargs):
        # login required validation
        validation_login_required,response = self.validate_login_required()
        if validation_login_required:
            return response
        
        # permission required validation
        validation_permissions,response = self.validate_permissions()
        if validation_permissions:
            return response

        return super().dispatch(request, *args, **kwargs)

    def delete(self,request,model,url,*args,**kwargs):
        self.model = model
        instance = get_object(self.model,self.kwargs['pk'])
        
        if instance is not None:
            instance.update(model_state = False)
            return redirect(url)        
        else:
            return redirect(url)