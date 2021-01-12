from django.shortcuts import render

# Create your views here.

# Create your views here.

def index(request):
    if request.method == 'POST':
        article = Article(title=request.POST['title'], text=request.POST['text'], posted_at=timezone.now())
        article.save()
    if ('sort' in request.GET):
        if  request.GET['sort'] == 'date':
            articles = Article.objects.order_by('-posted_at')
        elif  request.GET['sort'] == 'like':
                articles = Article.objects.order_by('-like')
        print(request.GET['sort'])
    else:
        print('No sort')
        articles = Article.objects.order_by('-posted_at')
    context = {
        'articles': articles
    }
    return render(request, 'shop/index.html', context)

def update(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")

    if request.method == 'POST':
        article.title = request.POST['title']
        article.text= request.POST['text']
        article.save()
        return redirect(detail, article_id)

    context = {
        'article': article
    }
    return render(request, 'shop/???.html', context)

def delete(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    
    article.delete()
    return redirect(index)
