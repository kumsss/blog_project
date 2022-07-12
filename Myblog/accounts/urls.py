from . import views
from django.urls import path
from .views import register

urlpatterns = [
    path('register/', views.register, name = 'register'),
    

]

