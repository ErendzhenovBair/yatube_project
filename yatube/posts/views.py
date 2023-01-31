from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


#Главная страница
def index(request):    
    return HttpResponse('Дневники твоих любимых блогеров')


# Страница с постами, отфильтрованными по группам

def group_posts(request, slug):
    return HttpResponse(f'Здесь будут посты {slug}, отфильтрованные по группам')


