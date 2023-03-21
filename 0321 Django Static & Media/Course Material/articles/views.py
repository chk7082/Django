from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

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
        form = ArticleForm(request.POST, request.FILES)
        
        if form.is_valid():
            # print('#'*80)
            # print(form.cleaned_data)
            # print('#'*80)
            article = form.save()
            return redirect('articles:detail', article.pk)
        
        # title = request.POST.get('title')
        # content = request.POST.get('content')

        # # # DB에 새로운 Article 저장
        # # Article.objects.create(
        # #     title=title,
        # #     content=content
        # # )

        # article = Article(title=title, content=content)
        # # ~~~~~~~~~~~~
        # article.save()

        
    
    else: # 게시글 작성 페이지 요청
        form = ArticleForm()
    
    context = {'form': form}
    return render(request, 'articles/create.html', context)
    
        

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
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save() # 이미 위에서 받고 있으니, 굳이 받을 필요 X
            return redirect('articles:detail', article.pk)

        # article.title = request.POST.get('title')
        # article.content = request.POST.get('content')
        # article.save()
        # return redirect('articles:detail', article.pk)
    
    else:
        # 비어 있는 form이 아니라 기존의 article을 채운 form 이어야함
        form = ArticleForm(instance=article)


    # context = {
    #     'article': article,
    # }
    
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)