from . import views
from django.urls import path
from . import views
from django.contrib import messages

urlpatterns = [
    path('register/', views.register, name = 'register'),
    

]

