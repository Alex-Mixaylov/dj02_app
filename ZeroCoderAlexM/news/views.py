from django.shortcuts import render
from .models import UserNewsPost

def user_news(request):
    user_news = UserNewsPost.objects.all()
    return render(request, 'news/news.html', {'user_news': user_news})

