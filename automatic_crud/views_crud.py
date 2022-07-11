from django.shortcuts import render,redirect
from django.views.generic import (
    CreateView,DeleteView,UpdateView,DetailView,
    ListView
)
from django.core.paginator import Paginator

from .generics import BaseCrudMixin
from .utils import get_object,get_form,build_template_name

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

        context['app'] = self.model._meta.app_label
        context['model'] = self.model.__name__.lower()
        context['title'] = self.model._meta.verbose_name
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
        context = {
            'form': form,
            'title': self.model._meta.verbose_name,
            'model': self.model.__name__.lower(),
            'app': self.model._meta.app_label
        }
        return render(request, self.template_name, context)    

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
                'form':form,
                'title': self.model._meta.verbose_name,
                'model': self.model.__name__.lower(),
                'app': self.model._meta.app_label
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
        context['app'] = self.model._meta.app_label
        context['model'] = self.model.__name__.lower()
        context['title'] = self.model._meta.verbose_name
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
        context['app'] = self.model._meta.app_label
        context['model'] = self.model.__name__.lower()
        context['title'] = self.model._meta.verbose_name
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
                    'form':form,
                    'title': self.model._meta.verbose_name,
                    'model': self.model.__name__.lower(),
                    'app': self.model._meta.app_label
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

    def get_deleted_objects(self, objs, request):
        from django.db import router
        from django.utils.text import capfirst
        from django.contrib.admin.utils import NestedObjects
        
        """
        Find all objects related to ``objs`` that should also be deleted. ``objs``
        must be a homogeneous iterable of objects (e.g. a QuerySet).
        Return a nested list of strings suitable for display in the
        template with the ``unordered_list`` filter.
        """
        try:
            obj = objs[0]
        except IndexError:
            return [], {}, set(), []
        else:
            using = router.db_for_write(obj._meta.model)
        collector = NestedObjects(using=using)
        collector.collect(objs)
        perms_needed = set()

        def format_callback(obj):
            model = obj.__class__
            opts = obj._meta

            no_edit_link = "%s: %s" % (capfirst(opts.verbose_name), obj)
            # Don't display link to edit, because it either has no
            # admin or is edited inline.
            return no_edit_link

        to_delete = collector.nested(format_callback)

        protected = [format_callback(obj) for obj in collector.protected]
        model_count = {
            model._meta.verbose_name_plural: len(objs)
            for model, objs in collector.model_objs.items()
        }

        return to_delete, model_count, perms_needed, protected

    def get_context_data(self, **kwargs):
        delete_objects, model_count, _, _ = self.get_deleted_objects([self.get_object()], self.request)
        context = super(BaseDirectDelete, self).get_context_data(**kwargs)
        context['app'] = self.model._meta.app_label
        context['model'] = self.model.__name__.lower()
        context['title'] = self.model._meta.verbose_name
        context['child_object'] = delete_objects[1:]
        context['child_object_count'] = model_count
        return context

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