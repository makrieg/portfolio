from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('resume/download/', views.resume_download, name='resume-download'),
    path('contact/', views.contact_view, name='contact'),
]
