from rest_framework import serializers
from shipment.models import 거래처, 현장, 출하, 수주

# class 수주(models.Model):
#     번호 = models.CharField(max_length=200)
#     일자 = models.DateField(default=date.today)
#     원청=  models.ForeignKey('거래처', on_delete=models.CASCADE, default=00)
#     현장 = models.ForeignKey('현장', on_delete=models.CASCADE, default=00)
#
#     class Meta:
#         ordering = ['번호']
#

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = 수주
        fields = ('번호', '일자', '원청', '현장')

class CustomerSerializer(serializers.Serializer):
    ##코드 = serializers.CharField(max_length=200, default='0000')
    거래처명 = serializers.CharField(max_length=200)
    대표자 = serializers.CharField(max_length=200)
    주소 = serializers.CharField(max_length=200)
    연락처1 = serializers.CharField(max_length=200)
    연락처2 = serializers.CharField(max_length=200)
    연락처3 = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
