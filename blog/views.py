from django.http import JsonResponse
from django.http import HttpResponse
import django.utils.timezone as timezone

from blog.models import Article
from blog.models import Comment
from blog.models import User

from blog.lib import Lib

from django.core import serializers

import json
import time
from datetime import datetime, timedelta
import base64


def log(func):
    def _log(*args, **kwargs):
        print('args', args[0].method)
        print('args', json.dumps(args[0].GET))
        print('args', json.dumps(args[0].POST))
        return func(*args, **kwargs)

    return _log


@log
def get_single(request):
    article = list(Article.objects.filter(pk=int(request.GET['id'])).values())
    return JsonResponse(article, safe=False)


def get_article_list(request):
    if request.method == 'GET':

        page = int(request.GET['page'])
        category_id = request.GET['category_id']
        month = request.GET['month']

        article_list = Article.objects.all()

        if month:
            start_month_time = datetime.strptime(month, "%Y-%m")
            end_month_time = datetime(start_month_time.year, (start_month_time.month + 1), start_month_time.day)
            article_list = article_list.filter(update_time__range=(start_month_time, end_month_time))

        if category_id:
            article_list = article_list.filter(category=category_id)

        response = JsonResponse(list(article_list[0: page + 5].values()), safe=False)

        return response


def get_article_recent(request):
    if request.method == 'GET':
        article_list = Article.objects.all().order_by('-update_time')[0:3]
        return JsonResponse(list(article_list.values()), safe=False)


@log
def get_month(request):
    if request.method == 'GET':
        month = Article.objects.all().values('pub_date')
        month_set = set()

        for item in month:
            item['pub_date'] = item['pub_date'].strftime('%Y-%m')
            month_set.add(item['pub_date'])

        return JsonResponse(list(month_set), safe=False)


def article_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        markdown = request.POST['markdown']
        category = request.POST['category']

        article = Article(title=title, content=content, markdown=markdown, category=category)
        article.save()

        return JsonResponse([], safe=False)


def article_edit(request):
    if request.method == 'POST':
        id = request.POST['id']
        title = request.POST['title']
        content = request.POST['content']
        markdown = request.POST['markdown']
        category = request.POST['category']
        article = Article.objects.filter(pk=id)
        article.update(title=title, content=content, markdown=markdown, category=category, update_time=timezone.now())

        return JsonResponse([], safe=False)
    else:
        return JsonResponse('请求错误', safe=False)


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


@log
def get_article_commit(request):
    if request.method == 'GET':
        try:
            article_id = request.GET['article_id']
        except Exception as e:
            print('Exception', e)

        commit_list = Comment.objects.filter(article_id=article_id)
        print('commit_list', commit_list)
        return JsonResponse(list(commit_list.values()), safe=False)


# 注册
def register(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            password = request.POST['password']
        except Exception as e:
            print('e', e)
            return JsonResponse({'code': 0, 'msg': '参数不正确'}, safe=False)

        user_list = User.objects.filter(name=name)
        if user_list.exists():
            return JsonResponse({'code': 0, 'msg': '注册名称重复，请更改用户名'}, safe=False)

        user = User(name=name, password=password)
        user.save()
        return JsonResponse({'code': 1, 'msg': '注册成功，请登录'}, safe=False)


# 用户名密码登录
def sign(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            password = request.POST['password']
        except Exception as e:
            print('e', e)
            return JsonResponse({'code': 0, 'msg': '参数不正确'}, safe=False)

        try:
            user = User.objects.get(name=name)
        except Exception as e:
            print('e', e)
            return JsonResponse({'code': 0, 'msg': '该用户未注册，请注册后登录'}, safe=False)

        if password == user.password:

            string = name + str(time.time())
            login_sequence = Lib.md5encode(string)
            token = Lib.md5encode(str(time.time()))

            user.login_sequence = login_sequence
            user.token = token
            user.save()

            response = JsonResponse({'code': 1, 'msg': '登录成功'}, safe=False)
            response.set_cookie('name', Lib.base64encode(name), 2592000)
            response.set_cookie('login_sequence', login_sequence, 2592000)
            response.set_cookie('token', token)
            return response
        else:
            response = JsonResponse({'code': 0, 'msg': '登录失败'}, safe=False)
            return response


# 判断cookie是否登录
def is_login(request):
    if request.method == 'GET':
        try:
            name = Lib.base64decode(request.COOKIES['name'])
            login_sequence = request.COOKIES['login_sequence']
            token = request.COOKIES['token']
        except Exception as e:
            print('is_login_e', e)
            return JsonResponse({'code': 0, 'msg': '请重新登录'}, safe=False)

        try:
            user = User.objects.get(name=name)
        except Exception as e:
            print('e', e)
            return JsonResponse({'code': 0, 'msg': '用户不存在，请重新登录或注册'}, safe=False)

        if user.login_sequence == login_sequence and user.token == token:
            token = Lib.md5encode(str(time.time()))
            response = JsonResponse({'code': 1, 'msg': '登录成功'}, safe=False)
            response.set_cookie('token', token)

            user.token = token
            user.save()

            return response
        else:
            return JsonResponse({'code': 0, 'msg': '请重新登录'}, safe=False)


def up_pic(request):
    try:
        pic = request.FILES['file']
    except Exception as e:
        print('e', e)
        print('request', request)
        return JsonResponse({'code': 0, 'msg': '失败'}, safe=False)

    print('pic', pic)
    # print('pic', pic.read())

    path = 'me.png'
    data = pic.read()

    with open(path, 'wb') as file:
        file.write(data)

    return JsonResponse({'code': 1, 'msg': '成功'}, safe=False)
