from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView
from app.forms import *

class cbv_html(TemplateView):
    template_name='cbv_html.html'


class cbv_context(TemplateView):
    template_name='cbv_context.html'
    
    def get_context_data(self, **kwargs):
        co=super().get_context_data(**kwargs)
        co['name']='rahul'
        co['age']=23
        return co
    
class cbv_form(TemplateView):
    template_name='cbv_form.html'

    def get_context_data(self, **kwargs):
        co= super().get_context_data(**kwargs)
        co['form']=TopicForm()
        return co
    
    def post(self,request):
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('data saved successfully')



