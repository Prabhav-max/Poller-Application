from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    FormView
)
from main import models,forms
from django.views.generic.detail import BaseDetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.

class Index(ListView):
    model=models.Question
    template_name='main/index.html'
    #context_object_name='question_list'  by default it goes by this name in template

class Question(PermissionRequiredMixin,BaseDetailView,FormView):
    model=models.Question
    template_name='main/question.html'
    form_class=forms.AnswerForm
    permission_required='add_answer'

    def get_context_data(self,**kwargs):
        data=super().get_context_data(**kwargs)
        data['answer']=models.Answer.objects.get(
            question=self.get_object(),
            user=self.request.user
        )
        return data   


    def form_valid(self,form):
        obj=form.save(commit=False) #Commit=False means that rightnow I don't want to save the form in database as user is not included
        obj.question=self.get_object()
        obj.user=self.request.user  #Here I jave included the user
        obj.save()  #Here I have saved the form
        return HttpResponseRedirect('/')