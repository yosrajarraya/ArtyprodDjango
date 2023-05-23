from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('', views.index, name='index'),
    path('home/', views.home_index, name='home'),
    path('login/', views.login_index, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('project_create/', views.project_create, name='project_create'),
    path('service/', views.service, name='service'),
    path('personnel/create/', views.personnel_create, name='personnel_create'),
    path('teams/', views.team_list, name='team_list'),
    path('teams/<int:team_id>/', views.team_detail, name='team_detail'),
    path('teams/create/', views.team_create, name='team_create'),
    path('teams/<int:team_id>/update/', views.team_update, name='team_update'),
    path('teams/<int:team_id>/delete/', views.team_delete, name='team_delete'),
    path('contact/', views.contact, name='contact'),
    path('inscription/', views.register, name='register'),
]
