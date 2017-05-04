from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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


class BlogSingle(DetailView):
    template_name = 'blog/single.html'
    context_object_name = 'article'
    model = Article

    # def get_queryset(self):
    #     show_id = self.kwargs['id']
    #     value = Article.objects.filter(pk=show_id)
    #     print('value', value)
    #     return value

    # def get_context_data(self, **kwargs):
    #     context = super(BlogSingle, self).get_context_data(**kwargs)
    #     print('self', self)
    #     # context['article'] = Article.objects.filter(pk=show)

    def get_object(self, queryset=None):
        print('self', self.kwargs.get('id'))
        return Article.objects.get(pk=self.kwargs.get('id'))


def get_article_list(request):
    page = int(request.GET['page'])
    article_list = Article.objects.all()[page:page + 5]

    article_arr = list(article_list.values())

    print('article_arr', article_arr[0])
    return JsonResponse(article_arr, safe=False)
