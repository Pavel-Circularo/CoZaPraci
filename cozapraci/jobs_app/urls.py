from django.urls import path
from .views import HomeView,ThankYouView,JobCreateView,JobDetailView,JobListView

app_name = "jobs_app"

urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("thank_you/",ThankYouView.as_view(),name='thank_you'),
    path("create_job/",JobCreateView.as_view(),name="create_job"),
    path("list_jobs/",JobListView.as_view(),name="list_jobs"),
    path("job/<int:pk>",JobDetailView.as_view(),name="job_detail")
]