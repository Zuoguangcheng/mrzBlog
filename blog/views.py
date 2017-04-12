from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView

from blog.models import Article


class BlogView(ListView):
    # print(1)
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    model = Article
    # def get_context_data(self, **kwargs):
    #     context = super(BlogView, self).get_context_data(**kwargs)


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
