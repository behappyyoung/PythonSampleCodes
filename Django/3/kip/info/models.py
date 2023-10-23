from django.db import models
import django.utils.timezone

class RecordDateMixin(models.Model):
    created_date = models.DateTimeField(default=django.utils.timezone.now)
    updated_date = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, help_text='null=main category')


class Tags(models.Model):
    name = models.CharField(max_length=100, null=False)
    other_name = models.CharField(max_length=100, null=False)


class ContentType(models.Model):
    type = models.CharField(max_length=10, null=False)
    type_name = models.CharField(max_length=100, null=False)


class Content(RecordDateMixin):
    url = models.URLField(null=True)
    title = models.CharField(max_length=200, null=True)
    content_type = models.ForeignKey(ContentType, null=False, default=1, on_delete=models.CASCADE)
    content_category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    contents = models.TextField(null=False)
    tags = models.TextField(null=True)


class ContentTags(RecordDateMixin):
    fail = models.BooleanField(blank=True, null=True)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
