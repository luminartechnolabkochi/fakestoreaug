from rest_framework import  serializers
from api.models import Products

class ProductSerializer(serializers.Serializer):

    id=serializers.CharField(read_only=True)
    name=serializers.CharField()
    price=serializers.IntegerField()
    description=serializers.CharField()
    category=serializers.CharField()
    image=serializers.ImageField()


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model=Products
        fields="__all__"
