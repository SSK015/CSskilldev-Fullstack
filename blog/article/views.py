from django.shortcuts import render

from django.http import HttpResponse
from .models import ArticlePost
# 视图函数
def article_list(request):
    articles = ArticlePost.objects.all();
    context = {'articles': articles}
    return render(request, 'article/list.html', context)

    # return HttpResponse("Hello world!")
# Create your views here.

def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    context = { 'article': article}
    return render(request, 'article/detail.html', context)

