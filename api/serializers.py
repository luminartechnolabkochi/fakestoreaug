from rest_framework import  serializers
from api.models import Products
from django.contrib.auth.models import User
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

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password"]


# localhost:8000/api/users/
# method:post
# {first_name:"ram","last_name":"ra","email":"ram@gmail.com",username:"django",password:"abc123"}