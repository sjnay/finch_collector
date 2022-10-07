
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from .models import Noodle
# Create your views here.



class Home(TemplateView):
    template_name="home.html"


class NoodleView(TemplateView):
    template_name="noodle_list.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        name= self.request.GET.get('name')
        if name != None:
            context["noodle"]= Noodle.objects.filter(name__icontains=name)
        else:
            context["noodle"] = Noodle.objects.all()
        return context
   


    
class NoodleNew(CreateView):
    model = Noodle
    fields = ['name','img']
    template_name = 'noodle_new.html'
    success_url = '/noodles/'

    

class NoodleAbout(DetailView):
    model = Noodle
    template_name = 'noodle_about.html'