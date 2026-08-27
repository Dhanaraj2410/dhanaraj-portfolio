"""
GitHub integration URL routing.
"""
from django.urls import path
from . import views

app_name = 'github_integration'

urlpatterns = [
    path('', views.github_api, name='github_api'),
]
