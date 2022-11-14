from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Products
from api.serializers import ProductSerializer,ProductModelSerializer
from rest_framework import viewsets

class ProductView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        serializer=ProductSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kw):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
#id
class ProductDetailsView(APIView):

    def get(self,request,*args,**kw):
        id=kw.get("id")
        qs=Products.objects.get(id=id)
        serializer=ProductSerializer(qs,many=False)
        return Response(data=serializer.data)


    def put(self,request,*args,**kw):
        id=kw.get("id")
        Products.objects.filter(id=id).update(**request.data)
        qs=Products.objects.get(id=id)
        serializer=ProductSerializer(qs,many=False)
        return Response(data=serializer.data)

    def delete(self,request,*args,**kw):
        id=kw.get("id")
        Products.objects.filter(id=id).delete()
        return Response(data="object deleted")


# ViewSets

class ProductViewsetView(viewsets.ViewSet):

    def list(self,request,*args,**kw):
        qs=Products.objects.all()
        serializer=ProductModelSerializer(qs,many=True)
        return Response(data=serializer.data)


