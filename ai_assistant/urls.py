"""
AI Assistant URL routing.
"""
from django.urls import path
from . import views

app_name = 'ai_assistant'

urlpatterns = [
    path('chat/', views.ai_chat, name='ai_chat'),
    path('resume-analysis/', views.ai_resume_analysis, name='ai_resume_analysis'),
]
