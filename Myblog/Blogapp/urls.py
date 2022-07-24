from django.urls import path
from Blogapp.views import PostList, DetailView
urlpatterns = [
    path('', PostList.as_view(), name = 'home'),
    path('<slug:slug>/', DetailView.as_view(), name = 'post_detail')

]

