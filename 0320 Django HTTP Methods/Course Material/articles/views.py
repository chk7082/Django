from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):

    articles = Article.objects.all()
    context = {'articles': articles}

    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}

    return render(request, 'articles/detail.html', context)

# def new(request):
#     return render(request, 'articles/new.html')

def create(request):


    if request.method == 'POST': # 게시글 작성 요청
        title = request.POST.get('title')
        content = request.POST.get('content')

        # # DB에 새로운 Article 저장
        # Article.objects.create(
        #     title=title,
        #     content=content
        # )

        article = Article(title=title, content=content)
        # ~~~~~~~~~~~~
        article.save()

        return redirect('articles:detail', article.pk)
    
    else: # 게시글 작성 페이지 요청
        return render(request, 'articles/create.html')

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {
#         'article': article,
#     }
#     return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {
            'article': article,
        }
        return render(request, 'articles/update.html', context)