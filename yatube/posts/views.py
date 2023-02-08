from django.shortcuts import render, get_object_or_404


from .models import Group, Post

from yatube.settings import NUMBER_OF_POSTS

#Главная страница
def index(request):    
    posts = Post.objects.order_by('-pub_date')[:NUMBER_OF_POSTS]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)    
    #return HttpResponse Главная страница

# Страница с постами, отфильтрованными по группам

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:NUMBER_OF_POSTS]
    title = f'Записи сообществ {group}'
    text = Group.description
    context = {
        'group': group,
        'posts': posts,
        'text': text,
    }
    return render(request, 'posts/group_posts.html', context) 
       
    


