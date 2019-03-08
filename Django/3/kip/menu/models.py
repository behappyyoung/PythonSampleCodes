from django.db import models


class Tags(models.Model):
    tag = models.CharField(max_length=20, null=False)
    url_list = models.TextField(null=False)
    count = models.IntegerField(null=False, default=1)


class Menu(models.Model):
    parent = models.ForeignKey('self')
    name = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=200, null=True)
    info = models.ForeignKey('info.Content', null=False)
