from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('employee/<str:pk>/', views.employee, name="employee"),
    path('add_employee/', views.addEmployee, name ="add_employee"),
    path('update_employee/<str:pk>/', views.updateEmployee, name="update_employee"),
    path('delete_employee/<str:pk>/', views.deleteEmployee, name="delete_employee"),
]
