from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect

from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def article_page(request, article_id):
    # article = models.Article.objects.get(pk=article_id)
    article = get_object_or_404(models.Article, pk=article_id)
    return render(request, 'article_page.html', {'article': article})

def edit_page(request, article_id):
    if article_id == '0':
        return render(request, 'edit_page.html')
    article = get_object_or_404(models.Article, pk=article_id)
    return render(request, 'edit_page.html', {'article': article})

def article_new(request):
    article_id = request.POST.get('article_id', 0)
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')

    if article_id == 0:
        models.Article.objects.create(title=title, content=content)
        # articles = models.Article.objects.all()
        # return render(request, 'index.html', {'articles': articles})
        return redirect('/blog/index')

    article = get_object_or_404(models.Article, pk=article_id)

    article.title = title
    article.content = content
    # print(article)
    article.save()
    return redirect('/blog/index')
    # return render(request, 'article_page.html', {'article': article})

def article_dele(request, article_id):
    article = get_object_or_404(models.Article, pk=article_id)
    article.delete()
    return redirect('/blog/index')
