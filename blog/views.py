from django.http import JsonResponse
from blog.models import Article


def get_single(request):
    article = list(Article.objects.filter(pk=int(request.GET['id'])).values())
    return JsonResponse(article, safe=False)


def get_article_list(request):
    page = int(request.GET['page'])
    article_list = Article.objects.all()[0:page + 5]

    article = []
    for item in article_list:
        article.append({'title': item.title, 'content': item.content, 'id': item.id})
    response = JsonResponse(article, safe=False)
    return response


def article_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']

        article = Article(title=title, content=content, category=category)
        article.save()

        return JsonResponse([], safe=False)
