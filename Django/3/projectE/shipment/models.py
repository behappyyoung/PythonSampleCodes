from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()

class Job(models.Model):
    번호 =  models.CharField(max_length=200)
    예정량 =  models.IntegerField()

class 거래처(models.Model):
    코드= models.CharField(max_length=200)
    거래처명=models.CharField(max_length=200)

class 현장(models.Model):
    현장명=models.CharField(max_length=200)

class 출하(models.Model):
    번호 = models.CharField(max_length=200)
    예정량 = models.IntegerField()
    거래처= models.ForeignKey(거래처)
    현장=models.ForeignKey(현장)