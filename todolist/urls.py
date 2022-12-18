from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<str:id>/', views.edit, name='edit'),
    path('delete/<str:id>/', views.delete, name='delete'),
]
