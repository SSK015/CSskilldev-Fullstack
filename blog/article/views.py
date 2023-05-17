from django.shortcuts import render

from django.http import HttpResponse
from .models import ArticlePost
# 视图函数
import markdown

def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)

    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])

    context = { 'article': article }
    return render(request, 'article/detail.html', context)

def article_list(request):
    article = ArticlePost.objects.all();
    context = {'article': article}
    return render(request, 'article/list.html', context)

    # return HttpResponse("Hello world!")
# Create your views here.

