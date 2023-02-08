from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name = 'index'), # главная страница
    path('group_list/<slug:slug>/', views.group_posts, name = 'group_list'),
] 