from django.db import models
from datetime import date

class Item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.IntegerField()

class Job(models.Model):
    번호 =  models.CharField(max_length=200)
    예정량 =  models.IntegerField()

class standard_name(models.Model):
    m40= models.CharField(max_length=200, default='40mm')
    m25= models.CharField(max_length=200, default='25mm')
    m19 = models.CharField(max_length=200, default='19mm')
    m13 = models.CharField(max_length=200, default='13mm')
    m10 = models.CharField(max_length=200, default='10mm')
    sd= models.CharField(max_length=200, default='석분')
    sb1 = models.CharField(max_length=200, default='SB-1')
    sb2 = models.CharField(max_length=200, default='SB-2')

class 규격(models.Model):
    규격명=models.CharField(max_length=200, default=' ')
    단가=models.IntegerField(default=0)
    운반비=models.IntegerField(default=0)

class standard(models.Model):
    name=models.CharField(max_length=200, default=' ')
    price=models.IntegerField(default=0)
    cost=models.IntegerField(default=0)
    standard_name=models.ForeignKey('standard_name', on_delete=models.CASCADE, default=00)

class 차량(models.Model):
    차량번호=models.CharField(max_length=200, default=' ')
    기사이름=models.CharField(max_length=200, default=' ')
    기사연락처=models.CharField(max_length=200, default=' ')
    적재량=models.IntegerField()

class cars(models.Model):
    number=models.CharField(max_length=200, default=' ')
    name=models.CharField(max_length=200, default=' ')
    number=models.CharField(max_length=200, default=' ')
    loadage=models.IntegerField(default=0)


class 현장(models.Model):
    현장명=models.CharField(max_length=200, default=' ')
    규격=models.ForeignKey('규격', on_delete=models.CASCADE, default=00)


class sites(models.Model):
    code = models.CharField(max_length=200, default='0000')
    name=models.CharField(max_length=200, default=' ')
    ##standard=models.ForeignKey('standard', on_delete=models.CASCADE, default=00)
    address = models.CharField(max_length=200, default=' ')

    customer = models.ForeignKey('customers', on_delete=models.CASCADE, default=00)
    standards = models.CharField(max_length=200, default=' ')
    
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


class customers(models.Model):
    code = models.CharField(max_length=200, default='0000')
    name = models.CharField(max_length=200)
    chief = models.CharField(max_length=200, default=' ')
    address = models.CharField(max_length=200, default=' ')
    phone = models.CharField(max_length=200, default=' ')
    fax = models.CharField(max_length=200, default=' ')
    manager = models.CharField(max_length=200, default=' ')
    email = models.CharField(max_length=200, default=' ')
    ##site = models.ForeignKey('sites', on_delete=models.CASCADE, default=00)
    ##sites = models.CharField(max_length=400, default=' ')
    ##standard = models.ForeignKey('standard', on_delete=models.CASCADE, default=00)
    ##car = models.ForeignKey('cars', on_delete=models.CASCADE, default=00)

    class Meta:
        ordering = ['name']


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


class contracts(models.Model):
    number = models.CharField(max_length=200)
    ##date= models.DateField(default=date.today)
    date=models.CharField(max_length=20, default=date.today)
    order_customer=  models.ForeignKey('customers', on_delete=models.CASCADE, default=00,  related_name='order_customer')
    sub_customer = models.ForeignKey('customers', on_delete=models.CASCADE, default=00,related_name='sub_customer')
    site = models.ForeignKey('sites', on_delete=models.CASCADE, default=00)

    class Meta:
        ordering = ['number']