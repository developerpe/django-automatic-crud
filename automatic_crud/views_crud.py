from django.shortcuts import render,redirect
from django.forms.models import modelform_factory
from django.views.generic import (
    CreateView,DeleteView,UpdateView,DetailView,ListView,View
)

from automatic_crud.utils import get_object

class BaseList(ListView):
    
    def get_queryset(self):
        return self.model.objects.filter(state = True)

class BaseCreate(CreateView):

    def post(self,request,form = None,*args,**kwargs):
        if form is not None:
            self.form_class = modelform_factory(model = self.model,form = form)
        
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

class BaseDetail(DetailView):
    pass

class BaseUpdate(UpdateView):

    def put(self,request,model,form = None,*args,**kwargs):
        if form is not None:
            self.form_class = modelform_factory(model = self.model,form = form)
        
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

class BaseDirectDelete(DeleteView):
    pass

class BaseLogicDelete(View):
    model = None

    def delete(self,request,model,url,*args,**kwargs):
        self.model = model
        instance = get_object(self.model,self.kwargs['pk'])
        
        if instance is not None:
            instance.update(state = False)
            return redirect(url)        
        else:
            return redirect(url)