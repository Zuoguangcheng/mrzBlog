from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BlogView.as_view(), name='index'),
    url(r'^about$', views.BlogAbout.as_view(), name='about'),
    url(r'^blog$', views.Blog.as_view(), name='blog'),
    url(r'^contact$', views.BlogContact.as_view(), name='contact'),
    url(r'^single/(?P<id>\d+)/$', views.BlogSingle.as_view(), name='single'),
    url(r'^article_list$', views.get_article_list, name='article_list')
]
