from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^single$', views.get_single, name='single'),
    url(r'^article_list$', views.get_article_list, name='article_list'),
    url(r'^article_create$', views.article_create, name='article_create'),
    url(r'^article_edit$', views.article_edit, name='article_edit'),
    url(r'^article_commit_create$', views.article_commit_create, name='article_create'),
    url(r'^get_article_commit$', views.get_article_commit, name='article_create'),
    url(r'^register$', views.register, name='register'),
    url(r'^sign$', views.sign, name='sign'),
    url(r'^is_login$', views.is_login, name='is_login'),
    url(r'^up_pic$', views.up_pic, name='up_pic'),
    url(r'^get_article_recent$', views.get_article_recent, name='get_article_recent'),
    url(r'^get_month$', views.get_month, name='get_month')
]
