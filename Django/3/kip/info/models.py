from django.db import models


class ContentType(models.Model):
    type = models.CharField(max_length=10, null=False)
    type_name = models.CharField(max_length=100, null=False)


class Content(models.Model):
    url = models.URLField(null=False)
    title = models.CharField(max_length=200, null=True)
    type = models.ForeignKey('ContentType', null=False, default=1, on_delete=models.CASCADE)
    content = models.TextField(null=False)