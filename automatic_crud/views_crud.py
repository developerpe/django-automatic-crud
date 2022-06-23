from django.shortcuts import render,redirect
from django.views.generic import (
    CreateView,DeleteView,UpdateView,DetailView,
    ListView
)
from django.core.paginator import Paginator

from automatic_crud.generics import BaseCrudMixin
from automatic_crud.utils import get_object,get_form,build_template_name

class BaseList(BaseCrudMixin, ListView):

    def dispatch(self, request, *args, **kwargs):
        # login required validation
        validation_login_required, response = self.validate_login_required()
        if validation_login_required:
            return response
        
        # permission required validation
        validation_permissions, response = self.validate_permissions()
        if validation_permissions:
            return response

        return super().dispatch(request, *args, **kwargs)    

    def get_queryset(self):
        return self.model.objects.filter(model_state=True)

    def get_context_data(self, **kwargs):
        context = {}
        data = self.get_queryset()
        
        if self.model.normal_pagination:
            paginator = Paginator(data, self.model.values_for_page)
            page_number = self.request.GET.get('page', '1')
            data = paginator.get_page(page_number)
        
        context['object_list'] = data
        return context

    def get(self, request, *args, **kwargs):
        self.template_name = build_template_name(self.template_name, self.model, 'list')
        return render(request, self.template_name, self.get_context_data())

class BaseCreate(BaseCrudMixin, CreateView):
    
    def dispatch(self, request, *args, **kwargs):
        # login required validation
        validation_login_required, response = self.validate_login_required()
        if validation_login_required:
            return response
        
        # permission required validation
        validation_permissions, response = self.validate_permissions()
        if validation_permissions:
            return response

        return super().dispatch(request, *args, **kwargs)    

    def get(self, request, form=None, *args, **kwargs):
        self.template_name = build_template_name(self.template_name, self.model, 'create')
        form = get_form(form, self.model)
        return render(request, self.template_name,{'form': form})    

    def post(self, request, form=None, *args, **kwargs):
        self.template_name = build_template_name(self.template_name, self.model, 'list')
        form = get_form(form, self.model)
        
        if self.form_class == None:    
            form = form(request.POST, request.FILES)
        else:
            form = self.form_class(request.POST, request.FILES)     
        
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            form = self.form_class()
            context = {
                'form':form
            }
            return render(request, self.template_name, context)

class BaseDetail(BaseCrudMixin, DetailView):
    def dispatch(self, request, *args, **kwargs):
        # login required validation
        validation_login_required, response = self.validate_login_required()
        if validation_login_required:
            return response
        
        # permission required validation
        validation_permissions, response = self.validate_permissions()
        if validation_permissions:
            return response

        return super().dispatch(request, *args, **kwargs)    

    def get_context_data(self, **kwargs):
        context = {}
        context['object'] = get_object(self.model,self.kwargs['pk'])
        return context  

    def get(self, request, form=None, *args, **kwargs):
        self.template_name = build_template_name(self.template_name, self.model, 'detail')
        return render(request, self.template_name, self.get_context_data())

class BaseUpdate(BaseCrudMixin, UpdateView):

    def dispatch(self, request, *args, **kwargs):
        # login required validation
        validation_login_required, response = self.validate_login_required()
        if validation_login_required:
            return response
        
        # permission required validation
        validation_permissions, response = self.validate_permissions()
        if validation_permissions:
            return response

        return super().dispatch(request, *args, **kwargs)   
    
    def get_context_data(self, **kwargs):
        context = {}
        context['object'] = get_object(self.model, self.kwargs['pk'])
        return context    

    def get(self, request, form=None, *args, **kwargs):
        self.template_name = build_template_name(self.template_name, self.model, 'update')
        
        form = get_form(form, self.model)
        form = form(instance=get_object(self.model, self.kwargs['pk']))
        
        context = self.get_context_data()
        if context['object'] == None:
            return redirect(self.success_url)        
        
        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, form=None, *args, **kwargs):
        self.template_name = build_template_name(self.template_name, self.model, 'list')
        form = get_form(form, self.model)
        
        instance = get_object(self.model, self.kwargs['pk'])
        if instance is not None:
            if self.form_class == None:
                form = form(request.POST, request.FILES, instance=instance)
            else:
                form = self.form_class(request.POST, request.FILES, instance=instance)   
            if form.is_valid():
                form.save()
                return redirect(self.success_url)
            else:
                form = self.form_class()
                context = {
                    'form':form
                }
                return render(request, self.template_name, context)
        else:
            return redirect(self.success_url)

class BaseDirectDelete(BaseCrudMixin, DeleteView):
    def dispatch(self, request, *args, **kwargs):
        # login required validation
        validation_login_required, response = self.validate_login_required()
        if validation_login_required:
            return response
        
        # permission required validation
        validation_permissions, response = self.validate_permissions()
        if validation_permissions:
            return response

        return super().dispatch(request, *args, **kwargs)    

class BaseLogicDelete(BaseCrudMixin, DeleteView):

    def dispatch(self, request, *args, **kwargs):
        # login required validation
        validation_login_required, response = self.validate_login_required()
        if validation_login_required:
            return response
        
        # permission required validation
        validation_permissions, response = self.validate_permissions()
        if validation_permissions:
            return response

        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = get_object(self.model, self.kwargs['pk'])
        
        if instance is not None:
            self.model.objects.filter(id=self.kwargs['pk']).update(model_state=False)
            return redirect(self.success_url)        
        else:
            return redirect(self.success_url)