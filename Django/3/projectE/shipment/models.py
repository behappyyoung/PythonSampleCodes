from django.db import models
from datetime import date

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()

class Job(models.Model):
    번호 =  models.CharField(max_length=200)
    예정량 =  models.IntegerField()

class 규격명(models.Model):
    m40= models.CharField(max_length=200, default='40mm')
    m25= models.CharField(max_length=200, default='25mm')
    m19 = models.CharField(max_length=200, default='19mm')
    m13 = models.CharField(max_length=200, default='13mm')

class 규격(models.Model):
    규격명=models.CharField(max_length=200, default=' ')
    단가=models.IntegerField()
    운반비=models.IntegerField()

class 차량(models.Model):
    차량번호=models.CharField(max_length=200, default=' ')
    기사이름=models.CharField(max_length=200, default=' ')
    기사연락처=models.CharField(max_length=200, default=' ')
    적재량=models.IntegerField()

class 현장(models.Model):
    현장명=models.CharField(max_length=200, default=' ')
    규격=models.ForeignKey('규격', on_delete=models.CASCADE, default=00)

    
class 거래처(models.Model):
    코드= models.CharField(max_length=200, default='0000')
    거래처명=models.CharField(max_length=200)
    대표자 = models.CharField(max_length=200)
    주소 = models.CharField(max_length=200)
    전화 = models.CharField(max_length=200)
    팩스 = models.CharField(max_length=200)
    담당자 = models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    현장 = models.ForeignKey('현장', on_delete=models.CASCADE, default=00)
    규격 = models.ForeignKey('규격', on_delete=models.CASCADE, default=00)
    차량 = models.ForeignKey('차량', on_delete=models.CASCADE, default=00)

    class Meta:
        ordering = ['거래처명']


class 출하(models.Model):
    번호 = models.CharField(max_length=200)
    예정량 = models.IntegerField()
    거래처= models.ForeignKey('거래처', on_delete=models.CASCADE, default=00)
    현장=models.ForeignKey('현장',on_delete=models.CASCADE, default=00)
    사각= models.CharField(max_length=200)
    차량 = models.CharField(max_length=200)

    class Meta:
        ordering = ['번호']

class 수주(models.Model):
    번호 = models.CharField(max_length=200)
    일자 = models.DateField(default=date.today)
    원청=  models.ForeignKey('거래처', on_delete=models.CASCADE, default=00)
    현장 = models.ForeignKey('현장', on_delete=models.CASCADE, default=00)

    class Meta:
        ordering = ['번호']
