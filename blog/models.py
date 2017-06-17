from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    markdown = models.TextField(u'markdown原始文本')
    category = models.CharField(u'类型', max_length=256)

    pub_date = models.DateTimeField(u'发表时间', auto_now=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article_id = models.CharField(u'文章索引', max_length=128)
    content = models.TextField(u'评论内容')

    def __str__(self):
        return self.article_id + self.content


class User(models.Model):
    name = models.CharField(u'用户名', max_length=128)
    password = models.CharField(u'密码', max_length=20)
    login_sequence = models.CharField(u'登录序列', max_length=256)
    token = models.CharField(u'token', max_length=256)

    def __str__(self):
        return self.name
