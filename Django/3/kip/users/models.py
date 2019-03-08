from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# for user models

myComment = '''
class UserRole(models.Model):
    group_name = models.CharField(max_length=50, unique=True)
    role_name = models.CharField(max_length=50, unique=True)
    permission = models.CharField(max_length=50)

    def __unicode__(self):
        return self.role_name


class Users(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
  #  role = models.ForeignKey('UserRole', on_delete=models.CASCADE, default=1)
    email = models.EmailField(max_length=100, null=False)
    group = models.CharField(max_length=50, default=' ')
    title = models.CharField(max_length=50, null=True)
    nameid = models.CharField(max_length=50, null=True)
    session_index = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.first_name + self.last_name

'''


# extending User Model with extra fields
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    session_index = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=50, default=' ')

    def __unicode__(self):
        return self.user.username


class Widgets(models.Model):
    name = models.CharField(max_length=50, null=False)
    unique_name = models.CharField(max_length=50, null=False)

    def __unicode__(self):
        return self.name


class UserWidgets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    widget = models.ForeignKey(Widgets, on_delete=models.CASCADE)
    order = models.IntegerField(default=1)


class UserWidgetList(models.Model):
    username = models.CharField(max_length=100, null=True)
    widgetlist = models.CharField(max_length=200, default='[]')                         # save list as array for now


MESSAGE_TYPE =(
    ('NOTE', 'New Note'),
    ('PERSONAL', 'Personal Message'),
    ('GROUP', 'Group Message')
)


class UserMessage(models.Model):
    user = models.ForeignKey(User, related_name='recipient_user', on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=MESSAGE_TYPE, default='NOTE')
    message = models.CharField(max_length=200, null=True, blank=True)
    read = models.BooleanField(default=False)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    update_time = models.DateTimeField(max_length=200, default=timezone.now)


