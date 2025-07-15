from django.shortcuts import render
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# Function Based API Views
"""
@api_view(['GET','POST'])
def ItemView(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        date = request.data
        serializer = ItemSerializer(data=date)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def ItemDetailView(request,pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ItemSerializer(item,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
"""

#Class Based API View
"""
class ItemView(APIView):
    def get(self,request):
        items = Item.objects.all()
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        date = request.data
        serializer = ItemSerializer(data=date)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
class ItemDetailView(APIView):

    def get_object(self,pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,pk):
        try:
            item = self.get_object(pk)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 """

        

    
