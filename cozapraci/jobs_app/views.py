from dataclasses import fields
from re import template
from django_unicorn.components import UnicornView
from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView, CreateView,DetailView, FormView,ListView,UpdateView,DeleteView
from jobs_app.models import Job
from . import forms
from random import randint
from random import choice

# Create your views here.
class HomeView(TemplateView):
    template_name = 'jobs_app/home.html'

class ThankYouView(TemplateView):
    template_name = 'jobs_app/thank_you.html'

class JobCreateView(CreateView):
    model = Job
    form_class = forms.JobForm
    #fields = "__all__"
    success_url = reverse_lazy("jobs_app:thank_you")

class JobListView(ListView):
    model = Job
    query_set = Job.objects.order_by("job_name")
    context_object_name = 'jobs_list'

class JobSearchView(TemplateView):
    template_name = "jobs_app/job_list2.html"

class JobDetailView(DetailView):
    model = Job

def random_view(request):
    """this function returs random approved job from database"""

    approved_jobs = Job.objects.values_list("pk",flat=True).filter(is_approved=1)
    random_job = Job.objects.get(pk=choice(approved_jobs))
    context = {"job" : random_job}

    return render(request, 'jobs_app/job_detail.html', context=context)