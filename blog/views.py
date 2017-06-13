from django.http import JsonResponse
from django.http import HttpResponse

from blog.models import Article
from blog.models import Comment
from blog.models import User

from django.core import serializers

import json


def get_single(request):
    article = list(Article.objects.filter(pk=int(request.GET['id'])).values())
    return JsonResponse(article, safe=False)


def get_article_list(request):
    if request.method == 'GET':

        page = int(request.GET['page'])
        category_id = request.GET['category_id']

        article_list = Article.objects.all()[0: page + 5]

        if category_id:
            article_list = Article.objects.filter(category=category_id)[0: page + 5]

        response = JsonResponse(list(article_list.values()), safe=False)
        # response.set_cookie('zuoguangcheng', 'zuoguangcheng')

        return response


def article_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']

        article = Article(title=title, content=content, category=category)
        article.save()

        return JsonResponse([], safe=False)


def article_commit_create(request):
    if request.method == 'POST':
        try:
            article_id = request.POST['article_id']
            content = request.POST['content']
        except Exception as e:
            print('e', e)
            return JsonResponse('参数不正确', safe=False)
        # if
        commit = Comment(article_id=article_id, content=content)
        commit.save()
        return JsonResponse([], safe=False)


def get_article_commit(request):
    if request.method == 'GET':
        try:
            article_id = request.GET['article_id']
        except Exception as e:
            print('Exception', e)

        commit_list = Comment.objects.filter(article_id=article_id)
        print('commit_list', commit_list)
        return JsonResponse(list(commit_list.values()), safe=False)


def register(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            password = request.POST['password']
        except Exception as e:
            print('e', e)
            return JsonResponse('参数不正确', safe=False)

        user_list = User.objects.filter(name=name)
        if user_list.exists():
            return HttpResponse('注册名称重复，请更改用户名')

        user = User(name=name, password=password)
        user.save()
        return HttpResponse('注册成功')


def sign(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            password = request.POST['password']
        except Exception as e:
            print('e', e)
            return JsonResponse('参数不正确', safe=False)

        user = User.objects.get(name=name)
        if password == user.password:
            response = HttpResponse('登录成功')
            response.set_cookie('login_sequence', 'login_sequence')
            response.set_cookie('token', 'token')
            return response
        else:
            response = HttpResponse('登录失败')
            return response
