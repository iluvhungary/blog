from django.urls import path
from . import views

app_name = 'blogapp'  # Define the namespace for the app
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('del/<int:pk>/', views.delete, name='delete'),
]
