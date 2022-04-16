from dataclasses import fields
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

class JobDetailView(DetailView):
    model = Job

def random_view(request):
    #all_jobs = Job.objects.all()
    #random_job = all_jobs[randint(1,len(all_jobs)-1)]

    pks = Job.objects.values_list('pk', flat=True)
    random_pk = choice(pks)
    random_job = Job.objects.get(pk=random_pk)
    context = {"job" : random_job}
    return render(request, 'jobs_app/job_detail.html', context=context)