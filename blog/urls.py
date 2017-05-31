from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^single$', views.get_single, name='single'),
    url(r'^article_list$', views.get_article_list, name='article_list'),
    url(r'^article_create$', views.article_create, name='article_create'),
]
