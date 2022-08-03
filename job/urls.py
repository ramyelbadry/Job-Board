from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.job_ist),
    path('<int:id>', views.job_detail)
]