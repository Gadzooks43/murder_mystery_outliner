from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.projects_list_create, name='projects_list_create'),
    path('delete_project/<int:pk>/', views.delete_project, name='delete_project'),
    path('project/<path:project_name>/', views.project_detail, name='project_detail'),
]
