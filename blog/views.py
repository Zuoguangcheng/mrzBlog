from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from blog.models import Article


class BlogView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    model = Article

    def get_queryset(self):
        value = Article.objects.all()[:5]
        return value

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        return context


class BlogAbout(ListView):
    template_name = 'blog/about.html'
    context_object_name = 'about_list'
    model = Article


class Blog(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'work_list'
    model = Article


class BlogContact(ListView):
    template_name = 'blog/contact.html'
    context_object_name = 'work_list'
    model = Article


class BlogSingle(ListView):
    template_name = 'blog/single.html'
    context_object_name = 'work_list'
    model = Article


def get_article_list(request):
    page = int(request.GET['page'])
    article_list = serializers.serialize("json", Article.objects.all()[page:page + 5])
    print(article_list)
    return JsonResponse(article_list, safe=False)
