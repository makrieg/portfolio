from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'marketplace'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='marketplace/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('skills/<int:pk>/', views.skill_detail, name='skill_detail'),
    path('skills/create/', views.skill_create, name='skill_create'),
    path('skills/<int:pk>/edit/', views.skill_update, name='skill_update'),
    path('skills/<int:pk>/delete/', views.skill_delete, name='skill_delete'),
    path('skills/<int:skill_pk>/request/', views.booking_request_create, name='booking_request_create'),
    path('booking-requests/received/', views.booking_requests_received, name='booking_requests_received'),
    path('booking-requests/sent/', views.booking_requests_sent, name='booking_requests_sent'),
    path('booking-requests/<int:pk>/status/<str:status>/', views.booking_request_update_status, name='booking_request_update_status'),
]
